"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0523 import (
    WebhookIssuesMilestonedPropIssueAllof0PropPerformedViaGithubAppType,
)
from .group_0524 import WebhookIssuesMilestonedPropIssueAllof0PropPullRequestType


class WebhookIssuesMilestonedPropIssueAllof0Type(TypedDict):
    """Issue

    The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    """

    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ]
    assignee: NotRequired[
        Union[WebhookIssuesMilestonedPropIssueAllof0PropAssigneeType, None]
    ]
    assignees: List[
        Union[WebhookIssuesMilestonedPropIssueAllof0PropAssigneesItemsType, None]
    ]
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
    body: Union[str, None]
    closed_at: Union[datetime, None]
    comments: int
    comments_url: str
    created_at: datetime
    draft: NotRequired[bool]
    events_url: str
    html_url: str
    id: int
    labels: NotRequired[List[WebhookIssuesMilestonedPropIssueAllof0PropLabelsItemsType]]
    labels_url: str
    locked: NotRequired[bool]
    milestone: Union[WebhookIssuesMilestonedPropIssueAllof0PropMilestoneType, None]
    node_id: str
    number: int
    performed_via_github_app: NotRequired[
        Union[WebhookIssuesMilestonedPropIssueAllof0PropPerformedViaGithubAppType, None]
    ]
    pull_request: NotRequired[WebhookIssuesMilestonedPropIssueAllof0PropPullRequestType]
    reactions: WebhookIssuesMilestonedPropIssueAllof0PropReactionsType
    repository_url: str
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[Union[str, None]]
    timeline_url: NotRequired[str]
    title: str
    updated_at: datetime
    url: str
    user: Union[WebhookIssuesMilestonedPropIssueAllof0PropUserType, None]


class WebhookIssuesMilestonedPropIssueAllof0PropAssigneeType(TypedDict):
    """User"""

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


class WebhookIssuesMilestonedPropIssueAllof0PropAssigneesItemsType(TypedDict):
    """User"""

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


class WebhookIssuesMilestonedPropIssueAllof0PropLabelsItemsType(TypedDict):
    """Label"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookIssuesMilestonedPropIssueAllof0PropMilestoneType(TypedDict):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None]
    closed_issues: int
    created_at: datetime
    creator: Union[
        WebhookIssuesMilestonedPropIssueAllof0PropMilestonePropCreatorType, None
    ]
    description: Union[str, None]
    due_on: Union[datetime, None]
    html_url: str
    id: int
    labels_url: str
    node_id: str
    number: int
    open_issues: int
    state: Literal["open", "closed"]
    title: str
    updated_at: datetime
    url: str


class WebhookIssuesMilestonedPropIssueAllof0PropMilestonePropCreatorType(TypedDict):
    """User"""

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


class WebhookIssuesMilestonedPropIssueAllof0PropReactionsType(TypedDict):
    """Reactions"""

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


class WebhookIssuesMilestonedPropIssueAllof0PropUserType(TypedDict):
    """User"""

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
    "WebhookIssuesMilestonedPropIssueAllof0Type",
    "WebhookIssuesMilestonedPropIssueAllof0PropAssigneeType",
    "WebhookIssuesMilestonedPropIssueAllof0PropAssigneesItemsType",
    "WebhookIssuesMilestonedPropIssueAllof0PropLabelsItemsType",
    "WebhookIssuesMilestonedPropIssueAllof0PropMilestoneType",
    "WebhookIssuesMilestonedPropIssueAllof0PropMilestonePropCreatorType",
    "WebhookIssuesMilestonedPropIssueAllof0PropReactionsType",
    "WebhookIssuesMilestonedPropIssueAllof0PropUserType",
)
