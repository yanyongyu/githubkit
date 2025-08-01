"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0341 import DeploymentBranchPolicySettingsType


class ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyType(TypedDict):
    """ReposOwnerRepoEnvironmentsEnvironmentNamePutBody"""

    wait_timer: NotRequired[int]
    prevent_self_review: NotRequired[bool]
    reviewers: NotRequired[
        Union[
            list[
                ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyPropReviewersItemsType
            ],
            None,
        ]
    ]
    deployment_branch_policy: NotRequired[
        Union[DeploymentBranchPolicySettingsType, None]
    ]


class ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyPropReviewersItemsType(TypedDict):
    """ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyPropReviewersItems"""

    type: NotRequired[Literal["User", "Team"]]
    id: NotRequired[int]


__all__ = (
    "ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyPropReviewersItemsType",
    "ReposOwnerRepoEnvironmentsEnvironmentNamePutBodyType",
)
