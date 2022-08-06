from dataclasses import dataclass
from typing import Dict, Optional
from datetime import datetime, timezone

from .base import BaseCache


@dataclass(frozen=True)
class _Item:
    value: str
    expire_at: datetime


class MemCache(BaseCache):
    """Simple Memory Cache with Expiration Support"""

    def __init__(self):
        self._cache: Dict[str, _Item] = {}

    def expire(self):
        now = datetime.now(timezone.utc)
        for key, item in list(self._cache.items()):
            if item.expire_at < now:
                self._cache.pop(key, None)

    def get(self, key: str) -> Optional[str]:
        self.expire()
        return (item := self._cache.get(key, None)) and item.value

    async def aget(self, key: str) -> Optional[str]:
        return self.get(key)

    def set(self, key: str, value: str, expire_at: datetime) -> None:
        self.expire()
        self._cache[key] = _Item(value, expire_at.astimezone(timezone.utc))

    async def aset(self, key: str, value: str, expire_at: datetime) -> None:
        return self.set(key, value, expire_at)
