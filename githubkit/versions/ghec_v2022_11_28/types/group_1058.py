"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0224 import ActionsVariableType


class ReposOwnerRepoActionsVariablesGetResponse200Type(TypedDict):
    """ReposOwnerRepoActionsVariablesGetResponse200"""

    total_count: int
    variables: list[ActionsVariableType]


__all__ = ("ReposOwnerRepoActionsVariablesGetResponse200Type",)
