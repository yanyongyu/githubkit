import abc
from datetime import timedelta
from typing import Optional

from hishel import AsyncBaseStorage, BaseStorage, Controller


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
        """Get the cache storage instance used in sync context

        raise CacheUnsupportedError if the strategy does not support sync usage
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_async_cache_storage(self) -> AsyncBaseCache:
        """Get the cache storage instance used in async context

        raise CacheUnsupportedError if the strategy does not support async usage
        """
        raise NotImplementedError

    def get_hishel_controller(self) -> Optional[Controller]:
        """Get the hishel controller instance

        Return `None` to use the default controller
        """
        return None

    @abc.abstractmethod
    def get_hishel_storage(self) -> BaseStorage:
        """Get the hishel storage instance used in sync context"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_async_hishel_storage(self) -> AsyncBaseStorage:
        """Get the hishel storage instance used in async context"""
        raise NotImplementedError
