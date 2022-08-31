from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from typing import TYPE_CHECKING, List, Union, Optional, Generator, AsyncGenerator

import httpx

from githubkit.exception import AuthCredentialError
from githubkit.cache import DEFAULT_CACHE, BaseCache
from githubkit.utils import UNSET, Unset, exclude_unset
from githubkit.rest import (
    BasicError,
    ValidationError,
    InstallationToken,
    AppInstallationsInstallationIdAccessTokensPostBody,
)

from .base import BaseAuthStrategy
from .oauth import OAuthAppAuthStrategy
from ._url import require_bypass, require_app_auth, require_basic_auth

try:
    import jwt
except ImportError:
    jwt = None

if TYPE_CHECKING:
    from githubkit import Response, GitHubCore
    from githubkit.rest.types import AppPermissionsType


@dataclass(slots=True)
class AppAuth(httpx.Auth):
    """GitHub App or Installation Authentication Hook"""

    github: "GitHubCore"
    app_id: str
    private_key: str
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    installation_id: Union[Unset, int] = UNSET
    repositories: Union[Unset, List[str]] = UNSET
    repository_ids: Union[Unset, List[int]] = UNSET
    permissions: Union[Unset, "AppPermissionsType"] = UNSET
    cache: "BaseCache" = DEFAULT_CACHE

    JWT_CACHE_KEY = "githubkit:auth:app:jwt"
    INSTALLATION_CACHE_KEY = "githubkit:auth:app:installation:{installation_id}:{permissions}:{repositories}:{repository_ids}"

    def _create_jwt(self) -> str:
        """Create a JWT authenticating as GitHub APP.

        See https://docs.github.com/en/developers/apps/building-github-apps/authenticating-with-github-apps#authenticating-as-a-github-app
        """
        if jwt is None:
            raise RuntimeError(
                "JWT support for GitHub APP should be installed "
                "with `pip install githubkit[auth-app]`"
            )
        time = datetime.now(timezone.utc) - timedelta(minutes=1)
        expire_time = time + timedelta(minutes=10)
        return jwt.encode(
            {"iss": self.app_id, "iat": time, "exp": expire_time},
            self.private_key,
            algorithm="RS256",
        )

    def get_jwt(self) -> str:
        if not (token := self.cache.get(self.JWT_CACHE_KEY)):
            token = self._create_jwt()
            self.cache.set(self.JWT_CACHE_KEY, token, timedelta(minutes=8))
        return token

    async def aget_jwt(self) -> str:
        if not (token := await self.cache.aget(self.JWT_CACHE_KEY)):
            token = self._create_jwt()
            await self.cache.aset(self.JWT_CACHE_KEY, token, timedelta(minutes=8))
        return token

    def _build_installation_auth_request(self) -> httpx.Request:
        if self.installation_id is UNSET:
            raise AuthCredentialError(
                "GitHub APP installation_id must be provided "
                "for accessing apis as an installation"
            )

        base_url = self.github.config.base_url
        url = base_url.copy_with(
            raw_path=base_url.raw_path
            + f"app/installations/{self.installation_id}/access_tokens".encode("ascii")
        )
        body = AppInstallationsInstallationIdAccessTokensPostBody.parse_obj(
            {
                "repositories": self.repositories,
                "repository_ids": self.repository_ids,
                "permissions": self.permissions,
            }
        ).dict(by_alias=True)
        return httpx.Request(
            "POST",
            url,
            json=exclude_unset(body),
            headers={
                "User-Agent": self.github.config.user_agent,
                "Accept": self.github.config.accept,
            },
        )

    def _parse_installation_auth_response(
        self, response: httpx.Response
    ) -> "Response[InstallationToken]":
        return self.github._check(
            response,
            response_model=InstallationToken,
            error_models={
                "403": BasicError,
                "401": BasicError,
                "404": BasicError,
                "422": ValidationError,
            },
        )

    def _get_installation_cache_key(self) -> str:
        if self.installation_id is UNSET:
            raise AuthCredentialError(
                "GitHub APP installation_id must be provided "
                "for accessing apis as an installation"
            )

        permissions = {} if isinstance(self.permissions, Unset) else self.permissions
        repositories = [] if isinstance(self.repositories, Unset) else self.repositories
        repository_ids = (
            [] if isinstance(self.repository_ids, Unset) else self.repository_ids
        )
        return self.INSTALLATION_CACHE_KEY.format(
            installation_id=self.installation_id,
            permissions=",".join(
                name if value == "read" else f"{name}!"
                for name, value in permissions.items()
            ),
            repositories=",".join(repositories),
            repository_ids=",".join(str(id) for id in repository_ids),
        )

    def sync_auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        if require_bypass(request.url):
            yield request
            return
        if require_app_auth(request.url):
            request.headers["Authorization"] = f"Bearer {self.get_jwt()}"
            yield request
            return
        if require_basic_auth(request.url):
            if not self.client_id or not self.client_secret:
                raise AuthCredentialError(
                    "GitHub APP's client_id and client_secret must "
                    "be provided for application apis"
                )
            yield from httpx.BasicAuth(
                self.client_id, self.client_secret
            ).sync_auth_flow(request)
            return

        key = self._get_installation_cache_key()
        if not (token := self.cache.get(key)):
            token_request = self._build_installation_auth_request()
            token_request.headers["Authorization"] = f"Bearer {self.get_jwt()}"
            response = yield token_request
            response.read()
            response = self._parse_installation_auth_response(response)
            token = response.parsed_data.token
            expire = datetime.strptime(
                response.parsed_data.expires_at, "%Y-%m-%dT%H:%M:%SZ"
            ).replace(tzinfo=timezone.utc) - datetime.now(timezone.utc)
            self.cache.set(key, token, expire)
        request.headers["Authorization"] = f"token {token}"
        yield request

    async def async_auth_flow(
        self, request: httpx.Request
    ) -> AsyncGenerator[httpx.Request, httpx.Response]:
        if require_bypass(request.url):
            yield request
            return
        if require_app_auth(request.url):
            request.headers["Authorization"] = f"Bearer {await self.aget_jwt()}"
            yield request
            return
        if require_basic_auth(request.url):
            if not self.client_id or not self.client_secret:
                raise AuthCredentialError(
                    "GitHub APP's client_id and client_secret must "
                    "be provided for application apis"
                )
            async for request in httpx.BasicAuth(
                self.client_id, self.client_secret
            ).async_auth_flow(request):
                yield request
            return

        key = self._get_installation_cache_key()
        if not (token := await self.cache.aget(key)):
            token_request = self._build_installation_auth_request()
            token_request.headers["Authorization"] = f"Bearer {await self.aget_jwt()}"
            response = yield token_request
            await response.aread()
            response = self._parse_installation_auth_response(response)
            token = response.parsed_data.token
            expire = datetime.strptime(
                response.parsed_data.expires_at, "%Y-%m-%dT%H:%M:%SZ"
            ) - datetime.now(timezone.utc)
            await self.cache.aset(key, token, expire)
        request.headers["Authorization"] = f"token {token}"
        yield request


