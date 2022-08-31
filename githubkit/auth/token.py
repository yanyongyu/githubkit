from dataclasses import dataclass
from typing import TYPE_CHECKING, Generator

import httpx

from .base import BaseAuthStrategy

if TYPE_CHECKING:
    from githubkit import GitHubCore


@dataclass(slots=True)
class TokenAuth(httpx.Auth):
    """Personal Access Token Authentication Hook"""

    token: str

    def __init__(self, token: str):
        self.token = token

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers["Authorization"] = f"token {self.token}"
        yield request


@dataclass(slots=True)
class TokenAuthStrategy(BaseAuthStrategy):
    """Personal Access Token Authentication"""

    token: str

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return TokenAuth(self.token)
