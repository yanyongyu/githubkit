from collections.abc import Awaitable
from functools import cached_property
from typing_extensions import ParamSpec
from typing import TYPE_CHECKING, Any, Union, TypeVar, Callable, Optional, overload

from .core import GitHubCore
from .response import Response
from .paginator import Paginator
from .auth import BaseAuthStrategy
from .graphql import GraphQLNamespace
from .typing import RetryDecisionFunc
from .versions import RestVersionSwitcher, WebhooksVersionSwitcher

if TYPE_CHECKING:
    import httpx

    from .config import Config
    from .cache import BaseCacheStrategy
    from .throttling import BaseThrottler
    from .auth import TokenAuthStrategy, UnauthAuthStrategy


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
            previews: Optional[list[str]] = None,
            user_agent: Optional[str] = None,
            follow_redirects: bool = True,
            timeout: Optional[Union[float, httpx.Timeout]] = None,
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
            previews: Optional[list[str]] = None,
            user_agent: Optional[str] = None,
            follow_redirects: bool = True,
            timeout: Optional[Union[float, httpx.Timeout]] = None,
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
            previews: Optional[list[str]] = None,
            user_agent: Optional[str] = None,
            follow_redirects: bool = True,
            timeout: Optional[Union[float, httpx.Timeout]] = None,
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
