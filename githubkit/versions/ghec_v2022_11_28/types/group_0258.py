"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0050 import TeamType
from .group_0067 import MilestoneType
from .group_0257 import AutoMergeType
from .group_0002 import SimpleUserType
from .group_0260 import PullRequestSimplePropLinksType
from .group_0259 import PullRequestSimplePropBaseType, PullRequestSimplePropHeadType


class PullRequestSimpleType(TypedDict):
    """Pull Request Simple

    Pull Request Simple
    """

    url: str
    id: int
    node_id: str
    html_url: str
    diff_url: str
    patch_url: str
    issue_url: str
    commits_url: str
    review_comments_url: str
    review_comment_url: str
    comments_url: str
    statuses_url: str
    number: int
    state: str
    locked: bool
    title: str
    user: Union[None, SimpleUserType]
    body: Union[str, None]
    labels: list[PullRequestSimplePropLabelsItemsType]
    milestone: Union[None, MilestoneType]
    active_lock_reason: NotRequired[Union[str, None]]
    created_at: datetime
    updated_at: datetime
    closed_at: Union[datetime, None]
    merged_at: Union[datetime, None]
    merge_commit_sha: Union[str, None]
    assignee: Union[None, SimpleUserType]
    assignees: NotRequired[Union[list[SimpleUserType], None]]
    requested_reviewers: NotRequired[Union[list[SimpleUserType], None]]
    requested_teams: NotRequired[Union[list[TeamType], None]]
    head: PullRequestSimplePropHeadType
    base: PullRequestSimplePropBaseType
    links: PullRequestSimplePropLinksType
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]
    auto_merge: Union[AutoMergeType, None]
    draft: NotRequired[bool]


class PullRequestSimplePropLabelsItemsType(TypedDict):
    """PullRequestSimplePropLabelsItems"""

    id: int
    node_id: str
    url: str
    name: str
    description: Union[str, None]
    color: str
    default: bool


__all__ = (
    "PullRequestSimpleType",
    "PullRequestSimplePropLabelsItemsType",
)
