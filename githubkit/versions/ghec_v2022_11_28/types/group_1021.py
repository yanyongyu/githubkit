"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .group_0181 import WorkflowRunType


class ReposOwnerRepoActionsWorkflowsWorkflowIdRunsGetResponse200Type(TypedDict):
    """ReposOwnerRepoActionsWorkflowsWorkflowIdRunsGetResponse200"""

    total_count: int
    workflow_runs: List[WorkflowRunType]


__all__ = ("ReposOwnerRepoActionsWorkflowsWorkflowIdRunsGetResponse200Type",)
