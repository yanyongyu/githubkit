import abc
from typing import TYPE_CHECKING, Any

import httpx

if TYPE_CHECKING:
    from githubkit import GitHubCore


class BaseAuthStrategy(abc.ABC):
    @abc.abstractmethod
    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        raise NotImplementedError


def build_request_with_options(
    github: "GitHubCore",
    method: str,
    url: httpx.URL,
    *,
    request: httpx.Request | None = None,
    **kwargs: Any,
) -> httpx.Request:
    """Build a request used inside auth flow, keeping the client options.

    httpx only sets extensions (e.g. timeout) on the request passed to `send`,
    so copy them from the original request, or fall back to client config.
    The `hishel_*` extensions are per-request cache controls and are not copied,
    so they never leak onto the auth requests (e.g. forcing a token to be cached).
    """
    extensions = (
        {
            key: value
            for key, value in request.extensions.items()
            if not key.startswith("hishel_")
        }
        if request is not None
        else {"timeout": github.config.timeout.as_dict()}
    )
    return httpx.Request(method, url, extensions=extensions, **kwargs)
