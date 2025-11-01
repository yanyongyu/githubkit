from typing import Callable

import httpx

from githubkit import GitHub, UnauthAuthStrategy


def get_mock_github(
    handle: Callable[[httpx.Request], httpx.Response],
) -> GitHub[UnauthAuthStrategy]:
    transport = httpx.MockTransport(handle)
    return GitHub(transport=transport, async_transport=transport)
