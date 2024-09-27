"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0193 import Commit
from .group_0188 import BranchProtection


class BranchWithProtection(GitHubModel):
    """Branch With Protection

    Branch With Protection
    """

    name: str = Field()
    commit: Commit = Field(title="Commit", description="Commit")
    links: BranchWithProtectionPropLinks = Field(alias="_links")
    protected: bool = Field()
    protection: BranchProtection = Field(
        title="Branch Protection", description="Branch Protection"
    )
    protection_url: str = Field()
    pattern: Missing[str] = Field(default=UNSET)
    required_approving_review_count: Missing[int] = Field(default=UNSET)


class BranchWithProtectionPropLinks(GitHubModel):
    """BranchWithProtectionPropLinks"""

    html: str = Field()
    self_: str = Field(alias="self")


model_rebuild(BranchWithProtection)
model_rebuild(BranchWithProtectionPropLinks)

__all__ = (
    "BranchWithProtection",
    "BranchWithProtectionPropLinks",
)
