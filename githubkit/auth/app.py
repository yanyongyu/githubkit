from collections.abc import AsyncGenerator, Generator, Sequence
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import TYPE_CHECKING, ClassVar, Optional, Union
from typing_extensions import LiteralString

import httpx

from githubkit.compat import model_dump, type_validate_python
from githubkit.exception import AuthCredentialError
from githubkit.utils import UNSET, Unset, exclude_unset

from ._url import require_app_auth, require_basic_auth, require_bypass
from .base import BaseAuthStrategy
from .oauth import OAuthAppAuthStrategy

try:
    import jwt
except ImportError:
    jwt = None

if TYPE_CHECKING:
    from githubkit import GitHubCore, Response
    from githubkit.versions.latest.models import InstallationToken
    from githubkit.versions.latest.types import AppPermissionsType


@dataclass
class AppAuth(httpx.Auth):
    """GitHub App or Installation Authentication Hook"""

    github: "GitHubCore"
    app_id: Union[str, int, None]
    private_key: str
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    installation_id: Union[Unset, int] = UNSET
    repositories: Union[Unset, Sequence[str]] = UNSET
    repository_ids: Union[Unset, Sequence[int]] = UNSET
    permissions: Union[Unset, "AppPermissionsType"] = UNSET

    JWT_CACHE_KEY: ClassVar[LiteralString] = "githubkit:auth:app:{issuer}:jwt"
    INSTALLATION_CACHE_KEY: ClassVar[LiteralString] = (
        "githubkit:auth:app:{issuer}:installation:"
        "{installation_id}:{permissions}:{repositories}:{repository_ids}"
    )

    @property
    def issuer(self) -> str:
        # issuer can be either app_id or client_id
        issuer = self.client_id if self.app_id is None else self.app_id
        if issuer is None:
            raise AuthCredentialError(
                "Either app_id or client_id must be provided for GitHub APP"
            )
        return str(issuer)

    def _get_api_route(self, url: httpx.URL) -> httpx.URL:
        """Get the api route (path only) for the given url."""
        base_url_path = self.github.config.base_url.path
        if (path := url.path).startswith(base_url_path):
            path = path[len(base_url_path) :]
            # add leading slash
            if not path.startswith("/"):
                path = "/" + path
        return httpx.URL(path=path)

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
            {"iss": self.issuer, "iat": time, "exp": expire_time},
            self.private_key,
            algorithm="RS256",
        )

    def _get_jwt_cache_key(self) -> str:
        return self.JWT_CACHE_KEY.format(issuer=self.issuer)

    def get_jwt(self) -> str:
        cache = self.github.config.cache_strategy.get_cache_storage()
        cache_key = self._get_jwt_cache_key()
        if not (token := cache.get(cache_key)):
            token = self._create_jwt()
            cache.set(cache_key, token, timedelta(minutes=8))
        return token

    async def aget_jwt(self) -> str:
        cache = self.github.config.cache_strategy.get_async_cache_storage()
        cache_key = self._get_jwt_cache_key()
        if not (token := await cache.aget(cache_key)):
            token = self._create_jwt()
            await cache.aset(cache_key, token, timedelta(minutes=8))
        return token

    def _build_installation_auth_request(self) -> httpx.Request:
        from githubkit.versions.latest.models import (
            AppInstallationsInstallationIdAccessTokensPostBody,
        )

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
        body = model_dump(
            type_validate_python(
                AppInstallationsInstallationIdAccessTokensPostBody,
                {
                    "repositories": self.repositories,
                    "repository_ids": self.repository_ids,
                    "permissions": self.permissions,
                },
            )
        )
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
        from githubkit.versions.latest.models import (
            BasicError,
            InstallationToken,
            ValidationError,
        )

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
            issuer=self.issuer,
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
        if require_app_auth(self._get_api_route(request.url)):
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

        cache = self.github.config.cache_strategy.get_cache_storage()
        key = self._get_installation_cache_key()
        if not (token := cache.get(key)):
            token_request = self._build_installation_auth_request()
            token_request.headers["Authorization"] = f"Bearer {self.get_jwt()}"
            response = yield token_request
            response.read()
            response = self._parse_installation_auth_response(response)
            token = response.parsed_data.token
            expire = datetime.strptime(
                response.parsed_data.expires_at, "%Y-%m-%dT%H:%M:%SZ"
            ).replace(tzinfo=timezone.utc) - datetime.now(timezone.utc)
            cache.set(key, token, expire)
        request.headers["Authorization"] = f"token {token}"
        yield request

    async def async_auth_flow(
        self, request: httpx.Request
    ) -> AsyncGenerator[httpx.Request, httpx.Response]:
        if require_bypass(request.url):
            yield request
            return
        if require_app_auth(self._get_api_route(request.url)):
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

        cache = self.github.config.cache_strategy.get_async_cache_storage()
        key = self._get_installation_cache_key()
        if not (token := await cache.aget(key)):
            token_request = self._build_installation_auth_request()
            token_request.headers["Authorization"] = f"Bearer {await self.aget_jwt()}"
            response = yield token_request
            await response.aread()
            response = self._parse_installation_auth_response(response)
            token = response.parsed_data.token
            expire = datetime.strptime(
                response.parsed_data.expires_at, "%Y-%m-%dT%H:%M:%SZ"
            ).replace(tzinfo=timezone.utc) - datetime.now(timezone.utc)
            await cache.aset(key, token, expire)
        request.headers["Authorization"] = f"token {token}"
        yield request


@dataclass
class AppAuthStrategy(BaseAuthStrategy):
    """GitHub App Authentication"""

    app_id: Union[str, int, None]
    private_key: str
    client_id: Optional[str] = None
    client_secret: Optional[str] = None

    def __post_init__(self):
        # either app_id or client_id must be provided
        if self.app_id is None and self.client_id is None:
            raise AuthCredentialError(
                "Either app_id or client_id must be provided for GitHub APP"
            )

    def as_installation(
        self,
        installation_id: int,
        repositories: Union[Unset, Sequence[str]] = UNSET,
        repository_ids: Union[Unset, Sequence[int]] = UNSET,
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
        )


@dataclass
class AppInstallationAuthStrategy(BaseAuthStrategy):
    """GitHub App Installation Authentication"""

    app_id: Union[str, int, None]
    private_key: str
    installation_id: int
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    repositories: Union[Unset, Sequence[str]] = UNSET
    repository_ids: Union[Unset, Sequence[int]] = UNSET
    permissions: Union[Unset, "AppPermissionsType"] = UNSET

    def __post_init__(self):
        # either app_id or client_id must be provided
        if self.app_id is None and self.client_id is None:
            raise AuthCredentialError(
                "Either app_id or client_id must be provided for GitHub APP"
            )

    def as_app(self) -> AppAuthStrategy:
        return AppAuthStrategy(
            self.app_id,
            self.private_key,
            self.client_id,
            self.client_secret,
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
        )
