"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoCommentsCommentIdReactionsPostBody(GitHubModel):
    """ReposOwnerRepoCommentsCommentIdReactionsPostBody"""

    content: Literal[
        "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
    ] = Field(
        description="The [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions) to add to the commit comment."
    )


model_rebuild(ReposOwnerRepoCommentsCommentIdReactionsPostBody)

__all__ = ("ReposOwnerRepoCommentsCommentIdReactionsPostBody",)
