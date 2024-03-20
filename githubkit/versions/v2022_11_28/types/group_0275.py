"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0033 import ReactionRollupType


class PullRequestReviewCommentType(TypedDict):
    """Pull Request Review Comment

    Pull Request Review Comments are comments on a portion of the Pull Request's
    diff.
    """

    url: str
    pull_request_review_id: Union[int, None]
    id: int
    node_id: str
    diff_hunk: str
    path: str
    position: NotRequired[int]
    original_position: NotRequired[int]
    commit_id: str
    original_commit_id: str
    in_reply_to_id: NotRequired[int]
    user: SimpleUserType
    body: str
    created_at: datetime
    updated_at: datetime
    html_url: str
    pull_request_url: str
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
    links: PullRequestReviewCommentPropLinksType
    start_line: NotRequired[Union[int, None]]
    original_start_line: NotRequired[Union[int, None]]
    start_side: NotRequired[Union[None, Literal["LEFT", "RIGHT"]]]
    line: NotRequired[int]
    original_line: NotRequired[int]
    side: NotRequired[Literal["LEFT", "RIGHT"]]
    subject_type: NotRequired[Literal["line", "file"]]
    reactions: NotRequired[ReactionRollupType]
    body_html: NotRequired[str]
    body_text: NotRequired[str]


class PullRequestReviewCommentPropLinksType(TypedDict):
    """PullRequestReviewCommentPropLinks"""

    self_: PullRequestReviewCommentPropLinksPropSelfType
    html: PullRequestReviewCommentPropLinksPropHtmlType
    pull_request: PullRequestReviewCommentPropLinksPropPullRequestType


class PullRequestReviewCommentPropLinksPropSelfType(TypedDict):
    """PullRequestReviewCommentPropLinksPropSelf"""

    href: str


class PullRequestReviewCommentPropLinksPropHtmlType(TypedDict):
    """PullRequestReviewCommentPropLinksPropHtml"""

    href: str


class PullRequestReviewCommentPropLinksPropPullRequestType(TypedDict):
    """PullRequestReviewCommentPropLinksPropPullRequest"""

    href: str


class TimelineLineCommentedEventType(TypedDict):
    """Timeline Line Commented Event

    Timeline Line Commented Event
    """

    event: NotRequired[Literal["line_commented"]]
    node_id: NotRequired[str]
    comments: NotRequired[List[PullRequestReviewCommentType]]


__all__ = (
    "PullRequestReviewCommentType",
    "PullRequestReviewCommentPropLinksType",
    "PullRequestReviewCommentPropLinksPropSelfType",
    "PullRequestReviewCommentPropLinksPropHtmlType",
    "PullRequestReviewCommentPropLinksPropPullRequestType",
    "TimelineLineCommentedEventType",
)
