"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0179 import CodespaceType


class ReposOwnerRepoCodespacesGetResponse200Type(TypedDict):
    """ReposOwnerRepoCodespacesGetResponse200"""

    total_count: int
    codespaces: list[CodespaceType]


__all__ = ("ReposOwnerRepoCodespacesGetResponse200Type",)
