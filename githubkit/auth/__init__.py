"""Authentication Strategies

See also: https://github.com/octokit/authentication-strategies.js
"""

import abc
from datetime import datetime, timezone, timedelta
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Union,
    Optional,
    Generator,
    AsyncGenerator,
    cast,
)

import httpx

from githubkit.utils import UNSET, Unset
from githubkit.oauth import (
    refresh_token,
    async_refresh_token,
    exchange_web_flow_code,
    async_exchange_web_flow_code,
)

try:
    import jwt
except ImportError:
    jwt = None

if TYPE_CHECKING:
    from githubkit import GitHub
    from githubkit.rest.types import AppPermissionsType


# auth hooks
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


class _OAuthWebAuth(httpx.Auth):
    """OAuth Web Authentication"""

    def __init__(
        self,
        github: "GitHub",
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: Optional[str] = None,
    ):
        self.github = github
        self.client_id = client_id
        self.client_secret = client_secret
        self.code = code
        self.redirect_uri = redirect_uri

        self._token: Optional[str] = None

        self._expire_time: Optional[datetime] = None
        self._refresh_token: Optional[str] = None

    def _parse_response_data(self, data: Dict[str, Any]) -> str:
        self._token = data["access_token"]
        if "refresh_token" in data:
            self._refresh_token = data["refresh_token"]
            self._expire_time = datetime.now(timezone.utc) + timedelta(
                minutes=-1, seconds=int(data["expires_in"])
            )
        return self._token

    def sync_auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        if not (token := self._token):
            token = self._parse_response_data(
                exchange_web_flow_code(
                    self.github,
                    self.client_id,
                    self.client_secret,
                    self.code,
                    self.redirect_uri,
                )
            )
        elif self._expire_time and datetime.now(timezone.utc) > self._expire_time:
            token = self._parse_response_data(
                refresh_token(
                    self.github,
                    self.client_id,
                    self.client_secret,
                    cast(str, self._refresh_token),
                )
            )
        request.headers["Authorization"] = f"token {token}"
        yield request

    async def async_auth_flow(
        self, request: httpx.Request
    ) -> AsyncGenerator[httpx.Request, httpx.Response]:
        if not (token := self._token):
            token = self._parse_response_data(
                await async_exchange_web_flow_code(
                    self.github,
                    self.client_id,
                    self.client_secret,
                    self.code,
                    self.redirect_uri,
                )
            )
        elif self._expire_time and datetime.now(timezone.utc) > self._expire_time:
            token = self._parse_response_data(
                await async_refresh_token(
                    self.github,
                    self.client_id,
                    self.client_secret,
                    cast(str, self._refresh_token),
                )
            )
        request.headers["Authorization"] = f"token {token}"
        yield request


# class _OAuthDeviceAuth(httpx.Auth):
#     """OAuth Device Authentication"""

#     def __init__(
#         self,
#         github: "GitHub",
#         client_id: str,
#         on_verifications: Callable[[Dict[str, Any]], Any],
#         scopes: Optional[List[str]] = None,
#     ):
#         self.github = github
#         self.client_id = client_id
#         self.on_verifications = on_verifications
#         self.scopes = scopes


class _AppInstallationAuth(httpx.Auth):
    """GitHub APP Installation Authentication"""

    def __init__(
        self,
        github: "GitHub",
        app_id: str,
        private_key: str,
        installation_id: int,
        repositories: List[str],
        repository_ids: List[int],
        permissions: Union[Unset, "AppPermissionsType"] = UNSET,
    ):
        self.github = github
        self.app_id = app_id
        self.private_key = private_key
        self.installation_id = installation_id
        self.repositories = repositories
        self.repository_ids = repository_ids
        self.permissions = permissions

    def sync_auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        resp = self.github.rest.apps.create_installation_access_token(
            self.installation_id,
            repositories=self.repositories,
            repository_ids=self.repository_ids,
            permissions=self.permissions,
        )

        yield request


class _AppAuth(httpx.Auth):
    """GitHub APP JWT Authentication"""

    def __init__(self, app_id: str, private_key: str):
        assert jwt
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

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        if not (token := self._jwt) or datetime.now(timezone.utc) > self._expire_time:
            token = self._create_jwt()
        request.headers["Authorization"] = f"Bearer {token}"
        yield request


# auth strategies
class BaseAuthStrategy(abc.ABC):
    @abc.abstractmethod
    def get_auth_flow(self, github: "GitHub") -> httpx.Auth:
        raise NotImplementedError


class NoneAuthStrategy(BaseAuthStrategy):
    """Unauthenticated githubkit"""

    def get_auth_flow(self, github: "GitHub") -> httpx.Auth:
        return httpx.Auth()


class TokenAuthStrategy(BaseAuthStrategy):
    """Authenticating with token.

    - person access token (PAT): ghp_xxxxxxxxxx
    - oauth token: gho_xxxxxxxxxx
    - github app installation token: ghs_xxxxxxxxxx
    - github app user-to-server token: ghu_xxxxxxxxxx
    """

    def __init__(self, token: str):
        self.flow = _TokenAuth(token)

    def get_auth_flow(self, github: "GitHub") -> httpx.Auth:
        return self.flow


class OAuthWebAuthStrategy(BaseAuthStrategy):
    """Authenticating with oauth web flow code."""

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: Optional[str] = None,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.code = code
        self.redirect_uri = redirect_uri

        self.flow: Optional["_OAuthWebAuth"] = None

    def get_auth_flow(self, github: "GitHub") -> httpx.Auth:
        if not self.flow:
            self.flow = _OAuthWebAuth(
                github, self.client_id, self.client_secret, self.code, self.redirect_uri
            )
        else:
            self.flow.github = github
        return self.flow


class OAuthAppAuthStrategy(BaseAuthStrategy):
    """Authenticating as OAuth APP"""

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.flow = httpx.BasicAuth(self.client_id, self.client_secret)

    def as_user(
        self, code: str, redirect_uri: Optional[str] = None
    ) -> OAuthWebAuthStrategy:
        """Authenticating as user with oauth web flow code."""
        return OAuthWebAuthStrategy(
            self.client_id, self.client_secret, code, redirect_uri
        )

    def get_auth_flow(self, github: "GitHub") -> httpx.Auth:
        return self.flow


class InstallationAuthStrategy(BaseAuthStrategy):
    """Authenticating as GitHub APP Installation"""

    def __init__(self, app_id: str, private_key: str, installation_id: int):
        self.app_id = app_id
        self.private_key = private_key
        self.installation_id = installation_id

        self.flow: Optional[_AppAuth] = None

    def get_auth_flow(self, github: "GitHub") -> httpx.Auth:
        ...


class AppAuthStrategy(BaseAuthStrategy):
    """Authenticating as GitHub APP"""

    def __init__(self, app_id: str, private_key: str):
        if jwt is None:
            raise RuntimeError(
                "JWT support for GitHub APP should be installed "
                "with `pip install githubkit[auth-app]`"
            )

        self.app_id = app_id
        self.private_key = private_key
        self.flow = _AppAuth(app_id, private_key)

    def get_auth_flow(self, github: "GitHub") -> httpx.Auth:
        return self.flow
