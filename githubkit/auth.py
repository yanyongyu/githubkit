import abc
from typing import TYPE_CHECKING, Any, Dict, Generator

import httpx

if TYPE_CHECKING:
    from .core import GitHubCore


class BaseAuthStrategy(abc.ABC):
    @abc.abstractmethod
    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        raise NotImplementedError()


class BasicAuthStrategy(BaseAuthStrategy):
    def __init__(self, username: str, token: str):
        self.username = username
        self.token = token

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return httpx.BasicAuth(self.username, self.token)


class _TokenAuth(httpx.Auth):
    def __init__(self, token: str):
        self.token = token

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers["Authorization"] = f"token {self.token}"
        yield request


class TokenAuthStrategy(BaseAuthStrategy):
    def __init__(self, token: str):
        self.token = token

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return _TokenAuth(self.token)
