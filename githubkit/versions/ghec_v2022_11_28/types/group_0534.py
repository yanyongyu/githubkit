"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0535 import (
    WebhookIssuesDemilestonedPropIssueAllof0PropMilestoneType,
    WebhookIssuesDemilestonedPropIssueAllof0PropPullRequestType,
)
from .group_0537 import (
    WebhookIssuesDemilestonedPropIssueAllof0PropPerformedViaGithubAppType,
)


class WebhookIssuesDemilestonedPropIssueAllof0Type(TypedDict):
    """Issue

    The [issue](https://docs.github.com/enterprise-
    cloud@latest//rest/issues/issues#get-an-issue) itself.
    """

    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ]
    assignee: NotRequired[
        Union[WebhookIssuesDemilestonedPropIssueAllof0PropAssigneeType, None]
    ]
    assignees: List[
        Union[WebhookIssuesDemilestonedPropIssueAllof0PropAssigneesItemsType, None]
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
    labels: NotRequired[
        List[WebhookIssuesDemilestonedPropIssueAllof0PropLabelsItemsType]
    ]
    labels_url: str
    locked: NotRequired[bool]
    milestone: Union[WebhookIssuesDemilestonedPropIssueAllof0PropMilestoneType, None]
    node_id: str
    number: int
    performed_via_github_app: NotRequired[
        Union[
            WebhookIssuesDemilestonedPropIssueAllof0PropPerformedViaGithubAppType, None
        ]
    ]
    pull_request: NotRequired[
        WebhookIssuesDemilestonedPropIssueAllof0PropPullRequestType
    ]
    reactions: WebhookIssuesDemilestonedPropIssueAllof0PropReactionsType
    repository_url: str
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[Union[str, None]]
    timeline_url: NotRequired[str]
    title: str
    updated_at: datetime
    url: str
    user: Union[WebhookIssuesDemilestonedPropIssueAllof0PropUserType, None]


class WebhookIssuesDemilestonedPropIssueAllof0PropAssigneeType(TypedDict):
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


class WebhookIssuesDemilestonedPropIssueAllof0PropAssigneesItemsType(TypedDict):
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


class WebhookIssuesDemilestonedPropIssueAllof0PropLabelsItemsType(TypedDict):
    """Label"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookIssuesDemilestonedPropIssueAllof0PropReactionsType(TypedDict):
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


class WebhookIssuesDemilestonedPropIssueAllof0PropUserType(TypedDict):
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


__all__ = (
    "WebhookIssuesDemilestonedPropIssueAllof0Type",
    "WebhookIssuesDemilestonedPropIssueAllof0PropAssigneeType",
    "WebhookIssuesDemilestonedPropIssueAllof0PropAssigneesItemsType",
    "WebhookIssuesDemilestonedPropIssueAllof0PropLabelsItemsType",
    "WebhookIssuesDemilestonedPropIssueAllof0PropReactionsType",
    "WebhookIssuesDemilestonedPropIssueAllof0PropUserType",
)
