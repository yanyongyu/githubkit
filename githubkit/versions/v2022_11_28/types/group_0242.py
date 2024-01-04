"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class GitTreeType(TypedDict):
    """Git Tree

    The hierarchy between files in a Git repository.
    """

    sha: str
    url: str
    truncated: bool
    tree: List[GitTreePropTreeItemsType]


class GitTreePropTreeItemsType(TypedDict):
    """GitTreePropTreeItems"""

    path: NotRequired[str]
    mode: NotRequired[str]
    type: NotRequired[str]
    sha: NotRequired[str]
    size: NotRequired[int]
    url: NotRequired[str]


__all__ = (
    "GitTreeType",
    "GitTreePropTreeItemsType",
)
