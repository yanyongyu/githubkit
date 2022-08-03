from types import TracebackType
from contextlib import contextmanager, asynccontextmanager
from typing import (
    Any,
    Dict,
    List,
    Type,
    Union,
    TypeVar,
    Optional,
    Generator,
    AsyncGenerator,
    cast,
)

import httpx

from .config import get_config
from .response import Response
from .exception import RequestFailed
from .auth import BaseAuthStrategy, NoneAuthStrategy, TokenAuthStrategy
from .typing import (
    URLTypes,
    CookieTypes,
    HeaderTypes,
    ContentTypes,
    RequestFiles,
    QueryParamTypes,
)

T = TypeVar("T")


class GitHubCore:
    def __init__(
        self,
        auth: Optional[Union[BaseAuthStrategy, str]] = None,
        *,
        base_url: Optional[Union[str, httpx.URL]] = None,
        accept_format: Optional[str] = None,
        previews: Optional[List[str]] = None,
        user_agent: Optional[str] = None,
        follow_redirects: bool = True,
        timeout: Optional[Union[float, httpx.Timeout]] = None,
    ):
        auth = auth or NoneAuthStrategy()
        self.auth: BaseAuthStrategy = (
            TokenAuthStrategy(auth) if isinstance(auth, str) else auth
        )

        self.config = get_config(
            base_url, accept_format, previews, user_agent, follow_redirects, timeout
        )

        self.__sync_client: Optional[httpx.Client] = None
        self.__async_client: Optional[httpx.AsyncClient] = None

    def __enter__(self):
        if self.__sync_client is not None:
            raise RuntimeError("Cannot enter sync context twice")
        self.__sync_client = self._create_sync_client()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ):
        cast(httpx.Client, self.__sync_client).close()
        self.__sync_client = None

    async def __aenter__(self):
        if self.__async_client is not None:
            raise RuntimeError("Cannot enter async context twice")
        self.__async_client = self._create_async_client()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ):
        await cast(httpx.AsyncClient, self.__async_client).aclose()
        self.__async_client = None

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

    def _create_sync_client(self) -> httpx.Client:
        return httpx.Client(**self._get_client_defaults())

    @contextmanager
    def get_sync_client(self) -> Generator[httpx.Client, None, None]:
        if self.__sync_client:
            yield self.__sync_client
        else:
            client = self._create_sync_client()
            try:
                yield client
            finally:
                client.close()

    def _create_async_client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(**self._get_client_defaults())

    @asynccontextmanager
    async def get_async_client(self) -> AsyncGenerator[httpx.AsyncClient, None]:
        if self.__async_client:
            yield self.__async_client
        else:
            client = self._create_async_client()
            try:
                yield client
            finally:
                await client.aclose()

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
            return client.request(
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
            return await client.request(
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

    def _check(
        self,
        response: httpx.Response,
        response_model: Type[T] = Any,
        error_models: Optional[Dict[str, type]] = None,
    ) -> Response[T]:
        if response.is_error:
            error_models = error_models or {}
            status_code = str(response.status_code)
            error_model = error_models.get(
                status_code,
                error_models.get(
                    f"{status_code[:-2]}XX", error_models.get("default", Any)
                ),
            )
            rep = Response(response, error_model)
            raise RequestFailed(rep)
        return Response(response, response_model)

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
        response_model: Type[T] = Any,
        error_models: Optional[Dict[str, type]] = None,
    ) -> Response[T]:
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
        response_model: Type[T] = Any,
        error_models: Optional[Dict[str, type]] = None,
    ) -> Response[T]:
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
