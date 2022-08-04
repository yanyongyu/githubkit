import abc
from datetime import datetime, timezone, timedelta
from typing import TYPE_CHECKING, Optional, Generator

import httpx

try:
    import jwt
except ImportError:
    jwt = None

if TYPE_CHECKING:
    from .core import GitHubCore

# auth types
# BasicAuth = httpx.BasicAuth
class _TokenAuth(httpx.Auth):
    """Token Authentication"""

    def __init__(self, token: str):
        self.token = token

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers["Authorization"] = f"token {self.token}"
        yield request


class _JWTAuth(httpx.Auth):
    """JWT Authentication"""

    def __init__(self, jwt: str):
        self.jwt = jwt

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers["Authorization"] = f"Bearer {self.jwt}"
        yield request


# auth strategies
class BaseAuthStrategy(abc.ABC):
    @abc.abstractmethod
    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        raise NotImplementedError


class NoneAuthStrategy(BaseAuthStrategy):
    """Unauthenticated githubkit"""

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return httpx.Auth()


class TokenAuthStrategy(BaseAuthStrategy):
    """Authenticating with token.

    - person access token (PAT): ghp_xxxxxxxxxx
    - oauth token: gho_xxxxxxxxxx
    - github app installation token: ghs_xxxxxxxxxx
    - github app user-to-server token: ghu_xxxxxxxxxx
    """

    def __init__(self, token: str):
        self.token = token

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return _TokenAuth(self.token)


class OAuthAppAuthStrategy(BaseAuthStrategy):
    """Authenticating as OAuth APP"""

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return httpx.BasicAuth(self.client_id, self.client_secret)


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

        self._expire_time: datetime
        self._jwt: Optional[str] = None

    def _create_jwt(self) -> str:
        """Create a JWT authenticating as GitHub APP.

        See https://docs.github.com/en/developers/apps/building-github-apps/authenticating-with-github-apps#authenticating-as-a-github-app
        """
        assert jwt
        time = datetime.now(timezone.utc) - timedelta(minutes=1)
        expire_time = time + timedelta(minutes=10)

        # ensure expire before request
        self._expire_time = expire_time - timedelta(minutes=1)
        self._jwt = jwt.encode(
            {"iss": self.app_id, "iat": time, "exp": expire_time},
            self.private_key,
            algorithm="RS256",
        )
        return self._jwt

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        if not (token := self._jwt) or datetime.now(timezone.utc) > self._expire_time:
            token = self._create_jwt()
        return _JWTAuth(token)
