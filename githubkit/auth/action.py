import os
from typing import TYPE_CHECKING, Generator

import httpx

from githubkit.exception import AuthCredentialError

from .base import BaseAuthStrategy

if TYPE_CHECKING:
    from githubkit import GitHubCore


class ActionAuth(httpx.Auth):
    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        token = os.environ.get("GITHUB_TOKEN", os.environ.get("INPUT_GITHUB_TOKEN"))
        if not token:
            raise AuthCredentialError(
                "`GITHUB_TOKEN` is not provided. Use `env:` or `with:` to input a token."
            )
        request.headers["Authorization"] = f"token {token}"
        yield request


class ActionAuthStrategy(BaseAuthStrategy):
    def get_auth_flow(self, github: "GitHubCore") -> httpx.Auth:
        return ActionAuth()
