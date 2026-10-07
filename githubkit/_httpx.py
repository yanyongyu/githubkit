from typing import TYPE_CHECKING
import warnings

if TYPE_CHECKING:
    from hishel.httpx2 import AsyncCacheTransport as AsyncCacheTransport
    from hishel.httpx2 import SyncCacheTransport as SyncCacheTransport
    import httpx2 as httpx
else:
    try:
        from hishel.httpx2 import AsyncCacheTransport, SyncCacheTransport
        import httpx2 as httpx
    except ImportError:
        # Hishel wraps a missing HTTP client in ImportError.
        try:
            from hishel.httpx import AsyncCacheTransport as AsyncCacheTransport
            from hishel.httpx import SyncCacheTransport as SyncCacheTransport
            import httpx as httpx
        except ImportError:
            raise RuntimeError(
                "GitHubKit requires httpx2 and its Hishel integration "
                "to be installed.\n"
                "You can install them with:\n"
                '    $ pip install httpx2 "hishel[async,httpx2]>=1.4.0"\n'
            ) from None
        else:
            warnings.warn(
                "Using `httpx` with GitHubKit is deprecated; install `httpx2` "
                "and `hishel[async,httpx2]>=1.4.0` instead.",
                DeprecationWarning,
                stacklevel=2,
            )
