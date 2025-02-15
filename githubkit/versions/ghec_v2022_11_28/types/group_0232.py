"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict


class PullRequestMinimalType(TypedDict):
    """Pull Request Minimal"""

    id: int
    number: int
    url: str
    head: PullRequestMinimalPropHeadType
    base: PullRequestMinimalPropBaseType


class PullRequestMinimalPropHeadType(TypedDict):
    """PullRequestMinimalPropHead"""

    ref: str
    sha: str
    repo: PullRequestMinimalPropHeadPropRepoType


class PullRequestMinimalPropHeadPropRepoType(TypedDict):
    """PullRequestMinimalPropHeadPropRepo"""

    id: int
    url: str
    name: str


class PullRequestMinimalPropBaseType(TypedDict):
    """PullRequestMinimalPropBase"""

    ref: str
    sha: str
    repo: PullRequestMinimalPropBasePropRepoType


class PullRequestMinimalPropBasePropRepoType(TypedDict):
    """PullRequestMinimalPropBasePropRepo"""

    id: int
    url: str
    name: str


__all__ = (
    "PullRequestMinimalPropBasePropRepoType",
    "PullRequestMinimalPropBaseType",
    "PullRequestMinimalPropHeadPropRepoType",
    "PullRequestMinimalPropHeadType",
    "PullRequestMinimalType",
)
