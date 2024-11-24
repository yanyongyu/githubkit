"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import TypedDict


class GitCommitType(TypedDict):
    """Git Commit

    Low-level Git commit operations within a repository
    """

    sha: str
    node_id: str
    url: str
    author: GitCommitPropAuthorType
    committer: GitCommitPropCommitterType
    message: str
    tree: GitCommitPropTreeType
    parents: list[GitCommitPropParentsItemsType]
    verification: GitCommitPropVerificationType
    html_url: str


class GitCommitPropAuthorType(TypedDict):
    """GitCommitPropAuthor

    Identifying information for the git-user
    """

    date: datetime
    email: str
    name: str


class GitCommitPropCommitterType(TypedDict):
    """GitCommitPropCommitter

    Identifying information for the git-user
    """

    date: datetime
    email: str
    name: str


class GitCommitPropTreeType(TypedDict):
    """GitCommitPropTree"""

    sha: str
    url: str


class GitCommitPropParentsItemsType(TypedDict):
    """GitCommitPropParentsItems"""

    sha: str
    url: str
    html_url: str


class GitCommitPropVerificationType(TypedDict):
    """GitCommitPropVerification"""

    verified: bool
    reason: str
    signature: Union[str, None]
    payload: Union[str, None]


__all__ = (
    "GitCommitPropAuthorType",
    "GitCommitPropCommitterType",
    "GitCommitPropParentsItemsType",
    "GitCommitPropTreeType",
    "GitCommitPropVerificationType",
    "GitCommitType",
)
