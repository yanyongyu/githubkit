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


class RepositoryRuleOneof18(GitHubModel):
    """max_file_size

    Prevent commits that exceed a specified file size limit from being pushed to the
    commit graph.
    """

    type: Literal["max_file_size"] = Field()
    parameters: Missing[RepositoryRuleOneof18PropParameters] = Field(default=UNSET)


class RepositoryRuleOneof18PropParameters(GitHubModel):
    """RepositoryRuleOneof18PropParameters"""

    max_file_size: int = Field(
        le=100.0,
        ge=1.0,
        description="The maximum file size allowed in megabytes. This limit does not apply to Git Large File Storage (Git LFS).",
    )


model_rebuild(RepositoryRuleOneof18)
model_rebuild(RepositoryRuleOneof18PropParameters)

__all__ = (
    "RepositoryRuleOneof18",
    "RepositoryRuleOneof18PropParameters",
)
