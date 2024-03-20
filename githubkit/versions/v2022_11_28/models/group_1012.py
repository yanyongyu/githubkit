"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0234 import DeploymentBranchPolicySettings


class ReposOwnerRepoEnvironmentsEnvironmentNamePutBody(GitHubModel):
    """ReposOwnerRepoEnvironmentsEnvironmentNamePutBody"""

    wait_timer: Missing[int] = Field(
        default=UNSET,
        description="The amount of time to delay a job after the job is initially triggered. The time (in minutes) must be an integer between 0 and 43,200 (30 days).",
    )
    prevent_self_review: Missing[bool] = Field(
        default=UNSET,
        description="Whether or not a user who created the job is prevented from approving their own job.",
    )
    reviewers: Missing[
        Union[
            List[ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyPropReviewersItems],
            None,
        ]
    ] = Field(
        default=UNSET,
        description="The people or teams that may review jobs that reference the environment. You can list up to six users or teams as reviewers. The reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve the job for it to proceed.",
    )
    deployment_branch_policy: Missing[
        Union[DeploymentBranchPolicySettings, None]
    ] = Field(
        default=UNSET,
        description="The type of deployment branch policy for this environment. To allow all branches to deploy, set to `null`.",
    )


class ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyPropReviewersItems(GitHubModel):
    """ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyPropReviewersItems"""

    type: Missing[Literal["User", "Team"]] = Field(
        default=UNSET, description="The type of reviewer."
    )
    id: Missing[int] = Field(
        default=UNSET,
        description="The id of the user or team who can review the deployment",
    )


model_rebuild(ReposOwnerRepoEnvironmentsEnvironmentNamePutBody)
model_rebuild(ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyPropReviewersItems)

__all__ = (
    "ReposOwnerRepoEnvironmentsEnvironmentNamePutBody",
    "ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyPropReviewersItems",
)
