"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0001 import SimpleUser


class EnvironmentApprovals(GitHubModel):
    """Environment Approval

    An entry in the reviews log for environment deployments
    """

    environments: List[EnvironmentApprovalsPropEnvironmentsItems] = Field(
        description="The list of environments that were approved or rejected"
    )
    state: Literal["approved", "rejected", "pending"] = Field(
        description="Whether deployment to the environment(s) was approved or rejected or pending (with comments)"
    )
    user: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    comment: str = Field(description="The comment submitted with the deployment review")


class EnvironmentApprovalsPropEnvironmentsItems(GitHubModel):
    """EnvironmentApprovalsPropEnvironmentsItems"""

    id: Missing[int] = Field(default=UNSET, description="The id of the environment.")
    node_id: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(
        default=UNSET, description="The name of the environment."
    )
    url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    created_at: Missing[datetime] = Field(
        default=UNSET,
        description="The time that the environment was created, in ISO 8601 format.",
    )
    updated_at: Missing[datetime] = Field(
        default=UNSET,
        description="The time that the environment was last updated, in ISO 8601 format.",
    )


model_rebuild(EnvironmentApprovals)
model_rebuild(EnvironmentApprovalsPropEnvironmentsItems)

__all__ = (
    "EnvironmentApprovals",
    "EnvironmentApprovalsPropEnvironmentsItems",
)
