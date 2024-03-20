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


class ReposOwnerRepoMergesPostBody(GitHubModel):
    """ReposOwnerRepoMergesPostBody"""

    base: str = Field(
        description="The name of the base branch that the head will be merged into."
    )
    head: str = Field(
        description="The head to merge. This can be a branch name or a commit SHA1."
    )
    commit_message: Missing[str] = Field(
        default=UNSET,
        description="Commit message to use for the merge commit. If omitted, a default message will be used.",
    )


model_rebuild(ReposOwnerRepoMergesPostBody)

__all__ = ("ReposOwnerRepoMergesPostBody",)
