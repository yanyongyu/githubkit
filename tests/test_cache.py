from datetime import timedelta
import time

from githubkit.cache.mem_cache import MemCache


def test_mem_cache_passive_expiry():
    cache = MemCache()
    cache.set("key1", "val1", timedelta(milliseconds=1))
    cache.set("key2", "val2", timedelta(hours=1))

    time.sleep(0.01)

    assert cache.get("key1") is None
    assert cache.get("key2") == "val2"
    assert "key2" in cache._cache
