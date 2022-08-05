from typing import TYPE_CHECKING, Any, Dict, List, Optional

if TYPE_CHECKING:
    from githubkit import GitHub


def create_device_code(
    github: "GitHub", client_id: str, scopes: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Create a device code for OAuth."""
    body = {"client_id": client_id}
    if scopes:
        body["scopes"] = " ".join(scopes)
    resp = github.request(
        "POST",
        "/login/device/code",
        json=body,
        headers={"Accept": "application/json"},
    )
    return resp.json()


async def async_create_device_code(
    github: "GitHub", client_id: str, scopes: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Create a device code for OAuth."""
    body = {"client_id": client_id}
    if scopes:
        body["scopes"] = " ".join(scopes)
    resp = await github.arequest(
        "POST",
        "/login/device/code",
        json=body,
        headers={"Accept": "application/json"},
    )
    return resp.json()
