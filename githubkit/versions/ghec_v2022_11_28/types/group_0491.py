"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0010 import IntegrationType


class WebhooksIssueCommentType(TypedDict):
    """issue comment

    The [comment](https://docs.github.com/enterprise-
    cloud@latest//rest/issues/comments#get-an-issue-comment) itself.
    """

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
    body: str
    created_at: datetime
    html_url: str
    id: int
    issue_url: str
    node_id: str
    performed_via_github_app: Union[IntegrationType, None]
    reactions: WebhooksIssueCommentPropReactionsType
    updated_at: datetime
    url: str
    user: Union[WebhooksIssueCommentPropUserType, None]


class WebhooksIssueCommentPropReactionsType(TypedDict):
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


class WebhooksIssueCommentPropUserType(TypedDict):
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


__all__ = (
    "WebhooksIssueCommentPropReactionsType",
    "WebhooksIssueCommentPropUserType",
    "WebhooksIssueCommentType",
)
