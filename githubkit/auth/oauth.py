from time import sleep
from dataclasses import field, dataclass
from datetime import datetime, timezone, timedelta
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Union,
    Callable,
    ClassVar,
    Optional,
    Coroutine,
    Generator,
    AsyncGenerator,
    cast,
)

import httpx

from githubkit.utils import is_async
from githubkit.exception import AuthExpiredError

from .base import BaseAuthStrategy
from ._url import require_bypass, get_oauth_base_url, require_basic_auth

try:
    import anyio
    from anyio.to_thread import run_sync
    from anyio.from_thread import threadlocals
    from anyio.from_thread import run as run_async
except ImportError:
    anyio = None
    run_sync = None
    run_async = None
    threadlocals = None

if TYPE_CHECKING:
    from githubkit import GitHubCore


def create_device_code(
    github: "GitHubCore", client_id: str, scopes: Optional[List[str]] = None
) -> Generator[httpx.Request, httpx.Response, Dict[str, Any]]:
    """Create a device code for OAuth."""
    base_url = get_oauth_base_url(github.config.base_url)
    url = base_url.copy_with(raw_path=base_url.raw_path + b"login/device/code")
    body = {"client_id": client_id}
    if scopes:
        body["scopes"] = " ".join(scopes)
    response = yield httpx.Request(
        "POST",
        url,
        json=body,
        headers={
            "User-Agent": github.config.user_agent,
            "Accept": "application/json",
        },
    )
    response = github._check(response)
    return response.json()


def exchange_web_flow_code(
    github: "GitHubCore",
    client_id: str,
    client_secret: str,
    code: str,
    redirect_uri: Optional[str] = None,
) -> Generator[httpx.Request, httpx.Response, Dict[str, Any]]:
    """Exchange web flow code for token."""
    base_url = get_oauth_base_url(github.config.base_url)
    url = base_url.copy_with(raw_path=base_url.raw_path + b"login/oauth/access_token")
    body = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
    }
    if redirect_uri:
        body["redirect_uri"] = redirect_uri
    response = yield httpx.Request(
        "POST",
        url,
        json=body,
        headers={
            "User-Agent": github.config.user_agent,
            "Accept": "application/json",
        },
    )
    response = github._check(response)
    return response.json()


def exchange_device_code(
    github: "GitHubCore", client_id: str, device_code: str
) -> Generator[httpx.Request, httpx.Response, Dict[str, Any]]:
    """Exchange device code for token."""
    base_url = get_oauth_base_url(github.config.base_url)
    url = base_url.copy_with(raw_path=base_url.raw_path + b"login/oauth/access_token")
    response = yield httpx.Request(
        "POST",
        url,
        json={
            "client_id": client_id,
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            "device_code": device_code,
        },
        headers={
            "User-Agent": github.config.user_agent,
            "Accept": "application/json",
        },
    )
    response = github._check(response)
    return response.json()


def refresh_token(
    github: "GitHubCore", client_id: str, client_secret: str, refresh_token: str
) -> Generator[httpx.Request, httpx.Response, Dict[str, Any]]:
    """Refresh token."""
    base_url = get_oauth_base_url(github.config.base_url)
    url = base_url.copy_with(raw_path=base_url.raw_path + b"login/oauth/access_token")
    response = yield httpx.Request(
        "POST",
        url,
        json={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        },
        headers={"Accept": "application/json"},
    )
    response = github._check(response)
    return response.json()


