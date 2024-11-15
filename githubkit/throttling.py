import abc
import threading
from typing import Any, Optional
from typing_extensions import override
from collections.abc import Generator, AsyncGenerator
from contextlib import contextmanager, asynccontextmanager

import anyio
import httpx


class BaseThrottler(abc.ABC):
    """Throttle the number of concurrent requests to avoid hitting rate limits.

    See also:
    - https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api#avoid-concurrent-requests
    - https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits

    TODO: Implement the pause between mutative requests.
    """

    @abc.abstractmethod
    @contextmanager
    def acquire(self, request: httpx.Request) -> Generator[None, Any, Any]:
        raise NotImplementedError
        yield

    @abc.abstractmethod
    @asynccontextmanager
    async def async_acquire(self, request: httpx.Request) -> AsyncGenerator[None, Any]:
        raise NotImplementedError
        yield


class LocalThrottler(BaseThrottler):
    def __init__(self, max_concurrency: int) -> None:
        self.max_concurrency = max_concurrency
        self.semaphore = threading.Semaphore(max_concurrency)
        self._async_semaphore: Optional[anyio.Semaphore] = None

    @property
    def async_semaphore(self) -> anyio.Semaphore:
        if self._async_semaphore is None:
            self._async_semaphore = anyio.Semaphore(self.max_concurrency)
        return self._async_semaphore

    @override
    @contextmanager
    def acquire(self, request: httpx.Request) -> Generator[None, Any, Any]:
        with self.semaphore:
            yield

    @override
    @asynccontextmanager
    async def async_acquire(self, request: httpx.Request) -> AsyncGenerator[None, Any]:
        async with self.async_semaphore:
            yield
