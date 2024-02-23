"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoPagesDeploymentsPostBodyType(TypedDict):
    """ReposOwnerRepoPagesDeploymentsPostBody

    The object used to create GitHub Pages deployment
    """

    artifact_id: NotRequired[float]
    artifact_url: NotRequired[str]
    environment: NotRequired[str]
    pages_build_version: str
    oidc_token: str


__all__ = ("ReposOwnerRepoPagesDeploymentsPostBodyType",)
