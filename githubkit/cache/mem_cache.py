from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing_extensions import override

from githubkit.hishel import AsyncMemoryStorage, SyncMemoryStorage

from .base import AsyncBaseCache, BaseCache, BaseCacheStrategy


@dataclass(frozen=True)
class _Item:
    value: str
    expire_at: datetime | None = None


class MemCache(AsyncBaseCache, BaseCache):
    """Simple Memory Cache with Expiration Support"""

    def __init__(self):
        self._cache: dict[str, _Item] = {}

    def expire(self):
        now = datetime.now(timezone.utc)
        for key, item in list(self._cache.items()):
            if item.expire_at is not None and item.expire_at < now:
                self._cache.pop(key, None)

    @override
    def get(self, key: str) -> str | None:
        self.expire()
        return (item := self._cache.get(key, None)) and item.value

    @override
    async def aget(self, key: str) -> str | None:
        return self.get(key)

    @override
    def set(self, key: str, value: str, ex: timedelta) -> None:
        self.expire()
        self._cache[key] = _Item(value, datetime.now(timezone.utc) + ex)

    @override
    async def aset(self, key: str, value: str, ex: timedelta) -> None:
        return self.set(key, value, ex)


class MemCacheStrategy(BaseCacheStrategy):
    def __init__(self) -> None:
        self._cache: MemCache | None = None
        self._hishel_storage: SyncMemoryStorage | None = None
        self._hishel_async_storage: AsyncMemoryStorage | None = None

    @override
    def get_cache_storage(self) -> MemCache:
        if self._cache is None:
            self._cache = MemCache()
        return self._cache

    @override
    async def get_async_cache_storage(self) -> MemCache:
        return self.get_cache_storage()

    @override
    def get_hishel_storage(self) -> SyncMemoryStorage:
        if self._hishel_storage is None:
            self._hishel_storage = SyncMemoryStorage(keep_unclosed=True)
        return self._hishel_storage

    @override
    async def get_async_hishel_storage(self) -> AsyncMemoryStorage:
        if self._hishel_async_storage is None:
            self._hishel_async_storage = AsyncMemoryStorage(keep_unclosed=True)
        return self._hishel_async_storage

    def cleanup(self) -> None:
        if self._cache is not None:
            self._cache = None
        if self._hishel_storage is not None:
            self._hishel_storage.force_close()
            self._hishel_storage = None

    async def acleanup(self) -> None:
        self.cleanup()
        if self._hishel_async_storage is not None:
            await self._hishel_async_storage.force_close()
            self._hishel_async_storage = None
