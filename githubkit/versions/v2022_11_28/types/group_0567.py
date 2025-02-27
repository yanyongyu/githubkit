"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict


class WebhookIssueCommentEditedPropIssueAllof1Type(TypedDict):
    """WebhookIssueCommentEditedPropIssueAllof1"""

    active_lock_reason: NotRequired[Union[str, None]]
    assignee: Union[WebhookIssueCommentEditedPropIssueAllof1PropAssigneeType, None]
    assignees: NotRequired[
        list[
            Union[WebhookIssueCommentEditedPropIssueAllof1PropAssigneesItemsType, None]
        ]
    ]
    author_association: NotRequired[str]
    body: NotRequired[Union[str, None]]
    closed_at: NotRequired[Union[str, None]]
    comments: NotRequired[int]
    comments_url: NotRequired[str]
    created_at: NotRequired[str]
    events_url: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    labels: list[WebhookIssueCommentEditedPropIssueAllof1PropLabelsItemsType]
    labels_url: NotRequired[str]
    locked: bool
    milestone: NotRequired[
        Union[WebhookIssueCommentEditedPropIssueAllof1PropMilestoneType, None]
    ]
    node_id: NotRequired[str]
    number: NotRequired[int]
    performed_via_github_app: NotRequired[
        Union[
            WebhookIssueCommentEditedPropIssueAllof1PropPerformedViaGithubAppType, None
        ]
    ]
    reactions: NotRequired[WebhookIssueCommentEditedPropIssueAllof1PropReactionsType]
    repository_url: NotRequired[str]
    state: Literal["open", "closed"]
    timeline_url: NotRequired[str]
    title: NotRequired[str]
    updated_at: NotRequired[str]
    url: NotRequired[str]
    user: NotRequired[WebhookIssueCommentEditedPropIssueAllof1PropUserType]


class WebhookIssueCommentEditedPropIssueAllof1PropAssigneeType(TypedDict):
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
    user_view_type: NotRequired[str]


class WebhookIssueCommentEditedPropIssueAllof1PropAssigneesItemsType(TypedDict):
    """WebhookIssueCommentEditedPropIssueAllof1PropAssigneesItems"""


class WebhookIssueCommentEditedPropIssueAllof1PropLabelsItemsType(TypedDict):
    """Label"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookIssueCommentEditedPropIssueAllof1PropMilestoneType(TypedDict):
    """WebhookIssueCommentEditedPropIssueAllof1PropMilestone"""


class WebhookIssueCommentEditedPropIssueAllof1PropPerformedViaGithubAppType(TypedDict):
    """WebhookIssueCommentEditedPropIssueAllof1PropPerformedViaGithubApp"""


class WebhookIssueCommentEditedPropIssueAllof1PropReactionsType(TypedDict):
    """WebhookIssueCommentEditedPropIssueAllof1PropReactions"""

    plus_one: NotRequired[int]
    minus_one: NotRequired[int]
    confused: NotRequired[int]
    eyes: NotRequired[int]
    heart: NotRequired[int]
    hooray: NotRequired[int]
    laugh: NotRequired[int]
    rocket: NotRequired[int]
    total_count: NotRequired[int]
    url: NotRequired[str]


class WebhookIssueCommentEditedPropIssueAllof1PropUserType(TypedDict):
    """WebhookIssueCommentEditedPropIssueAllof1PropUser"""

    avatar_url: NotRequired[str]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]


__all__ = (
    "WebhookIssueCommentEditedPropIssueAllof1PropAssigneeType",
    "WebhookIssueCommentEditedPropIssueAllof1PropAssigneesItemsType",
    "WebhookIssueCommentEditedPropIssueAllof1PropLabelsItemsType",
    "WebhookIssueCommentEditedPropIssueAllof1PropMilestoneType",
    "WebhookIssueCommentEditedPropIssueAllof1PropPerformedViaGithubAppType",
    "WebhookIssueCommentEditedPropIssueAllof1PropReactionsType",
    "WebhookIssueCommentEditedPropIssueAllof1PropUserType",
    "WebhookIssueCommentEditedPropIssueAllof1Type",
)
