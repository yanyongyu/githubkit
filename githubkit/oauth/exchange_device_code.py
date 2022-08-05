from typing import TYPE_CHECKING, Any, Dict

if TYPE_CHECKING:
    from githubkit import GitHub


def exchange_device_code(
    github: "GitHub", client_id: str, device_code: str
) -> Dict[str, Any]:
    """Exchange device code for token."""
    resp = github.request(
        "POST",
        "/login/oauth/access_token",
        json={
            "client_id": client_id,
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            "device_code": device_code,
        },
        headers={"Accept": "application/json"},
    )
    return resp.json()


async def async_exchange_device_code(
    github: "GitHub", client_id: str, device_code: str
) -> Dict[str, Any]:
    """Exchange device code for token."""
    resp = await github.arequest(
        "POST",
        "/login/oauth/access_token",
        json={
            "client_id": client_id,
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            "device_code": device_code,
        },
        headers={"Accept": "application/json"},
    )
    return resp.json()
