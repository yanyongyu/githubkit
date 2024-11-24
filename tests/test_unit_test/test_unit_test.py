import json
from pathlib import Path
from typing import Any, TypeVar, Union

import httpx
import pytest

from githubkit import GitHub
from githubkit.response import Response
from githubkit.typing import UnsetType, URLTypes
from githubkit.utils import UNSET
from githubkit.versions.latest.models import FullRepository

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
    response_model: Union[type[T], UnsetType] = UNSET,
    **kwargs: Any,
) -> Response[Any]:
    if method == "GET" and url == "/repos/owner/repo":
        return Response[T](
            httpx.Response(status_code=200, json=FAKE_RESPONSE),
            Any if response_model is UNSET else response_model,
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
    response_model: Union[type[T], UnsetType] = UNSET,
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
