from .base import BaseCache as BaseCache
from .mem_cache import MemCache as MemCache
from .redis import RedisCache as RedisCache
from .base import AsyncBaseCache as AsyncBaseCache
from .redis import AsyncRedisCache as AsyncRedisCache
from .base import BaseCacheStrategy as BaseCacheStrategy
from .mem_cache import MemCacheStrategy as MemCacheStrategy
from .redis import RedisCacheStrategy as RedisCacheStrategy
from .redis import AsyncRedisCacheStrategy as AsyncRedisCacheStrategy

DEFAULT_CACHE_STRATEGY = MemCacheStrategy()
