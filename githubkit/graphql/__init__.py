from typing import TYPE_CHECKING, Any, Dict, Optional, cast

from githubkit.exception import GraphQLFailed, PrimaryRateLimitExceeded

from .models import GraphQLError as GraphQLError
from .models import SourceLocation as SourceLocation
from .models import GraphQLResponse as GraphQLResponse

if TYPE_CHECKING:
    from githubkit.core import GitHubCore
    from githubkit.response import Response


def build_graphql_request(
    query: str, variables: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    json: Dict[str, Any] = {"query": query}
    if variables:
        json["variables"] = variables
    return json


def parse_graphql_response(
    github: "GitHubCore", response: "Response[GraphQLResponse]"
) -> Dict[str, Any]:
    response_data = response.parsed_data
    if response_data.errors:
        # check rate limit exceeded
        # https://docs.github.com/en/graphql/overview/rate-limits-and-node-limits-for-the-graphql-api#exceeding-the-rate-limit
        # x-ratelimit-remaining may not be 0, ignore it
        # https://github.com/octokit/plugin-throttling.js/pull/636
        if any(error.type == "RATE_LIMITED" for error in response_data.errors):
            raise PrimaryRateLimitExceeded(
                response, github._extract_retry_after(response)
            )
        raise GraphQLFailed(response_data)
    return cast(Dict[str, Any], response_data.data)
