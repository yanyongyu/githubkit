import re

import httpx

APP_ROUTES = {
    r"/app",
    r"/app/hook/config",
    r"/app/hook/deliveries",
    r"/app/hook/deliveries/(?:.+?)",
    r"/app/hook/deliveries/(?:.+?)/attempts",
    r"/app/installations",
    r"/app/installations/(?:.+?)",
    r"/app/installations/(?:.+?)/access_tokens",
    r"/app/installations/(?:.+?)/suspended",
    r"/app/installation-requests",
    r"/marketplace_listing/accounts/(?:.+?)",
    r"/marketplace_listing/plan",
    r"/marketplace_listing/plans",
    r"/marketplace_listing/plans/(?:.+?)/accounts",
    r"/marketplace_listing/stubbed/accounts/(?:.+?)",
    r"/marketplace_listing/stubbed/plan",
    r"/marketplace_listing/stubbed/plans",
    r"/marketplace_listing/stubbed/plans/(?:.+?)/accounts",
    r"/orgs/(?:.+?)/installation",
    r"/repos/(?:.+?)/(?:.+?)/installation",
    r"/users/(?:.+?)/installation",
}

BYPASS_REGEX = re.compile(r"/login/(oauth/access_token|device/code)$")
"""Regex to match routes that should bypass auth.

See: https://github.com/octokit/auth-oauth-user.js/blob/b8b1141b21f285027e36a4a1670163e4db51d30f/src/hook.ts#L44
"""
APP_AUTH_REGEX = re.compile(rf"^(?:{'|'.join(APP_ROUTES)})$", re.I)
"""Regex to match app authentication routes.

See: https://github.com/octokit/auth-app.js/blob/9da834e0d8893b4cb233a2e9f67c3183abe8a341/src/requires-app-auth.ts#L46
"""
BASIC_AUTH_REGEX = re.compile(r"/applications/[^/]+/(token|grant)s?")
"""Regex to match basic authentication routes.

See: https://github.com/octokit/auth-oauth-user.js/blob/b8b1141b21f285027e36a4a1670163e4db51d30f/src/requires-basic-auth.ts#L17
"""
OAUTH_BASE_REGEX = re.compile(r"^https://(api\.)?github\.com/?$")


def require_bypass(url: httpx.URL) -> bool:
    """Check if the request should bypass auth."""
    return bool(BYPASS_REGEX.search(url.path))


def require_app_auth(url: httpx.URL) -> bool:
    """Check if the request should use app authentication.

    Note: the input url must remove the base url first.
    """
    return bool(APP_AUTH_REGEX.search(url.path))


def require_basic_auth(url: httpx.URL) -> bool:
    """Check if the request should use basic authentication."""
    return bool(BASIC_AUTH_REGEX.search(url.path))


def get_oauth_base_url(base_url: httpx.URL) -> httpx.URL:
    if OAUTH_BASE_REGEX.match(str(base_url)):
        return httpx.URL("https://github.com/")
    else:
        return base_url.copy_with(raw_path=b"/")
