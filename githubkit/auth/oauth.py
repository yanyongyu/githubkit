from collections.abc import AsyncGenerator, Coroutine, Generator, Sequence
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from time import sleep
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Optional, TypedDict, cast
from typing_extensions import Self

import httpx

from githubkit.exception import AuthCredentialError, AuthExpiredError
from githubkit.utils import is_async

from ._url import get_oauth_base_url, require_basic_auth, require_bypass
from .base import BaseAuthStrategy

try:
    import anyio
    from anyio.from_thread import run as run_async
    from anyio.from_thread import threadlocals
    from anyio.to_thread import run_sync
except ImportError:
    anyio = None
    run_sync = None
    run_async = None
    threadlocals = None

if TYPE_CHECKING:
    from githubkit import GitHubCore


def create_device_code(
    github: "GitHubCore", client_id: str, scopes: Optional[Sequence[str]] = None
) -> Generator[httpx.Request, httpx.Response, dict[str, Any]]:
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
) -> Generator[httpx.Request, httpx.Response, dict[str, Any]]:
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
) -> Generator[httpx.Request, httpx.Response, dict[str, Any]]:
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
    github: "GitHubCore",
    client_id: str,
    client_secret: Optional[str],  # client secret is optional in device flow
    refresh_token: str,
) -> Generator[httpx.Request, httpx.Response, dict[str, Any]]:
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


class TokenExchangeResult(TypedDict):
    token: str
    expire_time: Optional[datetime]
    refresh_token: Optional[str]
    refresh_token_expire_time: Optional[datetime]


def _parse_token_exchange_response(data: dict[str, Any]) -> TokenExchangeResult:
    if "access_token" not in data:
        raise AuthExpiredError(
            "Refresh access token error! Check your credentials.", data
        )

    token = data["access_token"]
    expire_time = None
    refresh_token = data.get("refresh_token", None)
    refresh_token_expire_time = None
    if refresh_token is not None:
        expire_time = datetime.now(timezone.utc) + timedelta(
            minutes=-1, seconds=int(data["expires_in"])
        )
        refresh_token_expire_time = datetime.now(timezone.utc) + timedelta(
            minutes=-1, seconds=int(data["refresh_token_expires_in"])
        )
    return {
        "token": token,
        "expire_time": expire_time,
        "refresh_token": refresh_token,
        "refresh_token_expire_time": refresh_token_expire_time,
    }


class CreateDeviceCodeResult(TypedDict):
    device_code: str
    expire_time: datetime
    interval: int


def _parse_create_device_code_response(data: dict[str, Any]) -> CreateDeviceCodeResult:
    return {
        "device_code": data["device_code"],
        "expire_time": (
            datetime.now(timezone.utc) + timedelta(seconds=int(data["expires_in"]))
        ),
        "interval": int(data["interval"]),
    }


def _call_handler(handler: Callable, data: dict[str, Any]) -> None:
    if is_async(handler):
        if anyio is None or threadlocals is None or run_async is None:
            raise RuntimeError(
                "AnyIO support for OAuth Device Callback should be installed "
                "with `pip install githubkit[auth-oauth-device]`"
            )
        handler = cast(Callable[[dict[str, Any]], Coroutine[None, None, None]], handler)
        if getattr(threadlocals, "current_async_module", None):
            # in anyio thread worker
            run_async(handler, data)
        else:
            # create and start a new event loop
            anyio.run(handler, data)
    else:
        handler = cast(Callable[[dict[str, Any]], None], handler)
        handler(data)


async def _async_call_handler(handler: Callable, data: dict[str, Any]) -> None:
    if is_async(handler):
        handler = cast(Callable[[dict[str, Any]], Coroutine[None, None, None]], handler)
        await handler(data)
    else:
        if run_sync is None:
            raise RuntimeError(
                "AnyIO support for OAuth Device Callback should be installed "
                "with `pip install githubkit[auth-oauth-device]`"
            )
        handler = cast(Callable[[dict[str, Any]], None], handler)
        await run_sync(handler, data)


