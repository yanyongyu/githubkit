import abc
from collections.abc import AsyncGenerator, Generator
from contextlib import asynccontextmanager, contextmanager
import threading
from typing import Any, Optional
from typing_extensions import override

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
    """Simple local throttler."""

    def __init__(self, max_concurrency: int) -> None:
        self.max_concurrency = max_concurrency
        self._semaphore: Optional[threading.Semaphore] = None
        self._async_semaphore: Optional[anyio.Semaphore] = None

    @property
    def semaphore(self) -> threading.Semaphore:
        if self._semaphore is None:
            self._semaphore = threading.Semaphore(self.max_concurrency)
        return self._semaphore

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
