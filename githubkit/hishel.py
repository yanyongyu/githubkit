import sqlite3
from typing import Any
from typing_extensions import override

import anysqlite
from hishel import (
    AsyncBaseStorage,
    AsyncSqliteStorage,
    BaseStorage,
    CacheOptions,
    SqliteStorage,
)

from ._httpx import AsyncCacheTransport, CacheTransport, httpx


class SyncCacheClient(httpx.Client):
    def __init__(self, *args: Any, **kwargs: Any):
        self.storage: BaseStorage | None = kwargs.pop("storage", None)
        self.policy: CacheOptions | bool = kwargs.pop("policy", True)
        super().__init__(*args, **kwargs)

    def _init_transport(self, *args, **kwargs) -> httpx.BaseTransport:
        _transport = super()._init_transport(*args, **kwargs)
        return CacheTransport(
            next_transport=_transport, storage=self.storage, rfc=self.policy
        )

    def _init_proxy_transport(self, *args, **kwargs) -> httpx.BaseTransport:
        _transport = super()._init_proxy_transport(*args, **kwargs)
        return CacheTransport(
            next_transport=_transport, storage=self.storage, rfc=self.policy
        )


class AsyncCacheClient(httpx.AsyncClient):
    def __init__(self, *args: Any, **kwargs: Any):
        self.storage: AsyncBaseStorage | None = kwargs.pop("storage", None)
        self.policy: CacheOptions | bool = kwargs.pop("policy", True)
        super().__init__(*args, **kwargs)

    def _init_transport(self, *args, **kwargs) -> httpx.AsyncBaseTransport:
        _transport = super()._init_transport(*args, **kwargs)
        return AsyncCacheTransport(
            next_transport=_transport, storage=self.storage, rfc=self.policy
        )

    def _init_proxy_transport(self, *args, **kwargs) -> httpx.AsyncBaseTransport:
        _transport = super()._init_proxy_transport(*args, **kwargs)
        return AsyncCacheTransport(
            next_transport=_transport, storage=self.storage, rfc=self.policy
        )


class SyncMemoryStorage(SqliteStorage):
    def __init__(
        self,
        *,
        default_ttl: float | None = None,
        keep_unclosed: bool = False,
    ) -> None:
        super().__init__(
            default_ttl=default_ttl,
        )
        # NOTE: hishel close the storage when the client transport is closed.
        # but for in-memory sqlite,
        # we may want to keep it unclosed to preserve the data for the next client.
        self.keep_unclosed = keep_unclosed

    @override
    def _ensure_connection(self) -> sqlite3.Connection:
        if self.connection is None:
            self.connection = sqlite3.connect(":memory:", check_same_thread=False)

        return super()._ensure_connection()

    @override
    def close(self) -> None:
        if self.keep_unclosed:
            return
        return super().close()

    def force_close(self) -> None:
        """Force close the connection, even if keep_unclosed is True."""
        return super().close()


class AsyncMemoryStorage(AsyncSqliteStorage):
    def __init__(
        self,
        *,
        default_ttl: float | None = None,
        keep_unclosed: bool = False,
    ) -> None:
        super().__init__(
            default_ttl=default_ttl,
        )
        # NOTE: hishel close the storage when the client transport is closed.
        # but for in-memory sqlite,
        # we may want to keep it unclosed to preserve the data for the next client.
        self.keep_unclosed = keep_unclosed

    @override
    async def _ensure_connection(self) -> anysqlite.Connection:
        if self.connection is not None and self._initialized:
            return self.connection

        async with self._init_lock:
            if self.connection is None:
                self.connection = await anysqlite.connect(":memory:")

        return await super()._ensure_connection()

    @override
    async def close(self) -> None:
        if self.keep_unclosed:
            # Do not close the connection, but drain all pending writes
            async with self._init_lock:
                return
        return await super().close()

    async def force_close(self) -> None:
        """Force close the connection, even if keep_unclosed is True."""
        return await super().close()
