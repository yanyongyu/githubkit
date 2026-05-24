from typing import Any

from hishel import AsyncBaseStorage, CachePolicy, SyncBaseStorage
from hishel.httpx import AsyncCacheTransport, SyncCacheTransport
import httpx


class SyncCacheClient(httpx.Client):
    def __init__(self, *args: Any, **kwargs: Any):
        self.storage: SyncBaseStorage | None = kwargs.pop("storage", None)
        self.policy: CachePolicy | None = kwargs.pop("policy", None)
        super().__init__(*args, **kwargs)

    def _init_transport(self, *args, **kwargs) -> httpx.BaseTransport:
        _transport = super()._init_transport(*args, **kwargs)
        return SyncCacheTransport(
            next_transport=_transport, storage=self.storage, policy=self.policy
        )

    def _init_proxy_transport(self, *args, **kwargs) -> httpx.BaseTransport:
        _transport = super()._init_proxy_transport(*args, **kwargs)
        return SyncCacheTransport(
            next_transport=_transport, storage=self.storage, policy=self.policy
        )


class AsyncCacheClient(httpx.AsyncClient):
    def __init__(self, *args: Any, **kwargs: Any):
        self.storage: AsyncBaseStorage | None = kwargs.pop("storage", None)
        self.policy: CachePolicy | None = kwargs.pop("policy", None)
        super().__init__(*args, **kwargs)

    def _init_transport(self, *args, **kwargs) -> httpx.AsyncBaseTransport:
        _transport = super()._init_transport(*args, **kwargs)
        return AsyncCacheTransport(
            next_transport=_transport, storage=self.storage, policy=self.policy
        )

    def _init_proxy_transport(self, *args, **kwargs) -> httpx.AsyncBaseTransport:
        _transport = super()._init_proxy_transport(*args, **kwargs)
        return AsyncCacheTransport(
            next_transport=_transport, storage=self.storage, policy=self.policy
        )
