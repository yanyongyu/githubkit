"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0245 import WorkflowRun


class ReposOwnerRepoActionsWorkflowsWorkflowIdRunsGetResponse200(GitHubModel):
    """ReposOwnerRepoActionsWorkflowsWorkflowIdRunsGetResponse200"""

    total_count: int = Field()
    workflow_runs: list[WorkflowRun] = Field()


model_rebuild(ReposOwnerRepoActionsWorkflowsWorkflowIdRunsGetResponse200)

__all__ = ("ReposOwnerRepoActionsWorkflowsWorkflowIdRunsGetResponse200",)
