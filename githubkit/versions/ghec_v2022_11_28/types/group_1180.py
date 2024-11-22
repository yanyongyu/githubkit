"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0102 import CodespaceMachineType


class UserCodespacesCodespaceNameMachinesGetResponse200Type(TypedDict):
    """UserCodespacesCodespaceNameMachinesGetResponse200"""

    total_count: int
    machines: list[CodespaceMachineType]


__all__ = ("UserCodespacesCodespaceNameMachinesGetResponse200Type",)
