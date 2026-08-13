import threading

import pytest

from githubkit import GitHubCore
from githubkit.throttling import LocalThrottler


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


def test_core_context_manager_safety():
    gh = GitHubCore()
    with gh:
        with pytest.raises(RuntimeError):
            gh.__enter__()

    # Ensure no lingering client after error
    assert gh._GitHubCore__sync_client.get() is None
