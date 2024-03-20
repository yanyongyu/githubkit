"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0201 import CommitType
from .group_0200 import DiffEntryType


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
    commits: List[CommitType]
    files: NotRequired[List[DiffEntryType]]


__all__ = ("CommitComparisonType",)
