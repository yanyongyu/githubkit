import re
from weakref import ref
from typing import TYPE_CHECKING, Any, Dict, Optional, cast

from githubkit.exception import GraphQLFailed, PrimaryRateLimitExceeded

from .paginator import Paginator as Paginator
from .models import GraphQLError as GraphQLError
from .models import SourceLocation as SourceLocation
from .models import GraphQLResponse as GraphQLResponse

if TYPE_CHECKING:
    from githubkit.core import GitHubCore
    from githubkit.response import Response


class GraphQLNamespace:
    def __init__(self, github: "GitHubCore") -> None:
        self._github_ref = ref(github)

    @property
    def _github(self) -> "GitHubCore":
        if g := self._github_ref():
            return g
        raise RuntimeError(
            "GitHub client has already been collected. "
            "Do not use the namespace after the client has been collected."
        )

    @staticmethod
    def build_graphql_request(
        query: str, variables: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        json: Dict[str, Any] = {"query": query}
        if variables:
            json["variables"] = variables
        return json

    def _get_graphql_endpoint(self) -> str:
        base_url = self._github.config.base_url
        path = base_url.path
        # workaround for GitHub Enterprise baseUrl set with /api/v3 suffix
        # https://github.com/octokit/graphql.js/pull/186
        # https://github.com/octokit/graphql.js/blob/dae781b027c19bcd458577cd9ac6ca888b2fdfeb/src/graphql.ts#L67-L72
        path, n = re.subn(r"/api/v3/?$", "/api/graphql", path, count=1)
        # if replaced, return the new path
        if n:
            return str(base_url.copy_with(path=path))
        return "/graphql"

    def parse_graphql_response(
        self, response: "Response[GraphQLResponse]"
    ) -> Dict[str, Any]:
        response_data = response.parsed_data
        if response_data.errors:
            # check rate limit exceeded
            # https://docs.github.com/en/graphql/overview/rate-limits-and-node-limits-for-the-graphql-api#exceeding-the-rate-limit
            # x-ratelimit-remaining may not be 0, ignore it
            # https://github.com/octokit/plugin-throttling.js/pull/636
            if any(error.type == "RATE_LIMITED" for error in response_data.errors):
                raise PrimaryRateLimitExceeded(
                    response, self._github._extract_retry_after(response)
                )
            raise GraphQLFailed(response_data)
        return cast(Dict[str, Any], response_data.data)

    def _request(
        self, query: str, variables: Optional[Dict[str, Any]] = None
    ) -> "Response[GraphQLResponse]":
        json = self.build_graphql_request(query, variables)

        return self._github.request(
            "POST",
            self._get_graphql_endpoint(),
            json=json,
            response_model=GraphQLResponse,
        )

    def request(
        self, query: str, variables: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self.parse_graphql_response(self._request(query, variables))

    async def _arequest(
        self, query: str, variables: Optional[Dict[str, Any]] = None
    ) -> "Response[GraphQLResponse]":
        json = self.build_graphql_request(query, variables)

        return await self._github.arequest(
            "POST",
            self._get_graphql_endpoint(),
            json=json,
            response_model=GraphQLResponse,
        )

    async def arequest(
        self, query: str, variables: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self.parse_graphql_response(await self._arequest(query, variables))

    # backport for calling graphql directly
    def __call__(
        self, query: str, variables: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self.request(query, variables)

    def paginate(
        self, query: str, variables: Optional[Dict[str, Any]] = None
    ) -> Paginator:
        return Paginator(self, query, variables)
