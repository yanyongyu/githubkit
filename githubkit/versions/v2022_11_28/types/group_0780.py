"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired

from .group_0019 import RepositoryType


class InstallationRepositoriesGetResponse200Type(TypedDict):
    """InstallationRepositoriesGetResponse200"""

    total_count: int
    repositories: List[RepositoryType]
    repository_selection: NotRequired[str]


__all__ = ("InstallationRepositoriesGetResponse200Type",)
