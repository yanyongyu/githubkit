"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType


class GistHistoryType(TypedDict):
    """Gist History

    Gist History
    """

    user: NotRequired[Union[None, SimpleUserType]]
    version: NotRequired[str]
    committed_at: NotRequired[datetime]
    change_status: NotRequired[GistHistoryPropChangeStatusType]
    url: NotRequired[str]


class GistHistoryPropChangeStatusType(TypedDict):
    """GistHistoryPropChangeStatus"""

    total: NotRequired[int]
    additions: NotRequired[int]
    deletions: NotRequired[int]


class GistSimplePropForkOfType(TypedDict):
    """Gist

    Gist
    """

    url: str
    forks_url: str
    commits_url: str
    id: str
    node_id: str
    git_pull_url: str
    git_push_url: str
    html_url: str
    files: GistSimplePropForkOfPropFilesType
    public: bool
    created_at: datetime
    updated_at: datetime
    description: Union[str, None]
    comments: int
    user: Union[None, SimpleUserType]
    comments_url: str
    owner: NotRequired[Union[None, SimpleUserType]]
    truncated: NotRequired[bool]
    forks: NotRequired[list[Any]]
    history: NotRequired[list[Any]]


class GistSimplePropForkOfPropFilesType(TypedDict):
    """GistSimplePropForkOfPropFiles"""


__all__ = (
    "GistHistoryPropChangeStatusType",
    "GistHistoryType",
    "GistSimplePropForkOfPropFilesType",
    "GistSimplePropForkOfType",
)
