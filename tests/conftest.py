import pytest

from githubkit import GitHub, ActionAuthStrategy


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture
def g() -> GitHub[ActionAuthStrategy]:
    return GitHub(ActionAuthStrategy(), http_cache=False)
