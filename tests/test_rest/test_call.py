import pytest

from githubkit import GitHub
from githubkit.versions import LATEST_VERSION
from githubkit.versions.latest.models import FullRepository

OWNER = "yanyongyu"
REPO = "githubkit"


def test_call(g: GitHub):
    resp = g.rest.repos.get(OWNER, REPO)
    assert isinstance(resp.parsed_data, FullRepository)


@pytest.mark.anyio
async def test_async_call(g: GitHub):
    resp = await g.rest.repos.async_get(OWNER, REPO)
    assert isinstance(resp.parsed_data, FullRepository)


def test_versioned_call(g: GitHub):
    resp = g.rest(LATEST_VERSION).repos.get(OWNER, REPO)
    assert isinstance(resp.parsed_data, FullRepository)


@pytest.mark.anyio
async def test_versioned_async_call(g: GitHub):
    resp = await g.rest(LATEST_VERSION).repos.async_get(OWNER, REPO)
    assert isinstance(resp.parsed_data, FullRepository)
