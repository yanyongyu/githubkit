import abc
from datetime import timedelta
from typing import Optional

from hishel import AsyncBaseStorage, BaseStorage, Controller

from githubkit.typing import HishelControllerOptions


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

    def get_hishel_controller_options(self) -> HishelControllerOptions:
        """Get the hishel controller options"""
        # set always revalidate by default
        # See: https://hishel.com/examples/github/
        return HishelControllerOptions(always_revalidate=True)

    def get_hishel_controller(self) -> Controller:
        """Get the hishel controller instance

        Get the controller options from `get_hishel_controller_options` method
        """
        return Controller(**self.get_hishel_controller_options())

    @abc.abstractmethod
    def get_hishel_storage(self) -> BaseStorage:
        """Get the hishel storage instance used in sync context"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_async_hishel_storage(self) -> AsyncBaseStorage:
        """Get the hishel storage instance used in async context"""
        raise NotImplementedError
