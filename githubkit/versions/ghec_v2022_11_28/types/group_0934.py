"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0041 import RunnerType


class OrgsOrgActionsRunnersGetResponse200Type(TypedDict):
    """OrgsOrgActionsRunnersGetResponse200"""

    total_count: int
    runners: list[RunnerType]


__all__ = ("OrgsOrgActionsRunnersGetResponse200Type",)
