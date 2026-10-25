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
    """Build a request used inside auth flow, keeping the client timeout.

    httpx only sets the timeout extension on the request passed to `send`,
    not on requests yielded by an auth flow, so copy it from the original
    request, or fall back to the client config.
    """
    timeout = (
        request.extensions.get("timeout") if request is not None else None
    ) or github.config.timeout.as_dict()
    return httpx.Request(method, url, extensions={"timeout": timeout}, **kwargs)