@dataclass
class OAuthTokenAuth(httpx.Auth):
    """OAuth Token Authentication"""

    github: "GitHubCore"
    auth_strategy: "OAuthTokenAuthStrategy"

    requires_response_body: ClassVar[bool] = True

    @property
    def client_id(self) -> str:
        return self.auth_strategy.client_id

    @property
    def client_secret(self) -> Optional[str]:
        return self.auth_strategy.client_secret

    @property
    def token(self) -> Optional[str]:
        return self.auth_strategy.token

    @token.setter
    def token(self, value: str) -> None:
        self.auth_strategy.token = value

    @property
    def expire_time(self) -> Optional[datetime]:
        return self.auth_strategy.expire_time

    @expire_time.setter
    def expire_time(self, value: Optional[datetime]) -> None:
        self.auth_strategy.expire_time = value

    @property
    def refresh_token(self) -> Optional[str]:
        return self.auth_strategy.refresh_token

    @refresh_token.setter
    def refresh_token(self, value: Optional[str]) -> None:
        self.auth_strategy.refresh_token = value

    @property
    def refresh_token_expire_time(self) -> Optional[datetime]:
        return self.auth_strategy.refresh_token_expire_time

    @refresh_token_expire_time.setter
    def refresh_token_expire_time(self, value: Optional[datetime]) -> None:
        self.auth_strategy.refresh_token_expire_time = value

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        if require_bypass(request.url):
            yield request
            return

        # check basic auth if is not device flow
        if self.client_secret is not None and require_basic_auth(request.url):
            yield from httpx.BasicAuth(self.client_id, self.client_secret).auth_flow(
                request
            )
            return

        # check refresh token expire
        if (
            self.refresh_token_expire_time
            and datetime.now(timezone.utc) > self.refresh_token_expire_time
        ):
            raise AuthExpiredError("Refresh token expired.")

        # refresh token if token is not provided or expired
        if not (token := self.token) or (
            self.expire_time and datetime.now(timezone.utc) > self.expire_time
        ):
            data = yield from refresh_token(
                self.github,
                self.client_id,
                self.client_secret,
                cast(str, self.refresh_token),
            )
            result = _parse_token_exchange_response(data)
            self.token = token = result["token"]
            self.expire_time = result["expire_time"]
            self.refresh_token = result["refresh_token"]
            self.refresh_token_expire_time = result["refresh_token_expire_time"]

        request.headers["Authorization"] = f"token {token}"
        yield request


@dataclass
class OAuthWebAuth(httpx.Auth):
    """OAuth Web Flow Hook Authentication

    This auth flow wraps the OAuth token auth flow.
    """

    github: "GitHubCore"
    auth_strategy: "OAuthWebAuthStrategy"

    @property
    def client_id(self) -> str:
        return self.auth_strategy.client_id

    @property
    def client_secret(self) -> str:
        return self.auth_strategy.client_secret

    @property
    def code(self) -> str:
        return self.auth_strategy.code

    @property
    def redirect_uri(self) -> Optional[str]:
        return self.auth_strategy.redirect_uri

    @property
    def _token_auth_strategy(self) -> Optional["OAuthTokenAuthStrategy"]:
        return self.auth_strategy._token_auth

    @_token_auth_strategy.setter
    def _token_auth_strategy(self, value: "OAuthTokenAuthStrategy") -> None:
        self.auth_strategy._token_auth = value

    def sync_auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        # exchange token for the first time
        if (token_auth_strategy := self._token_auth_strategy) is None:
            flow = exchange_web_flow_code(
                self.github,
                self.client_id,
                self.client_secret,
                self.code,
                self.redirect_uri,
            )
            exchange_request = next(flow)
            while True:
                response = yield exchange_request
                response.read()
                try:
                    exchange_request = flow.send(response)
                except StopIteration as e:
                    data = e.value
                    break

            result = _parse_token_exchange_response(data)
            token_auth_strategy = OAuthTokenAuthStrategy(
                self.client_id, self.client_secret, **result
            )
            self._token_auth_strategy = token_auth_strategy

        auth = token_auth_strategy.get_auth_flow(self.github)
        yield from auth.sync_auth_flow(request)

    async def async_auth_flow(
        self, request: httpx.Request
    ) -> AsyncGenerator[httpx.Request, httpx.Response]:
        # exchange token for the first time
        if (token_auth_strategy := self._token_auth_strategy) is None:
            flow = exchange_web_flow_code(
                self.github,
                self.client_id,
                self.client_secret,
                self.code,
                self.redirect_uri,
            )
            exchange_request = next(flow)
            while True:
                response = yield exchange_request
                await response.aread()
                try:
                    exchange_request = flow.send(response)
                except StopIteration as e:
                    data = e.value
                    break

            result = _parse_token_exchange_response(data)
            token_auth_strategy = OAuthTokenAuthStrategy(
                self.client_id, self.client_secret, **result
            )
            self._token_auth_strategy = token_auth_strategy

        auth = token_auth_strategy.get_auth_flow(self.github)
        flow = auth.async_auth_flow(request)
        request = await flow.__anext__()
        while True:
            response = yield request
            try:
                request = await flow.asend(response)
            except StopAsyncIteration:
                break


