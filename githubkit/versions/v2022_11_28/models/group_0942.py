"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoActionsRunnersGenerateJitconfigPostBody(GitHubModel):
    """ReposOwnerRepoActionsRunnersGenerateJitconfigPostBody"""

    name: str = Field(description="The name of the new runner.")
    runner_group_id: int = Field(
        description="The ID of the runner group to register the runner to."
    )
    labels: List[str] = Field(
        max_length=100,
        min_length=1,
        description="The names of the custom labels to add to the runner. **Minimum items**: 1. **Maximum items**: 100.",
    )
    work_folder: Missing[str] = Field(
        default=UNSET,
        description="The working directory to be used for job execution, relative to the runner install directory.",
    )


model_rebuild(ReposOwnerRepoActionsRunnersGenerateJitconfigPostBody)

__all__ = ("ReposOwnerRepoActionsRunnersGenerateJitconfigPostBody",)
