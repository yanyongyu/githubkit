from datetime import timedelta
from typing import TYPE_CHECKING, Any, NoReturn
from typing_extensions import override

from hishel import AsyncBaseStorage, AsyncRedisStorage, RedisStorage

from githubkit.exception import CacheUnsupportedError

from .base import AsyncBaseCache, BaseCache, BaseCacheStrategy

if TYPE_CHECKING:
    from redis import Redis
    from redis.asyncio import Redis as AsyncRedis


def _ensure_str_or_none(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    elif isinstance(value, bytes):
        return value.decode("utf-8")
    elif value is None:
        return None
    else:
        raise RuntimeError(f"Unexpected redis value {value!r} with type {type(value)}")


class RedisCache(BaseCache):
    def __init__(self, client: "Redis", prefix: str | None = None) -> None:
        self.client = client
        self.prefix = prefix

    def _get_key(self, key: str) -> str:
        if self.prefix is not None:
            return f"{self.prefix}:{key}"
        return key

    @override
    def get(self, key: str) -> str | None:
        data = self.client.get(self._get_key(key))
        return _ensure_str_or_none(data)

    @override
    def set(self, key: str, value: str, ex: timedelta) -> None:
        self.client.set(self._get_key(key), value, ex)


class AsyncRedisCache(AsyncBaseCache):
    def __init__(self, client: "AsyncRedis", prefix: str | None = None) -> None:
        self.client = client
        self.prefix = prefix

    def _get_key(self, key: str) -> str:
        if self.prefix is not None:
            return f"{self.prefix}:{key}"
        return key

    @override
    async def aget(self, key: str) -> str | None:
        data = await self.client.get(self._get_key(key))
        return _ensure_str_or_none(data)

    @override
    async def aset(self, key: str, value: str, ex: timedelta) -> None:
        await self.client.set(self._get_key(key), value, ex)


class RedisCacheStrategy(BaseCacheStrategy):
    def __init__(self, client: "Redis", prefix: str | None = None) -> None:
        self.client = client
        self.prefix = prefix.removesuffix(":") if prefix else None

    @override
    def get_cache_storage(self) -> RedisCache:
        return RedisCache(self.client, self.prefix)

    @override
    async def get_async_cache_storage(self) -> NoReturn:
        raise CacheUnsupportedError(
            "Sync redis cache strategy does not support async usage"
        )

    @override
    def get_hishel_storage(self) -> RedisStorage:
        return RedisStorage(client=self.client, key_prefix=self.prefix or "hishel")

    @override
    async def get_async_hishel_storage(self) -> NoReturn:
        raise CacheUnsupportedError(
            "Sync redis cache strategy does not support async usage"
        )


class AsyncRedisCacheStrategy(BaseCacheStrategy):
    def __init__(self, client: "AsyncRedis", prefix: str | None = None) -> None:
        self.client = client
        self.prefix = prefix.removesuffix(":") if prefix else None

    @override
    def get_cache_storage(self) -> NoReturn:
        raise CacheUnsupportedError(
            "Async redis cache strategy does not support sync usage"
        )

    @override
    async def get_async_cache_storage(self) -> AsyncRedisCache:
        return AsyncRedisCache(self.client, self.prefix)

    @override
    def get_hishel_storage(self) -> NoReturn:
        raise CacheUnsupportedError(
            "Async redis cache strategy does not support sync usage"
        )

    @override
    async def get_async_hishel_storage(self) -> AsyncBaseStorage:
        return AsyncRedisStorage(client=self.client, key_prefix=self.prefix or "hishel")
