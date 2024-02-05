"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0161 import WorkflowRun


class ReposOwnerRepoActionsRunsGetResponse200(GitHubModel):
    """ReposOwnerRepoActionsRunsGetResponse200"""

    total_count: int = Field()
    workflow_runs: List[WorkflowRun] = Field()


model_rebuild(ReposOwnerRepoActionsRunsGetResponse200)

__all__ = ("ReposOwnerRepoActionsRunsGetResponse200",)
