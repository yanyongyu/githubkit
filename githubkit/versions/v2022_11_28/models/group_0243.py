"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0200 import DiffEntry
from .group_0201 import Commit


class CommitComparison(GitHubModel):
    """Commit Comparison

    Commit Comparison
    """

    url: str = Field()
    html_url: str = Field()
    permalink_url: str = Field()
    diff_url: str = Field()
    patch_url: str = Field()
    base_commit: Commit = Field(title="Commit", description="Commit")
    merge_base_commit: Commit = Field(title="Commit", description="Commit")
    status: Literal["diverged", "ahead", "behind", "identical"] = Field()
    ahead_by: int = Field()
    behind_by: int = Field()
    total_commits: int = Field()
    commits: list[Commit] = Field()
    files: Missing[list[DiffEntry]] = Field(default=UNSET)


model_rebuild(CommitComparison)

__all__ = ("CommitComparison",)
