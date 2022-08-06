from typing import Generator

import httpx

from .base import BaseAuthStrategy


class TokenAuthStrategy(BaseAuthStrategy):
    """Personal Access Token Authentication"""

    __slots__ = ("token",)

    def __init__(self, token: str):
        self.token = token

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers["Authorization"] = f"token {self.token}"
        yield request
