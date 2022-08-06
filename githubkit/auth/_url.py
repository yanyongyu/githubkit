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
APP_AUTH_REGEX = re.compile(rf"(?:{'|'.join(APP_ROUTES)})[^/]*$", re.I)


def require_bypass(url: httpx.URL) -> bool:
    # bypass oauth web flow and device flow
    return bool(BYPASS_REGEX.search(url.path))


def require_app_auth(url: httpx.URL) -> bool:
    return bool(APP_AUTH_REGEX.search(url.path))