@dataclass(slots=True)
class OAuthWebAuth(httpx.Auth):
    """OAuth Web Flow Hook Authentication"""

    github: "GitHubCore"
    client_id: str
    client_secret: str
    code: str
    redirect_uri: Optional[str] = None

    _token: Optional[str] = field(default=None, init=False, repr=False, compare=False)
    _expire_time: Optional[datetime] = field(
        default=None, init=False, repr=False, compare=False
    )
    _refresh_token: Optional[str] = field(
        default=None, init=False, repr=False, compare=False
    )
    _refresh_token_expire_time: Optional[datetime] = field(
        default=None, init=False, repr=False, compare=False
    )

    requires_response_body: ClassVar[bool] = True

    @property
    def token(self) -> str:
        if not self._token:
            raise RuntimeError("Token not exchanged yet.")
        return self._token

    @property
    def expire_time(self) -> Optional[datetime]:
        return self._expire_time

    def _exchange_code(self) -> httpx.Request:
        base_url = self.github.config.base_url
        url = base_url.copy_with(
            raw_path=f"{base_url.raw_path}login/oauth/access_token"
        )

        body = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": self.code,
        }
        if self.redirect_uri:
            body["redirect_uri"] = self.redirect_uri
        return httpx.Request(
            "POST",
            url,
            json=body,
            headers={
                "User-Agent": self.github.config.user_agent,
                "Accept": "application/json",
            },
        )

    def _parse_response_data(self, data: Dict[str, Any]) -> str:
        self._token = data["access_token"]
        if "refresh_token" in data:
            self._expire_time = datetime.now(timezone.utc) + timedelta(
                minutes=-1, seconds=int(data["expires_in"])
            )
            self._refresh_token = data["refresh_token"]
            self._refresh_token_expire_time = datetime.now(timezone.utc) + timedelta(
                minutes=-1, seconds=int(data["refresh_token_expires_in"])
            )
        return self._token

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        if require_bypass(request.url):
            yield request
            return
        if require_basic_auth(request.url):
            yield from httpx.BasicAuth(self.client_id, self.client_secret).auth_flow(
                request
            )
            return
        if not (token := self._token):
            data = yield from exchange_web_flow_code(
                self.github,
                self.client_id,
                self.client_secret,
                self.code,
                self.redirect_uri,
            )
            token = self._parse_response_data(data)
        elif (
            self._refresh_token_expire_time
            and datetime.now(timezone.utc) > self._refresh_token_expire_time
        ):
            raise AuthExpiredError("Refresh token expired.")
        elif self._expire_time and datetime.now(timezone.utc) > self._expire_time:
            data = yield from refresh_token(
                self.github,
                self.client_id,
                self.client_secret,
                cast(str, self._refresh_token),
            )
            token = self._parse_response_data(data)
        request.headers["Authorization"] = f"token {token}"
        yield request


