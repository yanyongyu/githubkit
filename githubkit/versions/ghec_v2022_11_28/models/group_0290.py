"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0289 import DeploymentBranchPolicySettings
from .group_0291 import EnvironmentPropProtectionRulesItemsAnyof1


class Environment(GitHubModel):
    """Environment

    Details of a deployment environment
    """

    id: int = Field(description="The id of the environment.")
    node_id: str = Field()
    name: str = Field(description="The name of the environment.")
    url: str = Field()
    html_url: str = Field()
    created_at: datetime = Field(
        description="The time that the environment was created, in ISO 8601 format."
    )
    updated_at: datetime = Field(
        description="The time that the environment was last updated, in ISO 8601 format."
    )
    protection_rules: Missing[
        list[
            Union[
                EnvironmentPropProtectionRulesItemsAnyof0,
                EnvironmentPropProtectionRulesItemsAnyof1,
                EnvironmentPropProtectionRulesItemsAnyof2,
            ]
        ]
    ] = Field(
        default=UNSET,
        description="Built-in deployment protection rules for the environment.",
    )
    deployment_branch_policy: Missing[Union[DeploymentBranchPolicySettings, None]] = (
        Field(
            default=UNSET,
            description="The type of deployment branch policy for this environment. To allow all branches to deploy, set to `null`.",
        )
    )


class EnvironmentPropProtectionRulesItemsAnyof0(GitHubModel):
    """EnvironmentPropProtectionRulesItemsAnyof0"""

    id: int = Field()
    node_id: str = Field()
    type: str = Field()
    wait_timer: Missing[int] = Field(
        default=UNSET,
        description="The amount of time to delay a job after the job is initially triggered. The time (in minutes) must be an integer between 0 and 43,200 (30 days).",
    )


class EnvironmentPropProtectionRulesItemsAnyof2(GitHubModel):
    """EnvironmentPropProtectionRulesItemsAnyof2"""

    id: int = Field()
    node_id: str = Field()
    type: str = Field()


class ReposOwnerRepoEnvironmentsGetResponse200(GitHubModel):
    """ReposOwnerRepoEnvironmentsGetResponse200"""

    total_count: Missing[int] = Field(
        default=UNSET, description="The number of environments in this repository"
    )
    environments: Missing[list[Environment]] = Field(default=UNSET)


model_rebuild(Environment)
model_rebuild(EnvironmentPropProtectionRulesItemsAnyof0)
model_rebuild(EnvironmentPropProtectionRulesItemsAnyof2)
model_rebuild(ReposOwnerRepoEnvironmentsGetResponse200)

__all__ = (
    "Environment",
    "EnvironmentPropProtectionRulesItemsAnyof0",
    "EnvironmentPropProtectionRulesItemsAnyof2",
    "ReposOwnerRepoEnvironmentsGetResponse200",
)
