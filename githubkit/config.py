from collections.abc import Sequence
from dataclasses import dataclass, fields
from typing import TYPE_CHECKING, Any, Optional, Union
from typing_extensions import Self

import httpx

from .cache import DEFAULT_CACHE_STRATEGY, BaseCacheStrategy
from .retry import RETRY_DEFAULT
from .throttling import BaseThrottler, LocalThrottler
from .typing import RetryDecisionFunc

if TYPE_CHECKING:
    import ssl


@dataclass(frozen=True)
class Config:
    base_url: httpx.URL
    accept: str
    user_agent: str
    follow_redirects: bool
    timeout: httpx.Timeout
    ssl_verify: Union[bool, "ssl.SSLContext"]
    cache_strategy: BaseCacheStrategy
    http_cache: bool
    throttler: BaseThrottler
    auto_retry: Optional[RetryDecisionFunc]
    rest_api_validate_body: bool

    def dict(self) -> dict[str, Any]:
        """Return the config as a dictionary without copy values."""
        return {field.name: getattr(self, field.name) for field in fields(self)}

    def copy(self) -> Self:
        """Return a shallow copy of the config."""
        return self.__class__(**self.dict())


def build_base_url(base_url: Optional[Union[str, httpx.URL]]) -> httpx.URL:
    base_url = base_url or httpx.URL("https://api.github.com/")
    base_url = base_url if isinstance(base_url, httpx.URL) else httpx.URL(base_url)
    # enforce trailing slash
    if not base_url.raw_path.endswith(b"/"):
        base_url = base_url.copy_with(raw_path=base_url.raw_path + b"/")
    return base_url


def build_accept(
    accept_format: Optional[str] = None, previews: Optional[Sequence[str]] = None
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


def build_user_agent(user_agent: Optional[str] = None) -> str:
    return user_agent or "GitHubKit/Python"


def build_timeout(
    timeout: Optional[Union[float, httpx.Timeout]] = None,
) -> httpx.Timeout:
    return timeout if isinstance(timeout, httpx.Timeout) else httpx.Timeout(timeout)


def build_cache_strategy(
    cache_strategy: Optional[BaseCacheStrategy],
) -> BaseCacheStrategy:
    return cache_strategy or DEFAULT_CACHE_STRATEGY


def build_throttler(
    throttler: Optional[BaseThrottler],
) -> BaseThrottler:
    # https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits
    # > No more than 100 concurrent requests are allowed
    return throttler or LocalThrottler(100)


def build_auto_retry(
    auto_retry: Union[bool, RetryDecisionFunc] = True,
) -> Optional[RetryDecisionFunc]:
    if auto_retry is True:
        return RETRY_DEFAULT
    elif auto_retry:
        return auto_retry
    else:
        return None


def get_config(
    *,
    base_url: Optional[Union[str, httpx.URL]] = None,
    accept_format: Optional[str] = None,
    previews: Optional[Sequence[str]] = None,
    user_agent: Optional[str] = None,
    follow_redirects: bool = True,
    timeout: Optional[Union[float, httpx.Timeout]] = None,
    ssl_verify: Union[bool, "ssl.SSLContext"] = True,
    cache_strategy: Optional[BaseCacheStrategy] = None,
    http_cache: bool = True,
    throttler: Optional[BaseThrottler] = None,
    auto_retry: Union[bool, RetryDecisionFunc] = True,
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
        build_cache_strategy(cache_strategy),
        http_cache,
        build_throttler(throttler),
        build_auto_retry(auto_retry),
        rest_api_validate_body,
    )
