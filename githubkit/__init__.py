from functools import cached_property
from typing_extensions import ParamSpec
from typing import Any, Dict, List, Union, TypeVar, Callable, Optional, Awaitable

from .core import GitHubCore
from .rest import RestNamespace
from .response import Response as Response
from .paginator import Paginator as Paginator
from .auth import BasicAuthStrategy as BasicAuthStrategy
from .auth import TokenAuthStrategy as TokenAuthStrategy
from .graphql import GraphQLResponse, build_graphql_request, parse_graphql_response

RT = TypeVar("RT")
CP = ParamSpec("CP")


class GitHub(GitHubCore):
    @cached_property
    def rest(self) -> RestNamespace:
        return RestNamespace(self)

    def graphql(
        self, query: str, variables: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        json = build_graphql_request(query, variables)

        return parse_graphql_response(
            self.request("POST", "/graphql", json=json, response_model=GraphQLResponse)
        )

    async def async_graphql(
        self, query: str, variables: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        json = build_graphql_request(query, variables)

        return parse_graphql_response(
            await self.arequest(
                "POST", "/graphql", json=json, response_model=GraphQLResponse
            )
        )

    @staticmethod
    def paginate(
        request: Union[
            Callable[CP, Response[List[RT]]],
            Callable[CP, Awaitable[Response[List[RT]]]],
        ],
        page: int = 1,
        per_page: int = 100,
        *args: CP.args,
        **kwargs: CP.kwargs,
    ) -> Paginator[RT]:
        return Paginator(request, page, per_page, *args, **kwargs)
