"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0548 import WebhookIssuesLockedPropIssueAllof0PropPullRequestType
from .group_0550 import WebhookIssuesLockedPropIssueMergedMilestoneType
from .group_0551 import WebhookIssuesLockedPropIssueMergedPerformedViaGithubAppType


class WebhookIssuesLockedPropIssueType(TypedDict):
    """WebhookIssuesLockedPropIssue"""

    active_lock_reason: Union[
        Union[None, Literal["resolved", "off-topic", "too heated", "spam"]], None
    ]
    assignee: NotRequired[Union[WebhookIssuesLockedPropIssueMergedAssigneeType, None]]
    assignees: List[WebhookIssuesLockedPropIssueMergedAssigneesType]
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
    labels: NotRequired[List[WebhookIssuesLockedPropIssueMergedLabelsType]]
    labels_url: str
    locked: Literal[True]
    milestone: Union[WebhookIssuesLockedPropIssueMergedMilestoneType, None]
    node_id: str
    number: int
    performed_via_github_app: NotRequired[
        Union[WebhookIssuesLockedPropIssueMergedPerformedViaGithubAppType, None]
    ]
    pull_request: NotRequired[WebhookIssuesLockedPropIssueAllof0PropPullRequestType]
    reactions: WebhookIssuesLockedPropIssueMergedReactionsType
    repository_url: str
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[Union[str, None]]
    timeline_url: NotRequired[str]
    title: str
    updated_at: datetime
    url: str
    user: WebhookIssuesLockedPropIssueMergedUserType


class WebhookIssuesLockedPropIssueMergedAssigneeType(TypedDict):
    """WebhookIssuesLockedPropIssueMergedAssignee"""

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


class WebhookIssuesLockedPropIssueMergedAssigneesType(TypedDict):
    """WebhookIssuesLockedPropIssueMergedAssignees"""

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


class WebhookIssuesLockedPropIssueMergedLabelsType(TypedDict):
    """WebhookIssuesLockedPropIssueMergedLabels"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookIssuesLockedPropIssueMergedReactionsType(TypedDict):
    """WebhookIssuesLockedPropIssueMergedReactions"""

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


class WebhookIssuesLockedPropIssueMergedUserType(TypedDict):
    """WebhookIssuesLockedPropIssueMergedUser"""

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
    "WebhookIssuesLockedPropIssueType",
    "WebhookIssuesLockedPropIssueMergedAssigneeType",
    "WebhookIssuesLockedPropIssueMergedAssigneesType",
    "WebhookIssuesLockedPropIssueMergedLabelsType",
    "WebhookIssuesLockedPropIssueMergedReactionsType",
    "WebhookIssuesLockedPropIssueMergedUserType",
)
