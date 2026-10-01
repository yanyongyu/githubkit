from collections.abc import Callable

from githubkit import GitHub, UnauthAuthStrategy
from githubkit._httpx import httpx


def get_mock_github(
    handle: Callable[[httpx.Request], httpx.Response],
) -> GitHub[UnauthAuthStrategy]:
    transport = httpx.MockTransport(handle)
    return GitHub(transport=transport, async_transport=transport)