@dataclass
class OAuthDeviceAuth(httpx.Auth):
    """OAuth Device Flow Hook Authentication

    This auth flow wraps the OAuth token auth flow.
    """

    github: "GitHubCore"
    auth_strategy: "OAuthDeviceAuthStrategy"

    @property
    def client_id(self) -> str:
        return self.auth_strategy.client_id

    @property
    def on_verification(self) -> Callable[[Any], Any]:
        return self.auth_strategy.on_verification

    @property
    def scopes(self) -> Optional[list[str]]:
        return self.auth_strategy.scopes

    @property
    def _token_auth_strategy(self) -> Optional["OAuthTokenAuthStrategy"]:
        return self.auth_strategy._token_auth

    @_token_auth_strategy.setter
    def _token_auth_strategy(self, value: Optional["OAuthTokenAuthStrategy"]) -> None:
        self.auth_strategy._token_auth = value

    def sync_auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        if require_bypass(request.url):
            yield request
            return

        # exchange token for the first time
        if (auth_strategy := self._token_auth_strategy) is None:
            # create device code
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

            result = _parse_create_device_code_response(data)
            _call_handler(self.on_verification, data)

            # loop to wait for user verification
            while True:
                # device code expired
                if datetime.now(timezone.utc) > result["expire_time"]:
                    raise AuthExpiredError("Device code expired.")
                flow = exchange_device_code(
                    self.github, self.client_id, result["device_code"]
                )
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
                    sleep(result["interval"])
                    continue

                # exchange token successfully
                result = _parse_token_exchange_response(data)
                auth_strategy = OAuthTokenAuthStrategy(self.client_id, None, **result)
                self._token_auth_strategy = auth_strategy
                break

        auth = auth_strategy.get_auth_flow(self.github)
        yield from auth.sync_auth_flow(request)

    async def async_auth_flow(
        self, request: httpx.Request
    ) -> AsyncGenerator[httpx.Request, httpx.Response]:
        if require_bypass(request.url):
            yield request
            return

        if anyio is None:
            raise RuntimeError(
                "AnyIO support for OAuth Device Flow should be installed "
                "with `pip install githubkit[auth-oauth-device]`"
            )

        # exchange token for the first time
        if (auth_strategy := self._token_auth_strategy) is None:
            # create device code
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

            result = _parse_create_device_code_response(data)
            await _async_call_handler(self.on_verification, data)

            # loop to wait for user verification
            while True:
                # device code expired
                if datetime.now(timezone.utc) > result["expire_time"]:
                    raise AuthExpiredError("Device code expired.")
                flow = exchange_device_code(
                    self.github, self.client_id, result["device_code"]
                )
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
                    await anyio.sleep(result["interval"])
                    continue

                result = _parse_token_exchange_response(data)
                auth_strategy = OAuthTokenAuthStrategy(self.client_id, None, **result)
                self._token_auth_strategy = auth_strategy
                break

        auth = auth_strategy.get_auth_flow(self.github)
        flow = auth.async_auth_flow(request)
        request = await flow.__anext__()
        while True:
            response = yield request
            await response.aread()
            try:
                request = await flow.asend(response)
            except StopAsyncIteration:
                break


@dataclass
class OAuthAppAuthStrategy(BaseAuthStrategy):
    """OAuth App Authentication"""

    client_id: str
    client_secret: str

    def as_web_user(
        self, code: str, redirect_uri: Optional[str] = None
    ) -> "OAuthWebAuthStrategy":
        return OAuthWebAuthStrategy(
            client_id=self.client_id,
            client_secret=self.client_secret,
            code=code,
            redirect_uri=redirect_uri,
        )

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return httpx.BasicAuth(self.client_id, self.client_secret)


