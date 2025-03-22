"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class ReposOwnerRepoForksPostBody(GitHubModel):
    """ReposOwnerRepoForksPostBody"""

    organization: Missing[str] = Field(
        default=UNSET,
        description="Optional parameter to specify the organization name if forking into an organization.",
    )
    name: Missing[str] = Field(
        default=UNSET,
        description="When forking from an existing repository, a new name for the fork.",
    )
    default_branch_only: Missing[bool] = Field(
        default=UNSET,
        description="When forking from an existing repository, fork with only the default branch.",
    )


model_rebuild(ReposOwnerRepoForksPostBody)

__all__ = ("ReposOwnerRepoForksPostBody",)
