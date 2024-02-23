"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0510 import (
    WebhookIssueCommentEditedPropIssueAllof0PropAssigneeType,
    WebhookIssueCommentEditedPropIssueAllof0PropLabelsItemsType,
    WebhookIssueCommentEditedPropIssueAllof0PropPullRequestType,
)
from .group_0516 import WebhookIssueCommentEditedPropIssueMergedMilestoneType
from .group_0517 import (
    WebhookIssueCommentEditedPropIssueMergedPerformedViaGithubAppType,
)


class WebhookIssueCommentEditedPropIssueType(TypedDict):
    """WebhookIssueCommentEditedPropIssue

    The [issue](https://docs.github.com/enterprise-
    cloud@latest//rest/issues/issues#get-an-issue) the comment belongs to.
    """

    active_lock_reason: Union[
        Literal["resolved", "off-topic", "too heated", "spam"], None
    ]
    assignee: Union[
        Union[WebhookIssueCommentEditedPropIssueAllof0PropAssigneeType, None], None
    ]
    assignees: List[WebhookIssueCommentEditedPropIssueMergedAssigneesType]
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
    labels: List[WebhookIssueCommentEditedPropIssueAllof0PropLabelsItemsType]
    labels_url: str
    locked: bool
    milestone: Union[WebhookIssueCommentEditedPropIssueMergedMilestoneType, None]
    node_id: str
    number: int
    performed_via_github_app: NotRequired[
        Union[WebhookIssueCommentEditedPropIssueMergedPerformedViaGithubAppType, None]
    ]
    pull_request: NotRequired[
        WebhookIssueCommentEditedPropIssueAllof0PropPullRequestType
    ]
    reactions: WebhookIssueCommentEditedPropIssueMergedReactionsType
    repository_url: str
    state: Literal["open", "closed"]
    state_reason: NotRequired[Union[str, None]]
    timeline_url: NotRequired[str]
    title: str
    updated_at: datetime
    url: str
    user: WebhookIssueCommentEditedPropIssueMergedUserType


class WebhookIssueCommentEditedPropIssueMergedAssigneesType(TypedDict):
    """WebhookIssueCommentEditedPropIssueMergedAssignees"""

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


class WebhookIssueCommentEditedPropIssueMergedReactionsType(TypedDict):
    """WebhookIssueCommentEditedPropIssueMergedReactions"""

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


class WebhookIssueCommentEditedPropIssueMergedUserType(TypedDict):
    """WebhookIssueCommentEditedPropIssueMergedUser"""

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
    "WebhookIssueCommentEditedPropIssueType",
    "WebhookIssueCommentEditedPropIssueMergedAssigneesType",
    "WebhookIssueCommentEditedPropIssueMergedReactionsType",
    "WebhookIssueCommentEditedPropIssueMergedUserType",
)
