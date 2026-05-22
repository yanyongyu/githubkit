from collections.abc import Sequence
from dataclasses import dataclass, fields
from typing import TYPE_CHECKING, Any
from typing_extensions import Self

import httpx

from .cache import DEFAULT_CACHE_STRATEGY, BaseCacheStrategy
from .retry import RETRY_DEFAULT
from .throttling import BaseThrottler, LocalThrottler
from .typing import EventHookTypes, ProxyTypes, RetryDecisionFunc

if TYPE_CHECKING:
    import ssl


@dataclass(frozen=True)
class Config:
    base_url: httpx.URL
    accept: str
    user_agent: str
    follow_redirects: bool
    timeout: httpx.Timeout
    ssl_verify: "bool | ssl.SSLContext"
    trust_env: bool  # effects the `httpx` proxy and ssl cert
    proxy: ProxyTypes | None
    transport: httpx.BaseTransport | None
    async_transport: httpx.AsyncBaseTransport | None
    event_hooks: EventHookTypes | None
    async_event_hooks: EventHookTypes | None
    cache_strategy: BaseCacheStrategy
    http_cache: bool
    throttler: BaseThrottler
    auto_retry: RetryDecisionFunc | None
    rest_api_validate_body: bool

    def dict(self) -> dict[str, Any]:
        """Return the config as a dictionary without copy values."""
        return {field.name: getattr(self, field.name) for field in fields(self)}

    def copy(self) -> Self:
        """Return a shallow copy of the config."""
        return self.__class__(**self.dict())


def build_base_url(base_url: str | httpx.URL | None) -> httpx.URL:
    base_url = base_url or httpx.URL("https://api.github.com/")
    base_url = base_url if isinstance(base_url, httpx.URL) else httpx.URL(base_url)
    # enforce trailing slash
    if not base_url.raw_path.endswith(b"/"):
        base_url = base_url.copy_with(raw_path=base_url.raw_path + b"/")
    return base_url


def build_accept(
    accept_format: str | None = None, previews: Sequence[str] | None = None
) -> str:
    if accept_format:
        accept_format = (
            accept_format if accept_format.startswith(".") else f".{accept_format}"
        )
    accept_format = accept_format or "+json"

    if previews:
        accepts = [
            f"application/vnd.github.{preview}-preview{accept_format}"
            for preview in previews
        ]
    else:
        accepts = [f"application/vnd.github{accept_format}"]
    return ",".join(accepts)


def build_user_agent(user_agent: str | None = None) -> str:
    return user_agent or "GitHubKit/Python"


def build_timeout(
    timeout: float | httpx.Timeout | None = None,
) -> httpx.Timeout:
    return timeout if isinstance(timeout, httpx.Timeout) else httpx.Timeout(timeout)


def build_cache_strategy(
    cache_strategy: BaseCacheStrategy | None,
) -> BaseCacheStrategy:
    return cache_strategy or DEFAULT_CACHE_STRATEGY


def build_throttler(
    throttler: BaseThrottler | None,
) -> BaseThrottler:
    # https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits
    # > No more than 100 concurrent requests are allowed
    return throttler or LocalThrottler(100)


def build_auto_retry(
    auto_retry: bool | RetryDecisionFunc = True,
) -> RetryDecisionFunc | None:
    if auto_retry is True:
        return RETRY_DEFAULT
    elif auto_retry:
        return auto_retry
    else:
        return None


def get_config(
    *,
    base_url: str | httpx.URL | None = None,
    accept_format: str | None = None,
    previews: Sequence[str] | None = None,
    user_agent: str | None = None,
    follow_redirects: bool = True,
    timeout: float | httpx.Timeout | None = None,
    ssl_verify: "bool | ssl.SSLContext" = True,
    trust_env: bool = True,
    proxy: ProxyTypes | None = None,
    transport: httpx.BaseTransport | None = None,
    async_transport: httpx.AsyncBaseTransport | None = None,
    event_hooks: EventHookTypes | None = None,
    async_event_hooks: EventHookTypes | None = None,
    cache_strategy: BaseCacheStrategy | None = None,
    http_cache: bool = True,
    throttler: BaseThrottler | None = None,
    auto_retry: bool | RetryDecisionFunc = True,
    rest_api_validate_body: bool = True,
) -> Config:
    """Build the configs from the given options."""
    return Config(
        build_base_url(base_url),
        build_accept(accept_format, previews),
        build_user_agent(user_agent),
        follow_redirects,
        build_timeout(timeout),
        ssl_verify,
        trust_env,
        proxy,
        transport,
        async_transport,
        event_hooks,
        async_event_hooks,
        build_cache_strategy(cache_strategy),
        http_cache,
        build_throttler(throttler),
        build_auto_retry(auto_retry),
        rest_api_validate_body,
    )
