"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0040 import IssueTypeType
from .group_0592 import (
    WebhookIssuesClosedPropIssueAllof0PropPullRequestType,
    WebhookIssuesClosedPropIssueAllof0PropSubIssuesSummaryType,
)
from .group_0594 import WebhookIssuesClosedPropIssueMergedMilestoneType
from .group_0595 import WebhookIssuesClosedPropIssueMergedPerformedViaGithubAppType


class WebhookIssuesClosedPropIssueType(TypedDict):
    """WebhookIssuesClosedPropIssue

    The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    """

    active_lock_reason: Union[
        Literal["resolved", "off-topic", "too heated", "spam"], None
    ]
    assignee: NotRequired[Union[WebhookIssuesClosedPropIssueMergedAssigneeType, None]]
    assignees: list[WebhookIssuesClosedPropIssueMergedAssigneesType]
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
    body: Union[Union[str, None], None]
    closed_at: Union[datetime, None]
    comments: int
    comments_url: str
    created_at: datetime
    draft: NotRequired[bool]
    events_url: str
    html_url: str
    id: int
    labels: NotRequired[list[WebhookIssuesClosedPropIssueMergedLabelsType]]
    labels_url: str
    locked: NotRequired[bool]
    milestone: Union[WebhookIssuesClosedPropIssueMergedMilestoneType, None]
    node_id: str
    number: int
    performed_via_github_app: NotRequired[
        Union[WebhookIssuesClosedPropIssueMergedPerformedViaGithubAppType, None]
    ]
    pull_request: NotRequired[WebhookIssuesClosedPropIssueAllof0PropPullRequestType]
    reactions: WebhookIssuesClosedPropIssueMergedReactionsType
    repository_url: str
    sub_issues_summary: NotRequired[
        WebhookIssuesClosedPropIssueAllof0PropSubIssuesSummaryType
    ]
    state: Literal["open", "closed"]
    state_reason: NotRequired[Union[str, None]]
    timeline_url: NotRequired[str]
    title: str
    type: NotRequired[Union[IssueTypeType, None]]
    updated_at: datetime
    url: str
    user: WebhookIssuesClosedPropIssueMergedUserType


class WebhookIssuesClosedPropIssueMergedAssigneeType(TypedDict):
    """WebhookIssuesClosedPropIssueMergedAssignee"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhookIssuesClosedPropIssueMergedAssigneesType(TypedDict):
    """WebhookIssuesClosedPropIssueMergedAssignees"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhookIssuesClosedPropIssueMergedLabelsType(TypedDict):
    """WebhookIssuesClosedPropIssueMergedLabels"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookIssuesClosedPropIssueMergedReactionsType(TypedDict):
    """WebhookIssuesClosedPropIssueMergedReactions"""

    plus_one: int
    minus_one: int
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhookIssuesClosedPropIssueMergedUserType(TypedDict):
    """WebhookIssuesClosedPropIssueMergedUser"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


__all__ = (
    "WebhookIssuesClosedPropIssueMergedAssigneeType",
    "WebhookIssuesClosedPropIssueMergedAssigneesType",
    "WebhookIssuesClosedPropIssueMergedLabelsType",
    "WebhookIssuesClosedPropIssueMergedReactionsType",
    "WebhookIssuesClosedPropIssueMergedUserType",
    "WebhookIssuesClosedPropIssueType",
)
