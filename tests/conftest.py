import pytest

from githubkit import GitHub, ActionAuthStrategy


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture
def g() -> GitHub:
    return GitHub(ActionAuthStrategy())
