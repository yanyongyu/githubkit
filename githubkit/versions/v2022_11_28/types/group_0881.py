"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0080 import RunnerLabelType


class OrgsOrgActionsRunnersRunnerIdLabelsGetResponse200Type(TypedDict):
    """OrgsOrgActionsRunnersRunnerIdLabelsGetResponse200"""

    total_count: int
    labels: list[RunnerLabelType]


__all__ = ("OrgsOrgActionsRunnersRunnerIdLabelsGetResponse200Type",)
