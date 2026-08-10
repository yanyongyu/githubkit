from datetime import timedelta
import json
from pathlib import Path
import threading
from typing import Any, TypeVar

from githubkit_schemas.latest.models import FullRepository
import httpx
import pytest

from githubkit import GitHub, GitHubCore
from githubkit.cache.mem_cache import MemCache
from githubkit.response import Response
from githubkit.throttling import LocalThrottler
from githubkit.typing import UnsetType, URLTypes
from githubkit.utils import UNSET

T = TypeVar("T")


FAKE_RESPONSE = json.loads((Path(__file__).parent / "fake_response.json").read_text())


def target_sync_func():
    github = GitHub("xxxxx")
    resp = github.rest.repos.get("owner", "repo")
    return resp.parsed_data


def mock_request(
    g: GitHub,
    method: str,
    url: URLTypes,
    *,
    response_model: type[T] | UnsetType = UNSET,
    **kwargs: Any,
) -> Response[Any]:
    if method == "GET" and url == "/repos/owner/repo":
        return Response[T](
            httpx.Response(status_code=200, json=FAKE_RESPONSE),
            Any if response_model is UNSET else response_model,  # type: ignore
        )
    raise RuntimeError(f"Unexpected request: {method} {url}")


def test_sync_mock():
    with pytest.MonkeyPatch.context() as m:
        m.setattr(GitHub, "request", mock_request)

        repo = target_sync_func()
        assert isinstance(repo, FullRepository)


async def target_async_func():
    github = GitHub("xxxxx")
    resp = await github.rest.repos.async_get("owner", "repo")
    return resp.parsed_data


async def mock_arequest(
    g: GitHub,
    method: str,
    url: URLTypes,
    *,
    response_model: type[T] | UnsetType = UNSET,
    **kwargs: Any,
) -> Response[Any]:
    if method == "GET" and url == "/repos/owner/repo":
        return Response[T](
            httpx.Response(status_code=200, json=FAKE_RESPONSE),
            Any if response_model is UNSET else response_model,  # type: ignore
        )
    raise RuntimeError(f"Unexpected request: {method} {url}")


@pytest.mark.anyio
async def test_async_mock():
    with pytest.MonkeyPatch.context() as m:
        m.setattr(GitHub, "arequest", mock_arequest)

        repo = await target_async_func()
        assert isinstance(repo, FullRepository)


def test_local_throttler_thread_safety():
    throttler = LocalThrottler(max_concurrency=5)
    threads = []
    semaphores = []

    def get_sem():
        semaphores.append(throttler.semaphore)

    for _ in range(20):
        t = threading.Thread(target=get_sem)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    assert len(semaphores) == 20
    first_sem = semaphores[0]
    for sem in semaphores:
        assert sem is first_sem


def test_mem_cache_passive_expiry():
    cache = MemCache()
    cache.set("key1", "val1", timedelta(milliseconds=1))
    cache.set("key2", "val2", timedelta(hours=1))

    import time

    time.sleep(0.01)

    assert cache.get("key1") is None
    assert cache.get("key2") == "val2"
    assert "key2" in cache._cache


def test_core_context_manager_safety():
    gh = GitHubCore()
    with gh:
        with pytest.raises(RuntimeError):
            gh.__enter__()

    # Ensure no lingering client after error
    assert gh._GitHubCore__sync_client.get() is None
