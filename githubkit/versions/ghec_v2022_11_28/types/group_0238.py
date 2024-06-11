"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict


class BranchShortType(TypedDict):
    """Branch Short

    Branch Short
    """

    name: str
    commit: BranchShortPropCommitType
    protected: bool


class BranchShortPropCommitType(TypedDict):
    """BranchShortPropCommit"""

    sha: str
    url: str


__all__ = (
    "BranchShortType",
    "BranchShortPropCommitType",
)
