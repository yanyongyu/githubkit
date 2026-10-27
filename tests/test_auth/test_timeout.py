import pytest

from githubkit import GitHub, OAuthWebAuthStrategy
from githubkit._httpx import httpx


@pytest.mark.anyio
@pytest.mark.parametrize("async_client", [False, True])
@pytest.mark.parametrize("override", [False, True])
async def test_oauth_timeout(async_client: bool, override: bool):
    expected = {"connect": 1.0, "read": 2.0, "write": 3.0, "pool": 4.0}
    if override:
        expected = dict.fromkeys(expected, None)
    paths = []

    def handle(request: httpx.Request) -> httpx.Response:
        assert request.extensions["timeout"] == expected
        paths.append(request.url.path)
        if request.url.path == "/login/oauth/access_token":
            return httpx.Response(200, json={"access_token": "test-token"})
        assert request.headers["Authorization"] == "token test-token"
        return httpx.Response(200, json={"login": "test-user"})

    transport = httpx.MockTransport(handle)
    github = GitHub(
        OAuthWebAuthStrategy("client", "secret", "code"),
        timeout=httpx.Timeout(connect=1.0, read=2.0, write=3.0, pool=4.0),
        transport=transport,
        async_transport=transport,
        http_cache=False,
    )
    if async_client:
        async with github.get_async_client() as client:
            request = client.build_request("GET", "/user")
            if override:
                request.extensions["timeout"] = expected.copy()
            response = await client.send(request)
    else:
        with github.get_sync_client() as client:
            request = client.build_request("GET", "/user")
            if override:
                request.extensions["timeout"] = expected.copy()
            response = client.send(request)

    assert response.json() == {"login": "test-user"}
    assert paths == ["/login/oauth/access_token", "/user"]
