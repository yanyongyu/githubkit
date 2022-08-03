import abc
from typing import TYPE_CHECKING, Generator
from datetime import datetime, timezone, timedelta

import httpx

try:
    import jwt
except ImportError:
    jwt = None

if TYPE_CHECKING:
    from .core import GitHubCore


class BaseAuthStrategy(abc.ABC):
    @abc.abstractmethod
    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        raise NotImplementedError


class NoneAuthStrategy(BaseAuthStrategy):
    """Unauthenticated githubkit"""

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return httpx.Auth()


class BasicAuthStrategy(BaseAuthStrategy):
    """Authenticating as OAuth APP or User with PAT"""

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
    """Authenticating as user with oauth token"""

    def __init__(self, token: str):
        self.token = token

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return _TokenAuth(self.token)


class _AppAuth(httpx.Auth):
    def __init__(self, app_id: str, private_key: str):
        self.app_id = app_id
        self.private_key = private_key

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        # See https://docs.github.com/en/developers/apps/building-github-apps/authenticating-with-github-apps#authenticating-as-a-github-app
        assert jwt
        time = datetime.now(timezone.utc) - timedelta(minutes=1)
        expire_time = time + timedelta(minutes=10)
        token = jwt.encode(
            {"iss": self.app_id, "iat": time, "exp": expire_time},
            self.private_key,
            algorithm="RS256",
        )
        request.headers["Authorization"] = f"Bearer {token}"
        yield request


class AppAuthStrategy(BaseAuthStrategy):
    """Authenticating as GitHub APP"""

    def __init__(self, app_id: str, private_key: str):
        if jwt is None:
            raise RuntimeError(
                "JWT support for GitHub APP should be installed "
                "with `pip install githubkit[app]`"
            )
        self.app_id = app_id
        self.private_key = private_key

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return _AppAuth(self.app_id, self.private_key)
