from collections.abc import Awaitable, Callable, Sequence
from functools import cached_property
from typing import TYPE_CHECKING, Any, TypeVar, overload
from typing_extensions import ParamSpec

from .auth import BaseAuthStrategy
from .core import GitHubCore
from .graphql import GraphQLNamespace
from .paginator import Paginator
from .response import Response
from .typing import EventHookTypes, ProxyTypes, RetryDecisionFunc
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

R = Callable[CP, Response[RT]] | Callable[CP, Awaitable[Response[RT]]]


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
            base_url: str | httpx.URL | None = None,
            accept_format: str | None = None,
            previews: Sequence[str] | None = None,
            user_agent: str | None = None,
            follow_redirects: bool = True,
            timeout: float | httpx.Timeout | None = None,
            ssl_verify: bool | "ssl.SSLContext" = ...,
            trust_env: bool = True,
            proxy: ProxyTypes | None = None,
            transport: httpx.BaseTransport | None = None,
            async_transport: httpx.AsyncBaseTransport | None = None,
            event_hooks: EventHookTypes | None = None,
            async_event_hooks: EventHookTypes | None = None,
            cache_strategy: "BaseCacheStrategy" | None = None,
            http_cache: bool = True,
            throttler: "BaseThrottler" | None = None,
            auto_retry: bool | RetryDecisionFunc = True,
            rest_api_validate_body: bool = True,
        ): ...

        # token auth without config
        @overload
        def __init__(
            self: "GitHub[TokenAuthStrategy]",
            auth: str,
            *,
            base_url: str | httpx.URL | None = None,
            accept_format: str | None = None,
            previews: Sequence[str] | None = None,
            user_agent: str | None = None,
            follow_redirects: bool = True,
            timeout: float | httpx.Timeout | None = None,
            ssl_verify: bool | "ssl.SSLContext" = ...,
            trust_env: bool = True,
            proxy: ProxyTypes | None = None,
            transport: httpx.BaseTransport | None = None,
            async_transport: httpx.AsyncBaseTransport | None = None,
            event_hooks: EventHookTypes | None = None,
            async_event_hooks: EventHookTypes | None = None,
            cache_strategy: "BaseCacheStrategy" | None = None,
            http_cache: bool = True,
            throttler: "BaseThrottler" | None = None,
            auto_retry: bool | RetryDecisionFunc = True,
            rest_api_validate_body: bool = True,
        ): ...

        # other auth strategies without config
        @overload
        def __init__(
            self: "GitHub[AS]",
            auth: AS,
            *,
            base_url: str | httpx.URL | None = None,
            accept_format: str | None = None,
            previews: Sequence[str] | None = None,
            user_agent: str | None = None,
            follow_redirects: bool = True,
            timeout: float | httpx.Timeout | None = None,
            ssl_verify: bool | "ssl.SSLContext" = ...,
            trust_env: bool = True,
            proxy: ProxyTypes | None = None,
            transport: httpx.BaseTransport | None = None,
            async_transport: httpx.AsyncBaseTransport | None = None,
            event_hooks: EventHookTypes | None = None,
            async_event_hooks: EventHookTypes | None = None,
            cache_strategy: "BaseCacheStrategy" | None = None,
            http_cache: bool = True,
            throttler: "BaseThrottler" | None = None,
            auto_retry: bool | RetryDecisionFunc = True,
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
        self, query: str, variables: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        return await self.graphql.arequest(query, variables)

    # rest pagination
    paginate = Paginator
