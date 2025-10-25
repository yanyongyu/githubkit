import json
from pathlib import Path
from typing import TypeVar

import httpx
import pytest

from githubkit import GitHub
from githubkit.versions.latest.models import FullRepository

T = TypeVar("T")


FAKE_RESPONSE = json.loads((Path(__file__).parent / "fake_response.json").read_text())


def target_sync_func(github: GitHub):
    resp = github.rest.repos.get("owner", "repo")
    return resp.parsed_data


def mock_transport_handler(request: httpx.Request) -> httpx.Response:
    if request.method == "GET" and request.url.path == "/repos/owner/repo":
        return httpx.Response(status_code=200, json=FAKE_RESPONSE)
    raise RuntimeError(f"Unexpected request: {request.method} {request.url.path}")


def test_sync_mock():
    g = GitHub("xxxxx", transport=httpx.MockTransport(mock_transport_handler))
    repo = target_sync_func(g)
    assert isinstance(repo, FullRepository)


async def target_async_func(github: GitHub):
    resp = await github.rest.repos.async_get("owner", "repo")
    return resp.parsed_data


@pytest.mark.anyio
async def test_async_mock():
    g = GitHub("xxxxx", async_transport=httpx.MockTransport(mock_transport_handler))
    repo = await target_async_func(g)
    assert isinstance(repo, FullRepository)
