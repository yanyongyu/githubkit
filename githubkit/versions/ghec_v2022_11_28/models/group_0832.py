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


class EnterprisesEnterpriseActionsRunnerGroupsGetResponse200(GitHubModel):
    """EnterprisesEnterpriseActionsRunnerGroupsGetResponse200"""

    total_count: float = Field()
    runner_groups: list[RunnerGroupsEnterprise] = Field()


class RunnerGroupsEnterprise(GitHubModel):
    """RunnerGroupsEnterprise"""

    id: float = Field()
    name: str = Field()
    visibility: str = Field()
    default: bool = Field()
    selected_organizations_url: Missing[str] = Field(default=UNSET)
    runners_url: str = Field()
    hosted_runners_url: Missing[str] = Field(default=UNSET)
    allows_public_repositories: bool = Field()
    workflow_restrictions_read_only: Missing[bool] = Field(
        default=UNSET,
        description="If `true`, the `restricted_to_workflows` and `selected_workflows` fields cannot be modified.",
    )
    restricted_to_workflows: Missing[bool] = Field(
        default=UNSET,
        description="If `true`, the runner group will be restricted to running only the workflows specified in the `selected_workflows` array.",
    )
    selected_workflows: Missing[list[str]] = Field(
        default=UNSET,
        description="List of workflows the runner group should be allowed to run. This setting will be ignored unless `restricted_to_workflows` is set to `true`.",
    )


model_rebuild(EnterprisesEnterpriseActionsRunnerGroupsGetResponse200)
model_rebuild(RunnerGroupsEnterprise)

__all__ = (
    "EnterprisesEnterpriseActionsRunnerGroupsGetResponse200",
    "RunnerGroupsEnterprise",
)
