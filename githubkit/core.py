import time
from types import TracebackType
from contextvars import ContextVar
from datetime import datetime, timezone, timedelta
from contextlib import contextmanager, asynccontextmanager
from typing import (
    Any,
    Dict,
    List,
    Type,
    Union,
    Generic,
    Literal,
    TypeVar,
    Optional,
    Generator,
    AsyncGenerator,
    cast,
    overload,
)

import anyio
import httpx
import hishel

from .utils import UNSET
from .response import Response
from .compat import to_jsonable_python
from .config import Config, get_config
from .auth import BaseAuthStrategy, TokenAuthStrategy, UnauthAuthStrategy
from .typing import (
    URLTypes,
    CookieTypes,
    HeaderTypes,
    ContentTypes,
    RequestFiles,
    QueryParamTypes,
    RetryDecisionFunc,
)
from .exception import (
    RequestError,
    RequestFailed,
    RequestTimeout,
    GitHubException,
    PrimaryRateLimitExceeded,
    SecondaryRateLimitExceeded,
)

T = TypeVar("T")
A = TypeVar("A", bound="BaseAuthStrategy")
AS = TypeVar("AS", bound="BaseAuthStrategy")


class GitHubCore(Generic[A]):
    # none auth with config
    @overload
    def __init__(
        self: "GitHubCore[UnauthAuthStrategy]",
        auth: None = None,
        *,
        config: Config,
    ): ...

    # token auth with config
    @overload
    def __init__(
        self: "GitHubCore[TokenAuthStrategy]",
        auth: str,
        *,
        config: Config,
    ): ...

    # other auth strategies with config
    @overload
    def __init__(
        self: "GitHubCore[AS]",
        auth: AS,
        *,
        config: Config,
    ): ...

    # none auth without config
    @overload
    def __init__(
        self: "GitHubCore[UnauthAuthStrategy]",
        auth: None = None,
        *,
        base_url: Optional[Union[str, httpx.URL]] = None,
        accept_format: Optional[str] = None,
        previews: Optional[List[str]] = None,
        user_agent: Optional[str] = None,
        follow_redirects: bool = True,
        timeout: Optional[Union[float, httpx.Timeout]] = None,
        http_cache: bool = True,
        auto_retry: Union[bool, RetryDecisionFunc] = True,
    ): ...

    # token auth without config
    @overload
    def __init__(
        self: "GitHubCore[TokenAuthStrategy]",
        auth: str,
        *,
        base_url: Optional[Union[str, httpx.URL]] = None,
        accept_format: Optional[str] = None,
        previews: Optional[List[str]] = None,
        user_agent: Optional[str] = None,
        follow_redirects: bool = True,
        timeout: Optional[Union[float, httpx.Timeout]] = None,
        http_cache: bool = True,
        auto_retry: Union[bool, RetryDecisionFunc] = True,
    ): ...

    # other auth strategies without config
    @overload
    def __init__(
        self: "GitHubCore[AS]",
        auth: AS,
        *,
        base_url: Optional[Union[str, httpx.URL]] = None,
        accept_format: Optional[str] = None,
        previews: Optional[List[str]] = None,
        user_agent: Optional[str] = None,
        follow_redirects: bool = True,
        timeout: Optional[Union[float, httpx.Timeout]] = None,
        http_cache: bool = True,
        auto_retry: Union[bool, RetryDecisionFunc] = True,
    ): ...

    def __init__(
        self,
        auth: Optional[Union[A, str]] = None,
        *,
        config: Optional[Config] = None,
        base_url: Optional[Union[str, httpx.URL]] = None,
        accept_format: Optional[str] = None,
        previews: Optional[List[str]] = None,
        user_agent: Optional[str] = None,
        follow_redirects: bool = True,
        timeout: Optional[Union[float, httpx.Timeout]] = None,
        http_cache: bool = True,
        auto_retry: Union[bool, RetryDecisionFunc] = True,
    ):
        auth = auth or UnauthAuthStrategy()  # type: ignore
        self.auth: A = (  # type: ignore
            TokenAuthStrategy(auth) if isinstance(auth, str) else auth
        )

        self.config = config or get_config(
            base_url,
            accept_format,
            previews,
            user_agent,
            follow_redirects,
            timeout,
            http_cache,
            auto_retry,
        )

        self.__sync_client: ContextVar[Optional[httpx.Client]] = ContextVar(
            "sync_client", default=None
        )
        self.__async_client: ContextVar[Optional[httpx.AsyncClient]] = ContextVar(
            "async_client", default=None
        )

    # sync context
    def __enter__(self):
        if self.__sync_client.get() is not None:
            raise RuntimeError("Cannot enter sync context twice")
        self.__sync_client.set(self._create_sync_client())
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ):
        cast(httpx.Client, self.__sync_client.get()).close()
        self.__sync_client.set(None)

    # async context
    async def __aenter__(self):
        if self.__async_client.get() is not None:
            raise RuntimeError("Cannot enter async context twice")
        self.__async_client.set(self._create_async_client())
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ):
        await cast(httpx.AsyncClient, self.__async_client.get()).aclose()
        self.__async_client.set(None)

    # default args for creating client
    def _get_client_defaults(self):
        return {
            "auth": self.auth.get_auth_flow(self),
            "base_url": self.config.base_url,
            "headers": {
                "User-Agent": self.config.user_agent,
                "Accept": self.config.accept,
            },
            "timeout": self.config.timeout,
            "follow_redirects": self.config.follow_redirects,
        }

    # create sync client
    def _create_sync_client(self) -> httpx.Client:
        if self.config.http_cache:
            transport = hishel.CacheTransport(
                httpx.HTTPTransport(), storage=hishel.InMemoryStorage()
            )
        else:
            transport = httpx.HTTPTransport()

        return httpx.Client(**self._get_client_defaults(), transport=transport)

    # get or create sync client
    @contextmanager
    def get_sync_client(self) -> Generator[httpx.Client, None, None]:
        if client := self.__sync_client.get():
            yield client
        else:
            client = self._create_sync_client()
            try:
                yield client
            finally:
                client.close()

    # create async client
    def _create_async_client(self) -> httpx.AsyncClient:
        if self.config.http_cache:
            transport = hishel.AsyncCacheTransport(
                httpx.AsyncHTTPTransport(), storage=hishel.AsyncInMemoryStorage()
            )
        else:
            transport = httpx.AsyncHTTPTransport()

        return httpx.AsyncClient(**self._get_client_defaults(), transport=transport)

    # get or create async client
    @asynccontextmanager
    async def get_async_client(self) -> AsyncGenerator[httpx.AsyncClient, None]:
        if client := self.__async_client.get():
            yield client
        else:
            client = self._create_async_client()
            try:
                yield client
            finally:
                await client.aclose()

    # sync request
    def _request(
        self,
        method: str,
        url: URLTypes,
        *,
        params: Optional[QueryParamTypes] = None,
        content: Optional[ContentTypes] = None,
        data: Optional[dict] = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
    ) -> httpx.Response:
        with self.get_sync_client() as client:
            try:
                return client.request(
                    method,
                    url,
                    params=params,
                    content=content,
                    data=data,
                    files=files,
                    json=to_jsonable_python(json),
                    headers=headers,
                    cookies=cookies,
                )
            except httpx.TimeoutException as e:
                raise RequestTimeout(e.request) from e
            except Exception as e:
                raise RequestError(repr(e)) from e

    # async request
    async def _arequest(
        self,
        method: str,
        url: URLTypes,
        *,
        params: Optional[QueryParamTypes] = None,
        content: Optional[ContentTypes] = None,
        data: Optional[dict] = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
    ) -> httpx.Response:
        async with self.get_async_client() as client:
            try:
                return await client.request(
                    method,
                    url,
                    params=params,
                    content=content,
                    data=data,
                    files=files,
                    json=to_jsonable_python(json),
                    headers=headers,
                    cookies=cookies,
                )
            except httpx.TimeoutException as e:
                raise RequestTimeout(e.request) from e
            except Exception as e:
                raise RequestError(repr(e)) from e

    # check and parse response
    @overload
    def _check(
        self,
        response: httpx.Response,
        response_model: Type[T],
        error_models: Optional[Dict[str, type]] = None,
    ) -> Response[T]: ...

    @overload
    def _check(
        self,
        response: httpx.Response,
        response_model: Literal[UNSET] = UNSET,
        error_models: Optional[Dict[str, type]] = None,
    ) -> Response[Any]: ...

    def _check(
        self,
        response: httpx.Response,
        response_model: Union[Type[T], Literal[UNSET]] = UNSET,
        error_models: Optional[Dict[str, type]] = None,
    ) -> Union[Response[T], Response[Any]]:
        if response.is_error:
            error_models = error_models or {}
            status_code = str(response.status_code)

            error_model = error_models.get(
                status_code,
                error_models.get(
                    f"{status_code[:-2]}XX", error_models.get("default", UNSET)
                ),
            )
            resp = Response(response, Any if error_model is UNSET else error_model)
        else:
            resp = Response(
                response, Any if response_model is UNSET else response_model
            )

        # only check rate limit when response is 403 or 429
        if response.status_code in (403, 429):
            self._check_rate_limit(resp)

        if response.is_error:
            raise RequestFailed(resp)
        return resp

    # check rate limit
    def _check_rate_limit(self, response: Response) -> None:
        # check rate limit exceeded
        # https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api#exceeding-the-rate-limit
        # https://docs.github.com/en/graphql/overview/rate-limits-and-node-limits-for-the-graphql-api#exceeding-the-rate-limit
        # https://github.com/octokit/plugin-throttling.js/blob/135a0f556752a6c4c0ed3b2798bb58e228cd179a/src/index.ts#L134-L179

        # Secondary rate limits
        # the `retry-after` response header is present
        if "retry-after" in response.headers:
            raise SecondaryRateLimitExceeded(
                response, self._extract_retry_after(response)
            )

        if (
            "x-ratelimit-remaining" in response.headers
            and response.headers["x-ratelimit-remaining"] == "0"
        ):
            retry_after = self._extract_retry_after(response)

            try:
                error = response.json()
            except Exception:
                error = None

            # Secondary rate limits
            # error message indicates that you exceeded a secondary rate limit
            if (
                isinstance(error, dict)
                and "message" in error
                and "secondary rate" in error["message"]
            ):
                raise SecondaryRateLimitExceeded(response, retry_after)

            # Primary rate limits
            raise PrimaryRateLimitExceeded(response, retry_after)

    def _extract_retry_after(self, response: Response) -> timedelta:
        if "retry-after" in response.headers:
            return timedelta(seconds=int(response.headers["retry-after"]))
        elif "x-ratelimit-reset" in response.headers:
            retry_after = datetime.fromtimestamp(
                int(response.headers["x-ratelimit-reset"]), tz=timezone.utc
            ) - datetime.now(tz=timezone.utc)
            return max(retry_after, timedelta())
        else:
            # wait for at least one minute before retrying
            return timedelta(seconds=60)

    # sync request and check
    @overload
    def request(
        self,
        method: str,
        url: URLTypes,
        *,
        params: Optional[QueryParamTypes] = None,
        content: Optional[ContentTypes] = None,
        data: Optional[dict] = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        response_model: Type[T],
        error_models: Optional[Dict[str, type]] = None,
    ) -> Response[T]: ...

    @overload
    def request(
        self,
        method: str,
        url: URLTypes,
        *,
        params: Optional[QueryParamTypes] = None,
        content: Optional[ContentTypes] = None,
        data: Optional[dict] = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        response_model: Literal[UNSET] = UNSET,
        error_models: Optional[Dict[str, type]] = None,
    ) -> Response[Any]: ...

    def request(
        self,
        method: str,
        url: URLTypes,
        *,
        params: Optional[QueryParamTypes] = None,
        content: Optional[ContentTypes] = None,
        data: Optional[dict] = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        response_model: Union[Type[T], Literal[UNSET]] = UNSET,
        error_models: Optional[Dict[str, type]] = None,
    ) -> Union[Response[T], Response[Any]]:
        retry_count: int = 0
        while True:
            try:
                raw_resp = self._request(
                    method,
                    url,
                    params=params,
                    content=content,
                    data=data,
                    files=files,
                    json=json,
                    headers=headers,
                    cookies=cookies,
                )
                return self._check(raw_resp, response_model, error_models)
            except GitHubException as e:
                if self.config.auto_retry is None:
                    raise
                else:
                    do_retry, retry_after = self.config.auto_retry(e, retry_count)

                if not do_retry:
                    raise

                time.sleep(retry_after.total_seconds() if retry_after else 60)
                retry_count += 1

    # async request and check
    @overload
    async def arequest(
        self,
        method: str,
        url: URLTypes,
        *,
        params: Optional[QueryParamTypes] = None,
        content: Optional[ContentTypes] = None,
        data: Optional[dict] = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        response_model: Type[T],
        error_models: Optional[Dict[str, type]] = None,
    ) -> Response[T]: ...

    @overload
    async def arequest(
        self,
        method: str,
        url: URLTypes,
        *,
        params: Optional[QueryParamTypes] = None,
        content: Optional[ContentTypes] = None,
        data: Optional[dict] = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        response_model: Literal[UNSET] = UNSET,
        error_models: Optional[Dict[str, type]] = None,
    ) -> Response[Any]: ...

    async def arequest(
        self,
        method: str,
        url: URLTypes,
        *,
        params: Optional[QueryParamTypes] = None,
        content: Optional[ContentTypes] = None,
        data: Optional[dict] = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        response_model: Union[Type[T], Literal[UNSET]] = UNSET,
        error_models: Optional[Dict[str, type]] = None,
    ) -> Union[Response[T], Response[Any]]:
        retry_count: int = 0
        while True:
            try:
                raw_resp = await self._arequest(
                    method,
                    url,
                    params=params,
                    content=content,
                    data=data,
                    files=files,
                    json=json,
                    headers=headers,
                    cookies=cookies,
                )
                return self._check(raw_resp, response_model, error_models)
            except GitHubException as e:
                if self.config.auto_retry is None:
                    raise
                else:
                    do_retry, retry_after = self.config.auto_retry(e, retry_count)

                if not do_retry:
                    raise

                await anyio.sleep(retry_after.total_seconds() if retry_after else 60)
                retry_count += 1
