from .base import BaseCache as BaseCache
from .mem_cache import MemCache as MemCache
from .base import AsyncBaseCache as AsyncBaseCache
from .base import BaseCacheStrategy as BaseCacheStrategy
from .mem_cache import MemCacheStrategy as MemCacheStrategy

DEFAULT_CACHE_STRATEGY = MemCacheStrategy()
