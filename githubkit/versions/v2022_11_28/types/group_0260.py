"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0214 import DiffEntryType
from .group_0215 import CommitType


class CommitComparisonType(TypedDict):
    """Commit Comparison

    Commit Comparison
    """

    url: str
    html_url: str
    permalink_url: str
    diff_url: str
    patch_url: str
    base_commit: CommitType
    merge_base_commit: CommitType
    status: Literal["diverged", "ahead", "behind", "identical"]
    ahead_by: int
    behind_by: int
    total_commits: int
    commits: list[CommitType]
    files: NotRequired[list[DiffEntryType]]


__all__ = ("CommitComparisonType",)