@dataclass
class OAuthTokenAuthStrategy(BaseAuthStrategy):
    """OAuth Token Authentication"""

    client_id: str
    client_secret: Optional[str] = None  # client secret is optional in device flow
    token: Optional[str] = None
    expire_time: Optional[datetime] = None
    refresh_token: Optional[str] = None
    refresh_token_expire_time: Optional[datetime] = None

    def __post_init__(self):
        # either token or refresh_token should be provided
        if not self.token and not self.refresh_token:
            raise AuthCredentialError(
                "Either token or refresh_token should be provided."
            )
        # when both token and refresh_token are provided, expire_time should be provided
        if self.token and self.refresh_token and not self.expire_time:
            raise AuthCredentialError(
                "expire_time should be provided "
                "when both token and refresh_token are provided."
            )

    def refresh(self, github: "GitHubCore") -> Self:
        """Refresh access token with refresh token in place and return self."""

        if self.refresh_token is None:
            raise AuthCredentialError("Refresh token is not provided.")

        flow = refresh_token(
            github, self.client_id, self.client_secret, self.refresh_token
        )
        with github:
            with github.get_sync_client() as client:
                refresh_request = next(flow)
                while True:
                    response = client.send(refresh_request)
                    response.read()
                    try:
                        refresh_request = flow.send(response)
                    except StopIteration as e:
                        data = e.value
                        break

        result = _parse_token_exchange_response(data)
        self.token = result["token"]
        self.expire_time = result["expire_time"]
        self.refresh_token = result["refresh_token"]
        self.refresh_token_expire_time = result["refresh_token_expire_time"]
        return self

    async def async_refresh(self, github: "GitHubCore") -> Self:
        """Refresh access token with refresh token in place and return self."""

        if self.refresh_token is None:
            raise AuthCredentialError("Refresh token is not provided.")

        flow = refresh_token(
            github, self.client_id, self.client_secret, self.refresh_token
        )
        async with github:
            async with github.get_async_client() as client:
                refresh_request = next(flow)
                while True:
                    response = await client.send(refresh_request)
                    await response.aread()
                    try:
                        refresh_request = flow.send(response)
                    except StopIteration as e:
                        data = e.value
                        break

        result = _parse_token_exchange_response(data)
        self.token = result["token"]
        self.expire_time = result["expire_time"]
        self.refresh_token = result["refresh_token"]
        self.refresh_token_expire_time = result["refresh_token_expire_time"]
        return self

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return OAuthTokenAuth(github, self)


@dataclass
class OAuthWebAuthStrategy(BaseAuthStrategy):
    """OAuth Web Flow Authentication

    Note that this auth strategy is one-time use only.
    The code will expire after token exchange.
    """

    client_id: str
    client_secret: str
    code: str
    redirect_uri: Optional[str] = None

    _token_auth: Optional[OAuthTokenAuthStrategy] = field(
        default=None, init=False, repr=False
    )

    @property
    def token(self) -> str:
        if self._token_auth is None:
            raise RuntimeError("Token is not exchanged yet.")
        return cast(str, self._token_auth.token)

    @property
    def expire_time(self) -> Optional[datetime]:
        if self._token_auth is None:
            raise RuntimeError("Token is not exchanged yet.")
        return self._token_auth.expire_time

    @property
    def refresh_token(self) -> Optional[str]:
        if self._token_auth is None:
            raise RuntimeError("Token is not exchanged yet.")
        return self._token_auth.refresh_token

    @property
    def refresh_token_expire_time(self) -> Optional[datetime]:
        if self._token_auth is None:
            raise RuntimeError("Token is not exchanged yet.")
        return self._token_auth.refresh_token_expire_time

    def exchange_token(self, github: "GitHubCore") -> OAuthTokenAuthStrategy:
        """Exchange token using code and return the new token auth strategy."""

        if self._token_auth is not None:
            return self._token_auth

        flow = exchange_web_flow_code(
            github, self.client_id, self.client_secret, self.code, self.redirect_uri
        )
        with github:
            with github.get_sync_client() as client:
                exchange_request = next(flow)
                while True:
                    response = client.send(exchange_request)
                    response.read()
                    try:
                        exchange_request = flow.send(response)
                    except StopIteration as e:
                        data = e.value
                        break

        result = _parse_token_exchange_response(data)
        auth = OAuthTokenAuthStrategy(self.client_id, self.client_secret, **result)
        self._token_auth = auth
        return auth

    async def async_exchange_token(
        self, github: "GitHubCore"
    ) -> OAuthTokenAuthStrategy:
        """Exchange token using code and return the new token auth strategy."""

        if self._token_auth is not None:
            return self._token_auth

        flow = exchange_web_flow_code(
            github, self.client_id, self.client_secret, self.code, self.redirect_uri
        )
        async with github:
            async with github.get_async_client() as client:
                exchange_request = next(flow)
                while True:
                    response = await client.send(exchange_request)
                    await response.aread()
                    try:
                        exchange_request = flow.send(response)
                    except StopIteration as e:
                        data = e.value
                        break

        result = _parse_token_exchange_response(data)
        auth = OAuthTokenAuthStrategy(self.client_id, self.client_secret, **result)
        self._token_auth = auth
        return auth

    def as_oauth_app(self) -> OAuthAppAuthStrategy:
        return OAuthAppAuthStrategy(self.client_id, self.client_secret)

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        # use web auth flow to exchange token for the first time
        if self._token_auth is None:
            return OAuthWebAuth(github, self)

        return self._token_auth.get_auth_flow(github)


