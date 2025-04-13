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


class PullRequestReviewType(TypedDict):
    """Pull Request Review

    Pull Request Reviews are reviews on pull requests.
    """

    id: int
    node_id: str
    user: Union[None, SimpleUserType]
    body: str
    state: str
    html_url: str
    pull_request_url: str
    links: PullRequestReviewPropLinksType
    submitted_at: NotRequired[datetime]
    commit_id: Union[str, None]
    body_html: NotRequired[str]
    body_text: NotRequired[str]
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


class PullRequestReviewPropLinksType(TypedDict):
    """PullRequestReviewPropLinks"""

    html: PullRequestReviewPropLinksPropHtmlType
    pull_request: PullRequestReviewPropLinksPropPullRequestType


class PullRequestReviewPropLinksPropHtmlType(TypedDict):
    """PullRequestReviewPropLinksPropHtml"""

    href: str


class PullRequestReviewPropLinksPropPullRequestType(TypedDict):
    """PullRequestReviewPropLinksPropPullRequest"""

    href: str


__all__ = (
    "PullRequestReviewPropLinksPropHtmlType",
    "PullRequestReviewPropLinksPropPullRequestType",
    "PullRequestReviewPropLinksType",
    "PullRequestReviewType",
)
