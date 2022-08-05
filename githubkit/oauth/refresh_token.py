from typing import TYPE_CHECKING, Any, Dict

if TYPE_CHECKING:
    from githubkit import GitHub


def refresh_token(
    github: "GitHub", client_id: str, client_secret: str, refresh_token: str
) -> Dict[str, Any]:
    """Refresh token."""
    resp = github.request(
        "POST",
        "/login/oauth/access_token",
        json={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        },
        headers={"Accept": "application/json"},
    )
    return resp.json()


async def async_refresh_token(
    github: "GitHub", client_id: str, client_secret: str, refresh_token: str
) -> Dict[str, Any]:
    """Refresh token."""
    resp = await github.arequest(
        "POST",
        "/login/oauth/access_token",
        json={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        },
        headers={"Accept": "application/json"},
    )
    return resp.json()
