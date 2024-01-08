from functools import cached_property
from typing_extensions import ParamSpec
from typing import (
    TYPE_CHECKING,
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
from .paginator import Paginator
from .auth import BaseAuthStrategy
from .versions import RestVersionSwitcher, WebhooksVersionSwitcher
from .graphql import GraphQLResponse, build_graphql_request, parse_graphql_response

if TYPE_CHECKING:
    import httpx

    from .config import Config
    from .auth import TokenAuthStrategy, UnauthAuthStrategy


A = TypeVar("A", bound=BaseAuthStrategy)
A_o = TypeVar("A_o", bound=BaseAuthStrategy)

CP = ParamSpec("CP")
CT = TypeVar("CT")
RT = TypeVar("RT")

R = Union[
    Callable[CP, Response[RT]],
    Callable[CP, Awaitable[Response[RT]]],
]


class GitHub(GitHubCore[A]):
    if TYPE_CHECKING:
        # none auth with config
        @overload
        def __init__(
            self: "GitHub[UnauthAuthStrategy]",
            auth: None = None,
            *,
            config: Config,
        ):
            ...

        # token auth with config
        @overload
        def __init__(
            self: "GitHub[TokenAuthStrategy]",
            auth: str,
            *,
            config: Config,
        ):
            ...

        # other auth strategies with config
        @overload
        def __init__(
            self: "GitHub[A]",
            auth: A,
            *,
            config: Config,
        ):
            ...

        # none auth without config
        @overload
        def __init__(
            self: "GitHub[UnauthAuthStrategy]",
            auth: None = None,
            *,
            base_url: Optional[Union[str, httpx.URL]] = None,
            accept_format: Optional[str] = None,
            previews: Optional[List[str]] = None,
            user_agent: Optional[str] = None,
            follow_redirects: bool = True,
            timeout: Optional[Union[float, httpx.Timeout]] = None,
            http_cache: bool = True,
        ):
            ...

        # token auth without config
        @overload
        def __init__(
            self: "GitHub[TokenAuthStrategy]",
            auth: str,
            *,
            base_url: Optional[Union[str, httpx.URL]] = None,
            accept_format: Optional[str] = None,
            previews: Optional[List[str]] = None,
            user_agent: Optional[str] = None,
            follow_redirects: bool = True,
            timeout: Optional[Union[float, httpx.Timeout]] = None,
            http_cache: bool = True,
        ):
            ...

        # other auth strategies without config
        @overload
        def __init__(
            self: "GitHub[A]",
            auth: A,
            *,
            base_url: Optional[Union[str, httpx.URL]] = None,
            accept_format: Optional[str] = None,
            previews: Optional[List[str]] = None,
            user_agent: Optional[str] = None,
            follow_redirects: bool = True,
            timeout: Optional[Union[float, httpx.Timeout]] = None,
            http_cache: bool = True,
        ):
            ...

        def __init__(self, *args, **kwargs):
            ...

    # copy github instance with other auth
    def with_auth(self, auth: A_o) -> "GitHub[A_o]":
        return GitHub(auth=auth, config=self.config.copy())

    # rest api
    @cached_property
    def rest(self) -> RestVersionSwitcher:
        return RestVersionSwitcher(self)

    # webhooks
    webhooks = WebhooksVersionSwitcher()

    # graphql
    def graphql(
        self, query: str, variables: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        json = build_graphql_request(query, variables)

        return parse_graphql_response(
            self,
            self.request("POST", "/graphql", json=json, response_model=GraphQLResponse),
        )

    async def async_graphql(
        self, query: str, variables: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        json = build_graphql_request(query, variables)

        return parse_graphql_response(
            self,
            await self.arequest(
                "POST", "/graphql", json=json, response_model=GraphQLResponse
            ),
        )

    # rest pagination
    @overload
    @staticmethod
    def paginate(
        request: R[CP, List[RT]],
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
        map_func: Callable[[Response[CT]], List[RT]] = ...,  # type: ignore
        *args: CP.args,
        **kwargs: CP.kwargs,
    ) -> Paginator[RT]:
        ...

    @staticmethod
    def paginate(
        request: R[CP, CT],
        page: int = 1,
        per_page: int = 100,
        map_func: Optional[Callable[[Response[CT]], List[RT]]] = None,
        *args: CP.args,
        **kwargs: CP.kwargs,
    ) -> Paginator[RT]:
        return Paginator(
            request, page, per_page, map_func, *args, **kwargs  # type: ignore
        )
