from collections.abc import Awaitable, Sequence
from functools import cached_property
from typing import TYPE_CHECKING, Any, Callable, Optional, TypeVar, Union, overload
from typing_extensions import ParamSpec

from .auth import BaseAuthStrategy
from .core import GitHubCore
from .graphql import GraphQLNamespace
from .paginator import Paginator
from .response import Response
from .typing import RetryDecisionFunc
from .versions import RestVersionSwitcher, WebhooksVersionSwitcher

if TYPE_CHECKING:
    import ssl

    import httpx

    from .auth import TokenAuthStrategy, UnauthAuthStrategy
    from .cache import BaseCacheStrategy
    from .config import Config
    from .throttling import BaseThrottler


A = TypeVar("A", bound=BaseAuthStrategy)
AS = TypeVar("AS", bound=BaseAuthStrategy)

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
        ): ...

        # token auth with config
        @overload
        def __init__(
            self: "GitHub[TokenAuthStrategy]",
            auth: str,
            *,
            config: Config,
        ): ...

        # other auth strategies with config
        @overload
        def __init__(
            self: "GitHub[AS]",
            auth: AS,
            *,
            config: Config,
        ): ...

        # none auth without config
        @overload
        def __init__(
            self: "GitHub[UnauthAuthStrategy]",
            auth: None = None,
            *,
            base_url: Optional[Union[str, httpx.URL]] = None,
            accept_format: Optional[str] = None,
            previews: Optional[Sequence[str]] = None,
            user_agent: Optional[str] = None,
            follow_redirects: bool = True,
            timeout: Optional[Union[float, httpx.Timeout]] = None,
            ssl_verify: Union[bool, "ssl.SSLContext"] = ...,
            cache_strategy: Optional["BaseCacheStrategy"] = None,
            http_cache: bool = True,
            throttler: Optional["BaseThrottler"] = None,
            auto_retry: Union[bool, RetryDecisionFunc] = True,
            rest_api_validate_body: bool = True,
        ): ...

        # token auth without config
        @overload
        def __init__(
            self: "GitHub[TokenAuthStrategy]",
            auth: str,
            *,
            base_url: Optional[Union[str, httpx.URL]] = None,
            accept_format: Optional[str] = None,
            previews: Optional[Sequence[str]] = None,
            user_agent: Optional[str] = None,
            follow_redirects: bool = True,
            timeout: Optional[Union[float, httpx.Timeout]] = None,
            ssl_verify: Union[bool, "ssl.SSLContext"] = ...,
            cache_strategy: Optional["BaseCacheStrategy"] = None,
            http_cache: bool = True,
            throttler: Optional["BaseThrottler"] = None,
            auto_retry: Union[bool, RetryDecisionFunc] = True,
            rest_api_validate_body: bool = True,
        ): ...

        # other auth strategies without config
        @overload
        def __init__(
            self: "GitHub[AS]",
            auth: AS,
            *,
            base_url: Optional[Union[str, httpx.URL]] = None,
            accept_format: Optional[str] = None,
            previews: Optional[Sequence[str]] = None,
            user_agent: Optional[str] = None,
            follow_redirects: bool = True,
            timeout: Optional[Union[float, httpx.Timeout]] = None,
            ssl_verify: Union[bool, "ssl.SSLContext"] = ...,
            cache_strategy: Optional["BaseCacheStrategy"] = None,
            http_cache: bool = True,
            throttler: Optional["BaseThrottler"] = None,
            auto_retry: Union[bool, RetryDecisionFunc] = True,
            rest_api_validate_body: bool = True,
        ): ...

        def __init__(self, *args, **kwargs): ...

    # copy github instance with other auth
    def with_auth(self, auth: AS) -> "GitHub[AS]":
        return GitHub(auth=auth, config=self.config.copy())

    # rest api
    @cached_property
    def rest(self) -> RestVersionSwitcher:
        return RestVersionSwitcher(self)

    # webhooks
    webhooks = WebhooksVersionSwitcher()

    # graphql
    @cached_property
    def graphql(self) -> GraphQLNamespace:
        return GraphQLNamespace(self)

    # alias for graphql.arequest
    async def async_graphql(
        self, query: str, variables: Optional[dict[str, Any]] = None
    ) -> dict[str, Any]:
        return await self.graphql.arequest(query, variables)

    # rest pagination
    paginate = Paginator
