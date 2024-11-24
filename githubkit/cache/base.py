import abc
from datetime import timedelta
from typing import Optional

from hishel import AsyncBaseStorage, BaseStorage


class BaseCache(abc.ABC):
    @abc.abstractmethod
    def get(self, key: str) -> Optional[str]:
        raise NotImplementedError

    @abc.abstractmethod
    def set(self, key: str, value: str, ex: timedelta) -> None:
        raise NotImplementedError


class AsyncBaseCache(abc.ABC):
    @abc.abstractmethod
    async def aget(self, key: str) -> Optional[str]:
        raise NotImplementedError

    @abc.abstractmethod
    async def aset(self, key: str, value: str, ex: timedelta) -> None:
        raise NotImplementedError


class BaseCacheStrategy(abc.ABC):
    @abc.abstractmethod
    def get_cache_storage(self) -> BaseCache:
        raise NotImplementedError

    @abc.abstractmethod
    def get_async_cache_storage(self) -> AsyncBaseCache:
        raise NotImplementedError

    @abc.abstractmethod
    def get_hishel_storage(self) -> BaseStorage:
        raise NotImplementedError

    @abc.abstractmethod
    def get_async_hishel_storage(self) -> AsyncBaseStorage:
        raise NotImplementedError
