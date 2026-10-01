import json
import subprocess
import sys
import textwrap

import pytest


@pytest.mark.parametrize(
    ("blocked", "expected"),
    [
        ([], "httpx2"),
        (["httpx"], "httpx2"),
        (["httpx2"], "httpx"),
        (["hishel.httpx2"], "httpx"),
        (["httpx", "httpx2"], None),
        (["hishel.httpx", "hishel.httpx2"], None),
    ],
)
def test_http_client_selection(blocked: list[str], expected: str | None):
    # A fresh interpreter exercises package initialization without cached imports.
    script = textwrap.dedent(
        """
        import asyncio
        import importlib.abc
        import json
        import sys
        import warnings

        blocked, expected = json.loads(sys.argv[1])

        class BlockImports(importlib.abc.MetaPathFinder):
            def find_spec(self, fullname, path=None, target=None):
                if any(fullname == name or fullname.startswith(name + ".")
                       for name in blocked):
                    raise ModuleNotFoundError(fullname, name=fullname)

        sys.meta_path.insert(0, BlockImports())
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always", DeprecationWarning)
            if expected is None:
                try:
                    import githubkit
                except RuntimeError as exc:
                    install = 'pip install httpx2 "hishel[async,httpx2]>=1.4.0"'
                    assert install in str(exc)
                    assert exc.__suppress_context__
                else:
                    raise AssertionError("Missing dependencies should fail")
                sys.exit(0)

            from githubkit import GitHub
            from githubkit._httpx import (
                httpx, AsyncCacheTransport, SyncCacheTransport,
            )
            from githubkit.hishel import AsyncCacheClient, SyncCacheClient

        assert httpx.__name__ == expected
        assert issubclass(SyncCacheTransport, httpx.BaseTransport)
        assert issubclass(AsyncCacheTransport, httpx.AsyncBaseTransport)
        assert issubclass(SyncCacheClient, httpx.Client)
        assert issubclass(AsyncCacheClient, httpx.AsyncClient)
        deprecations = [w for w in caught if w.category is DeprecationWarning]
        assert len(deprecations) == (1 if expected == "httpx" else 0)
        if deprecations:
            assert "deprecated" in str(deprecations[0].message)

        calls = []
        def handle(request):
            assert isinstance(request, httpx.Request)
            calls.append(request)
            return httpx.Response(
                200, json={"backend": expected},
                headers={"Cache-Control": "max-age=3600"},
            )

        transport = httpx.MockTransport(handle)
        with GitHub(transport=transport, trust_env=False) as github:
            for _ in range(2):
                # GitHubKit normally sends no-cache to force revalidation.
                response = github.request(
                    "GET", "/httpx-migration-test",
                    headers={"Cache-Control": "max-age=3600"},
                )
                assert isinstance(response.raw_response, httpx.Response)
                assert response.raw_response.json() == {"backend": expected}
        assert len(calls) == 1, "Sync Hishel cache did not serve the second request"

        async def check_async():
            async with GitHub(async_transport=transport, trust_env=False) as github:
                for _ in range(2):
                    response = await github.arequest(
                        "GET", "/httpx-migration-async-test",
                        headers={"Cache-Control": "max-age=3600"},
                    )
                    assert isinstance(response.raw_response, httpx.Response)
                    assert response.raw_response.json() == {"backend": expected}

        asyncio.run(check_async())
        assert len(calls) == 2, "Async Hishel cache did not serve the second request"
        """
    )

    result = subprocess.run(
        [sys.executable, "-c", script, json.dumps([blocked, expected])],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
