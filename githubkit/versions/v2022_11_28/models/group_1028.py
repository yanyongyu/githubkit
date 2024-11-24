"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoMergeUpstreamPostBody(GitHubModel):
    """ReposOwnerRepoMergeUpstreamPostBody"""

    branch: str = Field(
        description="The name of the branch which should be updated to match upstream."
    )


model_rebuild(ReposOwnerRepoMergeUpstreamPostBody)

__all__ = ("ReposOwnerRepoMergeUpstreamPostBody",)
