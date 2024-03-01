"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0551 import WebhookIssuesUnlockedPropIssueMergedMilestoneType
from .group_0549 import WebhookIssuesUnlockedPropIssueAllof0PropPullRequestType


class WebhookIssuesUnlockedPropIssueType(TypedDict):
    """WebhookIssuesUnlockedPropIssue"""

    active_lock_reason: Union[None, None]
    assignee: NotRequired[Union[WebhookIssuesUnlockedPropIssueMergedAssigneeType, None]]
    assignees: List[WebhookIssuesUnlockedPropIssueMergedAssigneesType]
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
    labels: NotRequired[List[WebhookIssuesUnlockedPropIssueMergedLabelsType]]
    labels_url: str
    locked: Literal[False]
    milestone: Union[WebhookIssuesUnlockedPropIssueMergedMilestoneType, None]
    node_id: str
    number: int
    performed_via_github_app: NotRequired[Union[None, None]]
    pull_request: NotRequired[WebhookIssuesUnlockedPropIssueAllof0PropPullRequestType]
    reactions: WebhookIssuesUnlockedPropIssueMergedReactionsType
    repository_url: str
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[Union[str, None]]
    timeline_url: NotRequired[str]
    title: str
    updated_at: datetime
    url: str
    user: WebhookIssuesUnlockedPropIssueMergedUserType


class WebhookIssuesUnlockedPropIssueMergedAssigneeType(TypedDict):
    """WebhookIssuesUnlockedPropIssueMergedAssignee"""

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
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookIssuesUnlockedPropIssueMergedAssigneesType(TypedDict):
    """WebhookIssuesUnlockedPropIssueMergedAssignees"""

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
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookIssuesUnlockedPropIssueMergedLabelsType(TypedDict):
    """WebhookIssuesUnlockedPropIssueMergedLabels"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookIssuesUnlockedPropIssueMergedReactionsType(TypedDict):
    """WebhookIssuesUnlockedPropIssueMergedReactions"""

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


class WebhookIssuesUnlockedPropIssueMergedUserType(TypedDict):
    """WebhookIssuesUnlockedPropIssueMergedUser"""

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
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


__all__ = (
    "WebhookIssuesUnlockedPropIssueType",
    "WebhookIssuesUnlockedPropIssueMergedAssigneeType",
    "WebhookIssuesUnlockedPropIssueMergedAssigneesType",
    "WebhookIssuesUnlockedPropIssueMergedLabelsType",
    "WebhookIssuesUnlockedPropIssueMergedReactionsType",
    "WebhookIssuesUnlockedPropIssueMergedUserType",
)
