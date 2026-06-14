import abc
from datetime import timedelta

from hishel import (
    AsyncBaseStorage,
    CacheOptions,
    CachePolicy,
    SpecificationPolicy,
    SyncBaseStorage,
)


class BaseCache(abc.ABC):
    @abc.abstractmethod
    def get(self, key: str) -> str | None:
        raise NotImplementedError

    @abc.abstractmethod
    def set(self, key: str, value: str, ex: timedelta) -> None:
        raise NotImplementedError


class AsyncBaseCache(abc.ABC):
    @abc.abstractmethod
    async def aget(self, key: str) -> str | None:
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
    async def get_async_cache_storage(self) -> AsyncBaseCache:
        """Get the cache storage instance used in async context

        raise CacheUnsupportedError if the strategy does not support async usage
        """
        raise NotImplementedError

    def get_hishel_policy(self) -> CachePolicy:
        """Get the hishel cache policy instance"""
        return SpecificationPolicy(cache_options=CacheOptions(shared=False))

    @abc.abstractmethod
    def get_hishel_storage(self) -> SyncBaseStorage:
        """Get the hishel storage instance used in sync context"""
        raise NotImplementedError

    @abc.abstractmethod
    async def get_async_hishel_storage(self) -> AsyncBaseStorage:
        """Get the hishel storage instance used in async context"""
        raise NotImplementedError
