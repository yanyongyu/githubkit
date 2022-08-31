from functools import cached_property
from typing_extensions import ParamSpec
from typing import (
    Any,
    Dict,
    List,
    Union,
    TypeVar,
    Callable,
    Optional,
    Awaitable,
    overload,
)

from .core import GitHubCore
from .response import Response
from .rest import RestNamespace
from .paginator import Paginator
from .auth import BaseAuthStrategy
from .graphql import GraphQLResponse, build_graphql_request, parse_graphql_response

A = TypeVar("A", bound=BaseAuthStrategy)
A_o = TypeVar("A_o", bound=BaseAuthStrategy)

CP = ParamSpec("CP")
CT = TypeVar("CT")
RT = TypeVar("RT")

R = Union[
    Callable[CP, Response[List[RT]]],
    Callable[CP, Awaitable[Response[List[RT]]]],
]


class GitHub(GitHubCore[A]):
    # copy github instance with other auth
    def with_auth(self, auth: A_o) -> "GitHub[A_o]":
        return GitHub(auth=auth, config=self.config.copy())

    # rest api
    @cached_property
    def rest(self) -> RestNamespace:
        return RestNamespace(self)

    # graphql
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

    # rest pagination
    @overload
    @staticmethod
    def paginate(
        request: R[CP, RT],
        page: int = 1,
        per_page: int = 100,
        map_func: None = None,
        *args: CP.args,
        **kwargs: CP.kwargs,
    ) -> Paginator[RT]:
        ...

    @overload
    @staticmethod
    def paginate(
        request: R[CP, CT],
        page: int = 1,
        per_page: int = 100,
        map_func: Callable[[Response[List[CT]]], List[RT]] = ...,  # type: ignore
        *args: CP.args,
        **kwargs: CP.kwargs,
    ) -> Paginator[RT]:
        ...

    @staticmethod
    def paginate(
        request: R[CP, CT],
        page: int = 1,
        per_page: int = 100,
        map_func: Optional[Callable[[Response[List[CT]]], List[RT]]] = None,
        *args: CP.args,
        **kwargs: CP.kwargs,
    ) -> Paginator[RT]:
        return Paginator(request, page, per_page, map_func, *args, **kwargs)  # type: ignore
