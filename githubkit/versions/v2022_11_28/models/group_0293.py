"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0002 import SimpleUser
from .group_0040 import ReactionRollup


class PullRequestReviewComment(GitHubModel):
    """Pull Request Review Comment

    Pull Request Review Comments are comments on a portion of the Pull Request's
    diff.
    """

    url: str = Field(description="URL for the pull request review comment")
    pull_request_review_id: Union[int, None] = Field(
        description="The ID of the pull request review to which the comment belongs."
    )
    id: int = Field(description="The ID of the pull request review comment.")
    node_id: str = Field(description="The node ID of the pull request review comment.")
    diff_hunk: str = Field(
        description="The diff of the line that the comment refers to."
    )
    path: str = Field(
        description="The relative path of the file to which the comment applies."
    )
    position: Missing[int] = Field(
        default=UNSET,
        description="The line index in the diff to which the comment applies. This field is deprecated; use `line` instead.",
    )
    original_position: Missing[int] = Field(
        default=UNSET,
        description="The index of the original line in the diff to which the comment applies. This field is deprecated; use `original_line` instead.",
    )
    commit_id: str = Field(
        description="The SHA of the commit to which the comment applies."
    )
    original_commit_id: str = Field(
        description="The SHA of the original commit to which the comment applies."
    )
    in_reply_to_id: Missing[int] = Field(
        default=UNSET, description="The comment ID to reply to."
    )
    user: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    body: str = Field(description="The text of the comment.")
    created_at: datetime = Field()
    updated_at: datetime = Field()
    html_url: str = Field(description="HTML URL for the pull request review comment.")
    pull_request_url: str = Field(
        description="URL for the pull request that the review comment belongs to."
    )
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ] = Field(
        title="author_association",
        description="How the author is associated with the repository.",
    )
    links: PullRequestReviewCommentPropLinks = Field(alias="_links")
    start_line: Missing[Union[int, None]] = Field(
        default=UNSET,
        description="The first line of the range for a multi-line comment.",
    )
    original_start_line: Missing[Union[int, None]] = Field(
        default=UNSET,
        description="The first line of the range for a multi-line comment.",
    )
    start_side: Missing[Union[None, Literal["LEFT", "RIGHT"]]] = Field(
        default=UNSET,
        description="The side of the first line of the range for a multi-line comment.",
    )
    line: Missing[int] = Field(
        default=UNSET,
        description="The line of the blob to which the comment applies. The last line of the range for a multi-line comment",
    )
    original_line: Missing[int] = Field(
        default=UNSET,
        description="The line of the blob to which the comment applies. The last line of the range for a multi-line comment",
    )
    side: Missing[Literal["LEFT", "RIGHT"]] = Field(
        default=UNSET,
        description="The side of the diff to which the comment applies. The side of the last line of the range for a multi-line comment",
    )
    subject_type: Missing[Literal["line", "file"]] = Field(
        default=UNSET,
        description="The level at which the comment is targeted, can be a diff line or a file.",
    )
    reactions: Missing[ReactionRollup] = Field(default=UNSET, title="Reaction Rollup")
    body_html: Missing[str] = Field(default=UNSET)
    body_text: Missing[str] = Field(default=UNSET)


class PullRequestReviewCommentPropLinks(GitHubModel):
    """PullRequestReviewCommentPropLinks"""

    self_: PullRequestReviewCommentPropLinksPropSelf = Field(alias="self")
    html: PullRequestReviewCommentPropLinksPropHtml = Field()
    pull_request: PullRequestReviewCommentPropLinksPropPullRequest = Field()


class PullRequestReviewCommentPropLinksPropSelf(GitHubModel):
    """PullRequestReviewCommentPropLinksPropSelf"""

    href: str = Field()


class PullRequestReviewCommentPropLinksPropHtml(GitHubModel):
    """PullRequestReviewCommentPropLinksPropHtml"""

    href: str = Field()


class PullRequestReviewCommentPropLinksPropPullRequest(GitHubModel):
    """PullRequestReviewCommentPropLinksPropPullRequest"""

    href: str = Field()


class TimelineLineCommentedEvent(GitHubModel):
    """Timeline Line Commented Event

    Timeline Line Commented Event
    """

    event: Missing[Literal["line_commented"]] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    comments: Missing[List[PullRequestReviewComment]] = Field(default=UNSET)


model_rebuild(PullRequestReviewComment)
model_rebuild(PullRequestReviewCommentPropLinks)
model_rebuild(PullRequestReviewCommentPropLinksPropSelf)
model_rebuild(PullRequestReviewCommentPropLinksPropHtml)
model_rebuild(PullRequestReviewCommentPropLinksPropPullRequest)
model_rebuild(TimelineLineCommentedEvent)

__all__ = (
    "PullRequestReviewComment",
    "PullRequestReviewCommentPropLinks",
    "PullRequestReviewCommentPropLinksPropSelf",
    "PullRequestReviewCommentPropLinksPropHtml",
    "PullRequestReviewCommentPropLinksPropPullRequest",
    "TimelineLineCommentedEvent",
)
