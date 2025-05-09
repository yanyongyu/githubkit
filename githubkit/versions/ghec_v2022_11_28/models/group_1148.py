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


class ReposOwnerRepoCommitsCommitShaCommentsPostBody(GitHubModel):
    """ReposOwnerRepoCommitsCommitShaCommentsPostBody"""

    body: str = Field(description="The contents of the comment.")
    path: Missing[str] = Field(
        default=UNSET, description="Relative path of the file to comment on."
    )
    position: Missing[int] = Field(
        default=UNSET, description="Line index in the diff to comment on."
    )
    line: Missing[int] = Field(
        default=UNSET,
        description="**Closing down notice**. Use **position** parameter instead. Line number in the file to comment on.",
    )


model_rebuild(ReposOwnerRepoCommitsCommitShaCommentsPostBody)

__all__ = ("ReposOwnerRepoCommitsCommitShaCommentsPostBody",)
