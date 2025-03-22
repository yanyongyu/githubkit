"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict


class WebhooksReviewCommentType(TypedDict):
    """Pull Request Review Comment

    The [comment](https://docs.github.com/enterprise-
    cloud@latest//rest/pulls/comments#get-a-review-comment-for-a-pull-request)
    itself.
    """

    links: WebhooksReviewCommentPropLinksType
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
    commit_id: str
    created_at: datetime
    diff_hunk: str
    html_url: str
    id: int
    in_reply_to_id: NotRequired[int]
    line: Union[int, None]
    node_id: str
    original_commit_id: str
    original_line: int
    original_position: int
    original_start_line: Union[int, None]
    path: str
    position: Union[int, None]
    pull_request_review_id: Union[int, None]
    pull_request_url: str
    reactions: WebhooksReviewCommentPropReactionsType
    side: Literal["LEFT", "RIGHT"]
    start_line: Union[int, None]
    start_side: Union[None, Literal["LEFT", "RIGHT"]]
    subject_type: NotRequired[Literal["line", "file"]]
    updated_at: datetime
    url: str
    user: Union[WebhooksReviewCommentPropUserType, None]


class WebhooksReviewCommentPropReactionsType(TypedDict):
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


class WebhooksReviewCommentPropUserType(TypedDict):
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
    user_view_type: NotRequired[str]


class WebhooksReviewCommentPropLinksType(TypedDict):
    """WebhooksReviewCommentPropLinks"""

    html: WebhooksReviewCommentPropLinksPropHtmlType
    pull_request: WebhooksReviewCommentPropLinksPropPullRequestType
    self_: WebhooksReviewCommentPropLinksPropSelfType


class WebhooksReviewCommentPropLinksPropHtmlType(TypedDict):
    """Link"""

    href: str


class WebhooksReviewCommentPropLinksPropPullRequestType(TypedDict):
    """Link"""

    href: str


class WebhooksReviewCommentPropLinksPropSelfType(TypedDict):
    """Link"""

    href: str


__all__ = (
    "WebhooksReviewCommentPropLinksPropHtmlType",
    "WebhooksReviewCommentPropLinksPropPullRequestType",
    "WebhooksReviewCommentPropLinksPropSelfType",
    "WebhooksReviewCommentPropLinksType",
    "WebhooksReviewCommentPropReactionsType",
    "WebhooksReviewCommentPropUserType",
    "WebhooksReviewCommentType",
)
