"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0020 import RepositoryType


class OrgsOrgActionsPermissionsRepositoriesGetResponse200Type(TypedDict):
    """OrgsOrgActionsPermissionsRepositoriesGetResponse200"""

    total_count: float
    repositories: list[RepositoryType]


__all__ = ("OrgsOrgActionsPermissionsRepositoriesGetResponse200Type",)
