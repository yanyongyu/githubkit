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


class ReposOwnerRepoGitBlobsPostBody(GitHubModel):
    """ReposOwnerRepoGitBlobsPostBody"""

    content: str = Field(description="The new blob's content.")
    encoding: Missing[str] = Field(
        default=UNSET,
        description='The encoding used for `content`. Currently, `"utf-8"` and `"base64"` are supported.',
    )


model_rebuild(ReposOwnerRepoGitBlobsPostBody)

__all__ = ("ReposOwnerRepoGitBlobsPostBody",)
