"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoCommentsCommentIdPatchBody(GitHubModel):
    """ReposOwnerRepoCommentsCommentIdPatchBody"""

    body: str = Field(description="The contents of the comment")


model_rebuild(ReposOwnerRepoCommentsCommentIdPatchBody)

__all__ = ("ReposOwnerRepoCommentsCommentIdPatchBody",)