@dataclass
class OAuthDeviceAuthStrategy(BaseAuthStrategy):
    """OAuth Device Flow Authentication

    Note that this auth strategy instance is only for single device.
    If you want to create new device auth, you should create a new instance.
    """

    client_id: str
    on_verification: Callable[[Any], Any]
    scopes: Optional[list[str]] = None

    _token_auth: Optional[OAuthTokenAuthStrategy] = field(
        default=None, init=False, repr=False
    )

    @property
    def token(self) -> str:
        if self._token_auth is None:
            raise RuntimeError("Token is not exchanged yet.")
        return cast(str, self._token_auth.token)

    @property
    def expire_time(self) -> Optional[datetime]:
        if self._token_auth is None:
            raise RuntimeError("Token is not exchanged yet.")
        return self._token_auth.expire_time

    @property
    def refresh_token(self) -> Optional[str]:
        if self._token_auth is None:
            raise RuntimeError("Token is not exchanged yet.")
        return self._token_auth.refresh_token

    @property
    def refresh_token_expire_time(self) -> Optional[datetime]:
        if self._token_auth is None:
            raise RuntimeError("Token is not exchanged yet.")
        return self._token_auth.refresh_token_expire_time

    def exchange_token(self, github: "GitHubCore") -> OAuthTokenAuthStrategy:
        """Exchange token using device code and return the new token auth strategy."""

        if self._token_auth is not None:
            return self._token_auth

        flow = create_device_code(github, self.client_id, self.scopes)
        with github:
            with github.get_sync_client() as client:
                create_request = next(flow)
                while True:
                    response = client.send(create_request)
                    response.read()
                    try:
                        create_request = flow.send(response)
                    except StopIteration as e:
                        data = e.value
                        break

                result = _parse_create_device_code_response(data)
                _call_handler(self.on_verification, data)

                while True:
                    if datetime.now(timezone.utc) > result["expire_time"]:
                        raise AuthExpiredError("Device code expired.")
                    flow = exchange_device_code(
                        github, self.client_id, result["device_code"]
                    )
                    auth_request = next(flow)
                    while True:
                        response = client.send(auth_request)
                        response.read()
                        try:
                            auth_request = flow.send(response)
                        except StopIteration as e:
                            data = e.value
                            break

                    if "error" in data:
                        sleep(result["interval"])
                        continue

                    result = _parse_token_exchange_response(data)
                    auth = OAuthTokenAuthStrategy(self.client_id, None, **result)
                    self._token_auth = auth
                    return auth

    async def async_exchange_token(
        self, github: "GitHubCore"
    ) -> OAuthTokenAuthStrategy:
        """Exchange token using device code and return the new token auth strategy."""

        if self._token_auth is not None:
            return self._token_auth

        if anyio is None:
            raise RuntimeError(
                "AnyIO support for OAuth Device Flow should be installed "
                "with `pip install githubkit[auth-oauth-device]`"
            )

        flow = create_device_code(github, self.client_id, self.scopes)
        async with github:
            async with github.get_async_client() as client:
                create_request = next(flow)
                while True:
                    response = await client.send(create_request)
                    await response.aread()
                    try:
                        create_request = flow.send(response)
                    except StopIteration as e:
                        data = e.value
                        break

                result = _parse_create_device_code_response(data)
                await _async_call_handler(self.on_verification, data)

                while True:
                    if datetime.now(timezone.utc) > result["expire_time"]:
                        raise AuthExpiredError("Device code expired.")
                    flow = exchange_device_code(
                        github, self.client_id, result["device_code"]
                    )
                    auth_request = next(flow)
                    while True:
                        response = await client.send(auth_request)
                        await response.aread()
                        try:
                            auth_request = flow.send(response)
                        except StopIteration as e:
                            data = e.value
                            break

                    if "error" in data:
                        await anyio.sleep(result["interval"])
                        continue

                    result = _parse_token_exchange_response(data)
                    auth = OAuthTokenAuthStrategy(self.client_id, None, **result)
                    self._token_auth = auth
                    return auth

    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        # use device auth flow to exchange token for the first time
        if self._token_auth is None:
            return OAuthDeviceAuth(github, self)

        return self._token_auth.get_auth_flow(github)
