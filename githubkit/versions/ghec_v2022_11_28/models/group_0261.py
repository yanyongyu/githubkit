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

from .group_0260 import BranchProtection


class ShortBranch(GitHubModel):
    """Short Branch

    Short Branch
    """

    name: str = Field()
    commit: ShortBranchPropCommit = Field()
    protected: bool = Field()
    protection: Missing[BranchProtection] = Field(
        default=UNSET, title="Branch Protection", description="Branch Protection"
    )
    protection_url: Missing[str] = Field(default=UNSET)


class ShortBranchPropCommit(GitHubModel):
    """ShortBranchPropCommit"""

    sha: str = Field()
    url: str = Field()


model_rebuild(ShortBranch)
model_rebuild(ShortBranchPropCommit)

__all__ = (
    "ShortBranch",
    "ShortBranchPropCommit",
)
