from typing import TYPE_CHECKING

import httpx

from .base import BaseAuthStrategy

if TYPE_CHECKING:
    from githubkit import GitHub


class UnauthAuthStrategy(BaseAuthStrategy):
    """Unauthenticated GitHubKit"""

    def get_auth_flow(self, github: "GitHub") -> httpx.Auth:
        return httpx.Auth()
