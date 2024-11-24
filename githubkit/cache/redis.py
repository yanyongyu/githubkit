from datetime import timedelta
from typing import TYPE_CHECKING, Any, NoReturn, Optional
from typing_extensions import override

from hishel import AsyncBaseStorage, AsyncRedisStorage, RedisStorage

from githubkit.exception import CacheUnsupportedError

from .base import AsyncBaseCache, BaseCache, BaseCacheStrategy

if TYPE_CHECKING:
    from redis import Redis
    from redis.asyncio import Redis as AsyncRedis


def _ensure_str_or_none(value: Any) -> Optional[str]:
    if isinstance(value, str):
        return value
    elif isinstance(value, bytes):
        return value.decode("utf-8")
    elif value is None:
        return None
    else:
        raise RuntimeError(f"Unexpected redis value {value!r} with type {type(value)}")


class RedisCache(BaseCache):
    def __init__(self, client: "Redis") -> None:
        self.client = client

    @override
    def get(self, key: str) -> Optional[str]:
        data = self.client.get(key)
        return _ensure_str_or_none(data)

    @override
    def set(self, key: str, value: str, ex: timedelta) -> None:
        self.client.set(key, value, ex)


class AsyncRedisCache(AsyncBaseCache):
    def __init__(self, client: "AsyncRedis") -> None:
        self.client = client

    @override
    async def aget(self, key: str) -> Optional[str]:
        data = await self.client.get(key)
        return _ensure_str_or_none(data)

    @override
    async def aset(self, key: str, value: str, ex: timedelta) -> None:
        await self.client.set(key, value, ex)


class RedisCacheStrategy(BaseCacheStrategy):
    def __init__(self, client: "Redis") -> None:
        self.client = client

    @override
    def get_cache_storage(self) -> RedisCache:
        return RedisCache(self.client)

    @override
    def get_async_cache_storage(self) -> NoReturn:
        raise CacheUnsupportedError(
            "Sync redis cache strategy does not support async usage"
        )

    @override
    def get_hishel_storage(self) -> RedisStorage:
        return RedisStorage(client=self.client)

    @override
    def get_async_hishel_storage(self) -> NoReturn:
        raise CacheUnsupportedError(
            "Sync redis cache strategy does not support async usage"
        )


class AsyncRedisCacheStrategy(BaseCacheStrategy):
    def __init__(self, client: "AsyncRedis") -> None:
        self.client = client

    @override
    def get_cache_storage(self) -> NoReturn:
        raise CacheUnsupportedError(
            "Async redis cache strategy does not support sync usage"
        )

    @override
    def get_async_cache_storage(self) -> AsyncRedisCache:
        return AsyncRedisCache(self.client)

    @override
    def get_hishel_storage(self) -> NoReturn:
        raise CacheUnsupportedError(
            "Async redis cache strategy does not support sync usage"
        )

    @override
    def get_async_hishel_storage(self) -> AsyncBaseStorage:
        return AsyncRedisStorage(client=self.client)
