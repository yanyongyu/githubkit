"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0010 import IntegrationType
from .group_0020 import RepositoryType
from .group_0150 import MilestoneType
from .group_0151 import IssueTypeType
from .group_0152 import ReactionRollupType


class IssueType(TypedDict):
    """Issue

    Issues are a great way to keep track of tasks, enhancements, and bugs for your
    projects.
    """

    id: int
    node_id: str
    url: str
    repository_url: str
    labels_url: str
    comments_url: str
    events_url: str
    html_url: str
    number: int
    state: str
    state_reason: NotRequired[
        Union[None, Literal["completed", "reopened", "not_planned", "duplicate"]]
    ]
    title: str
    body: NotRequired[Union[str, None]]
    user: Union[None, SimpleUserType]
    labels: list[Union[str, IssuePropLabelsItemsOneof1Type]]
    assignee: Union[None, SimpleUserType]
    assignees: NotRequired[Union[list[SimpleUserType], None]]
    milestone: Union[None, MilestoneType]
    locked: bool
    active_lock_reason: NotRequired[Union[str, None]]
    comments: int
    pull_request: NotRequired[IssuePropPullRequestType]
    closed_at: Union[datetime, None]
    created_at: datetime
    updated_at: datetime
    draft: NotRequired[bool]
    closed_by: NotRequired[Union[None, SimpleUserType]]
    body_html: NotRequired[Union[str, None]]
    body_text: NotRequired[Union[str, None]]
    timeline_url: NotRequired[str]
    type: NotRequired[Union[IssueTypeType, None]]
    repository: NotRequired[RepositoryType]
    performed_via_github_app: NotRequired[Union[None, IntegrationType, None]]
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
    reactions: NotRequired[ReactionRollupType]
    sub_issues_summary: NotRequired[SubIssuesSummaryType]


class SubIssuesSummaryType(TypedDict):
    """Sub-issues Summary"""

    total: int
    completed: int
    percent_completed: int


class IssuePropLabelsItemsOneof1Type(TypedDict):
    """IssuePropLabelsItemsOneof1"""

    id: NotRequired[int]
    node_id: NotRequired[str]
    url: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[Union[str, None]]
    color: NotRequired[Union[str, None]]
    default: NotRequired[bool]


class IssuePropPullRequestType(TypedDict):
    """IssuePropPullRequest"""

    merged_at: NotRequired[Union[datetime, None]]
    diff_url: Union[str, None]
    html_url: Union[str, None]
    patch_url: Union[str, None]
    url: Union[str, None]


__all__ = (
    "IssuePropLabelsItemsOneof1Type",
    "IssuePropPullRequestType",
    "IssueType",
    "SubIssuesSummaryType",
)
