"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0182 import WorkflowRunType


class ReposOwnerRepoActionsRunsGetResponse200Type(TypedDict):
    """ReposOwnerRepoActionsRunsGetResponse200"""

    total_count: int
    workflow_runs: list[WorkflowRunType]


__all__ = ("ReposOwnerRepoActionsRunsGetResponse200Type",)
