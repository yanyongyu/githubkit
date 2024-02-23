"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict, NotRequired


class FileCommitType(TypedDict):
    """File Commit

    File Commit
    """

    content: Union[FileCommitPropContentType, None]
    commit: FileCommitPropCommitType


class FileCommitPropContentType(TypedDict):
    """FileCommitPropContent"""

    name: NotRequired[str]
    path: NotRequired[str]
    sha: NotRequired[str]
    size: NotRequired[int]
    url: NotRequired[str]
    html_url: NotRequired[str]
    git_url: NotRequired[str]
    download_url: NotRequired[str]
    type: NotRequired[str]
    links: NotRequired[FileCommitPropContentPropLinksType]


class FileCommitPropContentPropLinksType(TypedDict):
    """FileCommitPropContentPropLinks"""

    self_: NotRequired[str]
    git: NotRequired[str]
    html: NotRequired[str]


class FileCommitPropCommitType(TypedDict):
    """FileCommitPropCommit"""

    sha: NotRequired[str]
    node_id: NotRequired[str]
    url: NotRequired[str]
    html_url: NotRequired[str]
    author: NotRequired[FileCommitPropCommitPropAuthorType]
    committer: NotRequired[FileCommitPropCommitPropCommitterType]
    message: NotRequired[str]
    tree: NotRequired[FileCommitPropCommitPropTreeType]
    parents: NotRequired[List[FileCommitPropCommitPropParentsItemsType]]
    verification: NotRequired[FileCommitPropCommitPropVerificationType]


class FileCommitPropCommitPropAuthorType(TypedDict):
    """FileCommitPropCommitPropAuthor"""

    date: NotRequired[str]
    name: NotRequired[str]
    email: NotRequired[str]


class FileCommitPropCommitPropCommitterType(TypedDict):
    """FileCommitPropCommitPropCommitter"""

    date: NotRequired[str]
    name: NotRequired[str]
    email: NotRequired[str]


class FileCommitPropCommitPropTreeType(TypedDict):
    """FileCommitPropCommitPropTree"""

    url: NotRequired[str]
    sha: NotRequired[str]


class FileCommitPropCommitPropParentsItemsType(TypedDict):
    """FileCommitPropCommitPropParentsItems"""

    url: NotRequired[str]
    html_url: NotRequired[str]
    sha: NotRequired[str]


class FileCommitPropCommitPropVerificationType(TypedDict):
    """FileCommitPropCommitPropVerification"""

    verified: NotRequired[bool]
    reason: NotRequired[str]
    signature: NotRequired[Union[str, None]]
    payload: NotRequired[Union[str, None]]


__all__ = (
    "FileCommitType",
    "FileCommitPropContentType",
    "FileCommitPropContentPropLinksType",
    "FileCommitPropCommitType",
    "FileCommitPropCommitPropAuthorType",
    "FileCommitPropCommitPropCommitterType",
    "FileCommitPropCommitPropTreeType",
    "FileCommitPropCommitPropParentsItemsType",
    "FileCommitPropCommitPropVerificationType",
)
