"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0073 import ActionsHostedRunnerImageType


class OrgsOrgActionsHostedRunnersImagesPartnerGetResponse200Type(TypedDict):
    """OrgsOrgActionsHostedRunnersImagesPartnerGetResponse200"""

    total_count: int
    images: list[ActionsHostedRunnerImageType]


__all__ = ("OrgsOrgActionsHostedRunnersImagesPartnerGetResponse200Type",)
