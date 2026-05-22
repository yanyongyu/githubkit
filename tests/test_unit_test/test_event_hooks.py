import json
from pathlib import Path

from githubkit_schemas.latest.models import FullRepository
import httpx
import pytest

from githubkit import GitHub

FAKE_RESPONSE = json.loads((Path(__file__).parent / "fake_response.json").read_text())


def mock_transport_handler(request: httpx.Request) -> httpx.Response:
    if request.method == "GET" and request.url.path == "/repos/owner/repo":
        return httpx.Response(status_code=200, json=FAKE_RESPONSE)
    raise RuntimeError(f"Unexpected request: {request.method} {request.url.path}")


def test_sync_event_hooks():
    requests_seen: list[httpx.Request] = []
    responses_seen: list[httpx.Response] = []

    def on_request(request: httpx.Request) -> None:
        requests_seen.append(request)

    def on_response(response: httpx.Response) -> None:
        responses_seen.append(response)

    g = GitHub(
        "xxxxx",
        transport=httpx.MockTransport(mock_transport_handler),
        event_hooks={
            "request": [on_request],
            "response": [on_response],
        },
    )
    resp = g.rest.repos.get("owner", "repo")
    assert isinstance(resp.parsed_data, FullRepository)
    assert len(requests_seen) == 1
    assert len(responses_seen) == 1
    assert requests_seen[0].url.path == "/repos/owner/repo"
    assert responses_seen[0].status_code == 200


@pytest.mark.anyio
async def test_async_event_hooks():
    requests_seen: list[httpx.Request] = []
    responses_seen: list[httpx.Response] = []

    async def on_request(request: httpx.Request) -> None:
        requests_seen.append(request)

    async def on_response(response: httpx.Response) -> None:
        responses_seen.append(response)

    g = GitHub(
        "xxxxx",
        async_transport=httpx.MockTransport(mock_transport_handler),
        async_event_hooks={
            "request": [on_request],
            "response": [on_response],
        },
    )
    resp = await g.rest.repos.async_get("owner", "repo")
    assert isinstance(resp.parsed_data, FullRepository)
    assert len(requests_seen) == 1
    assert len(responses_seen) == 1
    assert requests_seen[0].url.path == "/repos/owner/repo"
    assert responses_seen[0].status_code == 200
