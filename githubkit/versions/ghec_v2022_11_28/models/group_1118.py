"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class ReposOwnerRepoPagesDeploymentsPostBody(GitHubModel):
    """ReposOwnerRepoPagesDeploymentsPostBody

    The object used to create GitHub Pages deployment
    """

    artifact_id: Missing[float] = Field(
        default=UNSET,
        description="The ID of an artifact that contains the .zip or .tar of static assets to deploy. The artifact belongs to the repository. Either `artifact_id` or `artifact_url` are required.",
    )
    artifact_url: Missing[str] = Field(
        default=UNSET,
        description="The URL of an artifact that contains the .zip or .tar of static assets to deploy. The artifact belongs to the repository. Either `artifact_id` or `artifact_url` are required.",
    )
    environment: Missing[str] = Field(
        default=UNSET,
        description="The target environment for this GitHub Pages deployment.",
    )
    pages_build_version: str = Field(
        default="GITHUB_SHA",
        description="A unique string that represents the version of the build for this deployment.",
    )
    oidc_token: str = Field(
        description="The OIDC token issued by GitHub Actions certifying the origin of the deployment."
    )


model_rebuild(ReposOwnerRepoPagesDeploymentsPostBody)

__all__ = ("ReposOwnerRepoPagesDeploymentsPostBody",)
