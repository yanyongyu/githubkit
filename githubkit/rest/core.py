from types import TracebackType
from contextlib import contextmanager, asynccontextmanager
from typing import (
    Any,
    Dict,
    List,
    Type,
    Tuple,
    Union,
    Optional,
    Generator,
    AsyncGenerator,
    cast,
)

import httpx

from .auth import BaseAuthStrategy, TokenAuthStrategy
from .typing import URLTypes, HeaderTypes, QueryParamTypes


class GitHubCore:
    def __init__(
        self,
        auth: Union[BaseAuthStrategy, str],
        base_url: Optional[Union[str, httpx.URL]] = None,
        user_agent: Optional[str] = None,
        timeout: Optional[Union[float, httpx.Timeout]] = None,
    ):
        self.auth: BaseAuthStrategy = (
            TokenAuthStrategy(auth) if isinstance(auth, str) else auth
        )

        base_url = base_url or httpx.URL("https://api.github.com")
        self.base_url: httpx.URL = (
            base_url if isinstance(base_url, httpx.URL) else httpx.URL(base_url)
        )

        self.user_agent: str = user_agent or "GitHubKit/Python"

        self.timeout: httpx.Timeout = (
            timeout if isinstance(timeout, httpx.Timeout) else httpx.Timeout(timeout)
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
            "base_url": self.base_url,
            "headers": {
                "User-Agent": self.user_agent,
                "Accept": "application/vnd.github.v3+json",
            },
            "timeout": self.timeout,
            "follow_redirects": True,
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

    def request(
        self,
        method: str,
        url: URLTypes,
        params: Optional[QueryParamTypes] = None,
        json: Optional[Any] = None,
        headers: Optional[HeaderTypes] = None,
    ) -> httpx.Response:
        with self.get_sync_client() as client:
            return client.request(
                method, url, params=params, json=json, headers=headers
            )

    async def arequest(
        self,
        method: str,
        url: URLTypes,
        params: Optional[QueryParamTypes] = None,
        json: Optional[Any] = None,
        headers: Optional[HeaderTypes] = None,
    ) -> httpx.Response:
        async with self.get_async_client() as client:
            return await client.request(
                method, url, params=params, json=json, headers=headers
            )
