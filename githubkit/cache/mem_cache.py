from typing import Optional
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta

from hishel import InMemoryStorage, AsyncInMemoryStorage

from .base import BaseCache, AsyncBaseCache, BaseCacheStrategy


@dataclass(frozen=True)
class _Item:
    value: str
    expire_at: Optional[datetime] = None


class MemCache(AsyncBaseCache, BaseCache):
    """Simple Memory Cache with Expiration Support"""

    def __init__(self):
        self._cache: dict[str, _Item] = {}

    def expire(self):
        now = datetime.now(timezone.utc)
        for key, item in list(self._cache.items()):
            if item.expire_at is not None and item.expire_at < now:
                self._cache.pop(key, None)

    def get(self, key: str) -> Optional[str]:
        self.expire()
        return (item := self._cache.get(key, None)) and item.value

    async def aget(self, key: str) -> Optional[str]:
        return self.get(key)

    def set(self, key: str, value: str, ex: timedelta) -> None:
        self.expire()
        self._cache[key] = _Item(value, datetime.now(timezone.utc) + ex)

    async def aset(self, key: str, value: str, ex: timedelta) -> None:
        return self.set(key, value, ex)


class MemCacheStrategy(BaseCacheStrategy):
    def __init__(self) -> None:
        self._cache: Optional[MemCache] = None
        self._hishel_storage: Optional[InMemoryStorage] = None
        self._hishel_async_storage: Optional[AsyncInMemoryStorage] = None

    def get_cache_storage(self) -> MemCache:
        if self._cache is None:
            self._cache = MemCache()
        return self._cache

    def get_async_cache_storage(self) -> MemCache:
        return self.get_cache_storage()

    def get_hishel_storage(self) -> InMemoryStorage:
        if self._hishel_storage is None:
            self._hishel_storage = InMemoryStorage()
        return self._hishel_storage

    def get_async_hishel_storage(self) -> AsyncInMemoryStorage:
        if self._hishel_async_storage is None:
            self._hishel_async_storage = AsyncInMemoryStorage()
        return self._hishel_async_storage
