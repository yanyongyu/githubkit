"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0066 import ActionsHostedRunnerType


class OrgsOrgActionsHostedRunnersGetResponse200Type(TypedDict):
    """OrgsOrgActionsHostedRunnersGetResponse200"""

    total_count: int
    runners: list[ActionsHostedRunnerType]


__all__ = ("OrgsOrgActionsHostedRunnersGetResponse200Type",)
