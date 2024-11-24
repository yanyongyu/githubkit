import pytest

from githubkit import ActionAuthStrategy, GitHub


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture
def g() -> GitHub[ActionAuthStrategy]:
    return GitHub(ActionAuthStrategy(), http_cache=False)
