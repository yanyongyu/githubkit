from typing import Optional, Generator
from datetime import datetime, timezone, timedelta

import httpx

from githubkit.cache import DEFAULT_CACHE, BaseCache

from .base import BaseAuthStrategy
from ._url import require_bypass, require_app_auth

try:
    import jwt
except ImportError:
    jwt = None


class AppAuthStrategy(BaseAuthStrategy):
    """GitHub App or Installation Authentication"""

    __slots__ = (
        "app_id",
        "private_key",
        "client_id",
        "client_secret",
        "installation_id",
    )

    def __init__(
        self,
        app_id: str,
        private_key: str,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        installation_id: Optional[int] = None,
        cache: Optional["BaseCache"] = None,
    ):
        self.app_id = app_id
        self.private_key = private_key
        self.client_id = client_id
        self.client_secret = client_secret
        self.installation_id = installation_id
        self.cache = cache or DEFAULT_CACHE

    def _cache_token(self, token: str, expire_time: datetime):
        ...

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

        # ensure expire before request
        token = jwt.encode(
            {"iss": self.app_id, "iat": time, "exp": expire_time},
            self.private_key,
            algorithm="RS256",
        )
        self._cache_token(token, expire_time - timedelta(minutes=1))
        return token

    def sync_auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        if require_bypass(request.url):
            yield request
            return
        if require_app_auth(request.url):
            request.headers["Authorization"] = f"Bearer {self._create_jwt()}"
            yield request
            return
        yield request
