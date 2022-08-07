import abc
from typing import Union, Optional
from datetime import datetime, timedelta


class BaseCache(abc.ABC):
    @abc.abstractmethod
    def get(self, key: str) -> Optional[str]:
        raise NotImplementedError

    @abc.abstractmethod
    async def aget(self, key: str) -> Optional[str]:
        raise NotImplementedError

    @abc.abstractmethod
    def set(self, key: str, value: str, ex: timedelta) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    async def aset(self, key: str, value: str, ex: timedelta) -> None:
        raise NotImplementedError
