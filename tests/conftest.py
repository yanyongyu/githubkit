import pytest

from githubkit import GitHub, ActionAuthStrategy


@pytest.fixture
def g() -> GitHub:
    return GitHub(ActionAuthStrategy())
