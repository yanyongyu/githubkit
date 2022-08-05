from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from githubkit import GitHub


def exchange_web_flow_code(
    github: "GitHub",
    client_id: str,
    client_secret: str,
    code: str,
    redirect_uri: Optional[str] = None,
) -> Dict[str, Any]:
    """Exchange web flow code for token."""
    body = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
    }
    if redirect_uri:
        body["redirect_uri"] = redirect_uri
    resp = github.request(
        "POST",
        "/login/oauth/access_token",
        json=body,
        headers={"Accept": "application/json"},
    )
    return resp.json()


async def async_exchange_web_flow_code(
    github: "GitHub",
    client_id: str,
    client_secret: str,
    code: str,
    redirect_uri: Optional[str] = None,
) -> Dict[str, Any]:
    """Exchange web flow code for token."""
    body = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
    }
    if redirect_uri:
        body["redirect_uri"] = redirect_uri
    resp = await github.arequest(
        "POST",
        "/login/oauth/access_token",
        json=body,
        headers={"Accept": "application/json"},
    )
    return resp.json()