@dataclass(slots=True)
class OAuthDeviceAuth(httpx.Auth):
    """OAuth Device Flow Hook Authentication"""

    github: "GitHubCore"
    client_id: str
    on_verification: Union[
        Callable[[Dict[str, Any]], None],
        Callable[[Dict[str, Any]], Coroutine[Any, Any, None]],
    ]
    scopes: Optional[List[str]] = None

    _token: Optional[str] = field(default=None, init=False, repr=False, compare=False)
    _expire_time: Optional[datetime] = field(
        default=None, init=False, repr=False, compare=False
    )
    _refresh_token: Optional[str] = field(
        default=None, init=False, repr=False, compare=False
    )
    _refresh_token_expires_time: Optional[datetime] = field(
        default=None, init=False, repr=False, compare=False
    )

    def _parse_response_data(self, data: Dict[str, Any]) -> str:
        self._token = data["access_token"]
        return self._token

    def call_handler(self, data: Dict[str, Any]) -> None:
        if is_async(self.on_verification):
            if anyio is None or threadlocals is None or run_async is None:
                raise RuntimeError(
                    "AnyIO support for OAuth Device Callback should be installed "
                    "with `pip install githubkit[auth-oauth-device]`"
                )
            handler = cast(
                Callable[[Dict[str, Any]], Coroutine[None, None, None]],
                self.on_verification,
            )
            if getattr(threadlocals, "current_async_module", None):
                # in anyio thread worker
                run_async(handler, data)
            else:
                # create and start a new event loop
                anyio.run(handler, data)
        else:
            handler = cast(Callable[[Dict[str, Any]], None], self.on_verification)
            handler(data)

    async def acall_handler(self, data: Dict[str, Any]) -> None:
        if is_async(self.on_verification):
            handler = cast(
                Callable[[Dict[str, Any]], Coroutine[None, None, None]],
                self.on_verification,
            )
            await handler(data)
        else:
            if run_sync is None:
                raise RuntimeError(
                    "AnyIO support for OAuth Device Callback should be installed "
                    "with `pip install githubkit[auth-oauth-device]`"
                )
            handler = cast(Callable[[Dict[str, Any]], None], self.on_verification)
            await run_sync(handler, data)

    def sync_auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        if require_bypass(request.url):
            yield request
            return
        if not (token := self._token):
            flow = create_device_code(self.github, self.client_id, self.scopes)
            create_request = next(flow)
            while True:
                response = yield create_request
                response.read()
                try:
                    create_request = flow.send(response)
                except StopIteration as e:
                    data = e.value
                    break

            device_code = data["device_code"]
            expire_time = datetime.now(timezone.utc) + timedelta(
                seconds=int(data["expires_in"])
            )
            interval = int(data["interval"])
            self.call_handler(data)

            while True:
                if datetime.now(timezone.utc) > expire_time:
                    raise AuthExpiredError("Device code expired.")
                flow = exchange_device_code(self.github, self.client_id, device_code)
                auth_request = next(flow)
                while True:
                    response = yield auth_request
                    response.read()
                    try:
                        auth_request = flow.send(response)
                    except StopIteration as e:
                        data = e.value
                        break
                if "error" in data:
                    sleep(interval)
                    continue
                token = self._parse_response_data(data)
                break
        request.headers["Authorization"] = f"token {token}"
        yield request

    async def async_auth_flow(
        self, request: httpx.Request
    ) -> AsyncGenerator[httpx.Request, httpx.Response]:
        if require_bypass(request.url):
            yield request
            return
        if not (token := self._token):
            flow = create_device_code(self.github, self.client_id, self.scopes)
            create_request = next(flow)
            while True:
                response = yield create_request
                await response.aread()
                try:
                    create_request = flow.send(response)
                except StopIteration as e:
                    data = e.value
                    break

            device_code = data["device_code"]
            expire_time = datetime.now(timezone.utc) + timedelta(
                seconds=int(data["expires_in"])
            )
            interval = int(data["interval"])
            await self.acall_handler(data)

            while True:
                if datetime.now(timezone.utc) > expire_time:
                    raise AuthExpiredError("Device code expired.")
                flow = exchange_device_code(self.github, self.client_id, device_code)
                auth_request = next(flow)
                while True:
                    response = yield auth_request
                    await response.aread()
                    try:
                        auth_request = flow.send(response)
                    except StopIteration as e:
                        data = e.value
                        break
                if "error" in data:
                    await anyio.sleep(interval)
                    continue
                token = self._parse_response_data(data)
                break
        request.headers["Authorization"] = f"token {token}"
        yield request


@dataclass(slots=True)
class OAuthAppAuthStrategy(BaseAuthStrategy):
    """OAuth App Authentication"""

    client_id: str
    client_secret: str

    def as_web_user(
        self, code: str, redirect_uri: Optional[str] = None
    ) -> "OAuthWebAuthStrategy":
        return OAuthWebAuthStrategy(
            self.client_id, self.client_secret, code, redirect_uri
        )

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return httpx.BasicAuth(self.client_id, self.client_secret)


@dataclass(slots=True)
class OAuthWebAuthStrategy(BaseAuthStrategy):
    """OAuth Web Flow Authentication"""

    client_id: str
    client_secret: str
    code: str
    redirect_uri: Optional[str] = None

    def as_oauth_app(self) -> OAuthAppAuthStrategy:
        return OAuthAppAuthStrategy(self.client_id, self.client_secret)

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return OAuthWebAuth(
            github, self.client_id, self.client_secret, self.code, self.redirect_uri
        )


@dataclass(slots=True)
class OAuthDeviceAuthStrategy(BaseAuthStrategy):
    """OAuth Device Flow Authentication"""

    client_id: str
    on_verification: Callable

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return OAuthDeviceAuth(github, self.client_id, self.on_verification)