@dataclass(slots=True)
class AppAuthStrategy(BaseAuthStrategy):
    """GitHub App Authentication"""

    app_id: str
    private_key: str
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    cache: "BaseCache" = DEFAULT_CACHE

    def as_installation(
        self,
        installation_id: int,
        repositories: Union[Unset, List[str]] = UNSET,
        repository_ids: Union[Unset, List[int]] = UNSET,
        permissions: Union[Unset, "AppPermissionsType"] = UNSET,
    ) -> "AppInstallationAuthStrategy":
        return AppInstallationAuthStrategy(
            self.app_id,
            self.private_key,
            installation_id,
            self.client_id,
            self.client_secret,
            repositories,
            repository_ids,
            permissions,
            self.cache,
        )

    def as_oauth_app(self) -> OAuthAppAuthStrategy:
        if not self.client_id or not self.client_secret:
            raise AuthCredentialError(
                "GitHub APP's client_id and client_secret must be provided"
            )
        return OAuthAppAuthStrategy(self.client_id, self.client_secret)

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return AppAuth(
            github,
            self.app_id,
            self.private_key,
            self.client_id,
            self.client_secret,
            cache=self.cache,
        )


@dataclass(slots=True)
class AppInstallationAuthStrategy(BaseAuthStrategy):
    """GitHub App Installation Authentication"""

    app_id: str
    private_key: str
    installation_id: int
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    repositories: Union[Unset, List[str]] = UNSET
    repository_ids: Union[Unset, List[int]] = UNSET
    permissions: Union[Unset, "AppPermissionsType"] = UNSET
    cache: "BaseCache" = DEFAULT_CACHE

    def as_app(self) -> AppAuthStrategy:
        return AppAuthStrategy(
            self.app_id,
            self.private_key,
            self.client_id,
            self.client_secret,
            self.cache,
        )

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return AppAuth(
            github,
            self.app_id,
            self.private_key,
            self.client_id,
            self.client_secret,
            self.installation_id,
            self.repositories,
            self.repository_ids,
            self.permissions,
            cache=self.cache,
        )
