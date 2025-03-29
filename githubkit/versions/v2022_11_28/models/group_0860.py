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


class OrgsOrgActionsRunnerGroupsPostBody(GitHubModel):
    """OrgsOrgActionsRunnerGroupsPostBody"""

    name: str = Field(description="Name of the runner group.")
    visibility: Missing[Literal["selected", "all", "private"]] = Field(
        default=UNSET,
        description="Visibility of a runner group. You can select all repositories, select individual repositories, or limit access to private repositories.",
    )
    selected_repository_ids: Missing[list[int]] = Field(
        default=UNSET,
        description="List of repository IDs that can access the runner group.",
    )
    runners: Missing[list[int]] = Field(
        default=UNSET, description="List of runner IDs to add to the runner group."
    )
    allows_public_repositories: Missing[bool] = Field(
        default=UNSET,
        description="Whether the runner group can be used by `public` repositories.",
    )
    restricted_to_workflows: Missing[bool] = Field(
        default=UNSET,
        description="If `true`, the runner group will be restricted to running only the workflows specified in the `selected_workflows` array.",
    )
    selected_workflows: Missing[list[str]] = Field(
        default=UNSET,
        description="List of workflows the runner group should be allowed to run. This setting will be ignored unless `restricted_to_workflows` is set to `true`.",
    )
    network_configuration_id: Missing[str] = Field(
        default=UNSET,
        description="The identifier of a hosted compute network configuration.",
    )


model_rebuild(OrgsOrgActionsRunnerGroupsPostBody)

__all__ = ("OrgsOrgActionsRunnerGroupsPostBody",)
