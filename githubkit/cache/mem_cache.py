from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import sqlite3
from typing_extensions import override

import anysqlite
from hishel import AsyncSqliteStorage, SyncSqliteStorage

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

    @override
    def get_cache_storage(self) -> MemCache:
        if self._cache is None:
            self._cache = MemCache()
        return self._cache

    @override
    async def get_async_cache_storage(self) -> MemCache:
        return self.get_cache_storage()

    @override
    def get_hishel_storage(self) -> SyncSqliteStorage:
        # NOTE: although it's possible to use in-memory sqlite for hishel,
        # the connection can not be shared between clients.
        # the storage is closed when the client transport is closed.
        return SyncSqliteStorage(connection=sqlite3.connect(":memory:"))

    @override
    async def get_async_hishel_storage(self) -> AsyncSqliteStorage:
        return AsyncSqliteStorage(connection=await anysqlite.connect(":memory:"))
