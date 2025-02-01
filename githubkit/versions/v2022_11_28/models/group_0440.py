"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class WebhooksReviewComment(GitHubModel):
    """Pull Request Review Comment

    The [comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-
    for-a-pull-request) itself.
    """

    links: WebhooksReviewCommentPropLinks = Field(alias="_links")
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
        title="AuthorAssociation",
        description="How the author is associated with the repository.",
    )
    body: str = Field(description="The text of the comment.")
    commit_id: str = Field(
        description="The SHA of the commit to which the comment applies."
    )
    created_at: datetime = Field()
    diff_hunk: str = Field(
        description="The diff of the line that the comment refers to."
    )
    html_url: str = Field(description="HTML URL for the pull request review comment.")
    id: int = Field(description="The ID of the pull request review comment.")
    in_reply_to_id: Missing[int] = Field(
        default=UNSET, description="The comment ID to reply to."
    )
    line: Union[int, None] = Field(
        description="The line of the blob to which the comment applies. The last line of the range for a multi-line comment"
    )
    node_id: str = Field(description="The node ID of the pull request review comment.")
    original_commit_id: str = Field(
        description="The SHA of the original commit to which the comment applies."
    )
    original_line: int = Field(
        description="The line of the blob to which the comment applies. The last line of the range for a multi-line comment"
    )
    original_position: int = Field(
        description="The index of the original line in the diff to which the comment applies."
    )
    original_start_line: Union[int, None] = Field(
        description="The first line of the range for a multi-line comment."
    )
    path: str = Field(
        description="The relative path of the file to which the comment applies."
    )
    position: Union[int, None] = Field(
        description="The line index in the diff to which the comment applies."
    )
    pull_request_review_id: Union[int, None] = Field(
        description="The ID of the pull request review to which the comment belongs."
    )
    pull_request_url: str = Field(
        description="URL for the pull request that the review comment belongs to."
    )
    reactions: WebhooksReviewCommentPropReactions = Field(title="Reactions")
    side: Literal["LEFT", "RIGHT"] = Field(
        description="The side of the first line of the range for a multi-line comment."
    )
    start_line: Union[int, None] = Field(
        description="The first line of the range for a multi-line comment."
    )
    start_side: Union[None, Literal["LEFT", "RIGHT"]] = Field(
        default="RIGHT",
        description="The side of the first line of the range for a multi-line comment.",
    )
    subject_type: Missing[Literal["line", "file"]] = Field(
        default=UNSET,
        description="The level at which the comment is targeted, can be a diff line or a file.",
    )
    updated_at: datetime = Field()
    url: str = Field(description="URL for the pull request review comment")
    user: Union[WebhooksReviewCommentPropUser, None] = Field(title="User")


class WebhooksReviewCommentPropReactions(GitHubModel):
    """Reactions"""

    plus_one: int = Field(alias="+1")
    minus_one: int = Field(alias="-1")
    confused: int = Field()
    eyes: int = Field()
    heart: int = Field()
    hooray: int = Field()
    laugh: int = Field()
    rocket: int = Field()
    total_count: int = Field()
    url: str = Field()


class WebhooksReviewCommentPropUser(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhooksReviewCommentPropLinks(GitHubModel):
    """WebhooksReviewCommentPropLinks"""

    html: WebhooksReviewCommentPropLinksPropHtml = Field(title="Link")
    pull_request: WebhooksReviewCommentPropLinksPropPullRequest = Field(title="Link")
    self_: WebhooksReviewCommentPropLinksPropSelf = Field(alias="self", title="Link")


class WebhooksReviewCommentPropLinksPropHtml(GitHubModel):
    """Link"""

    href: str = Field()


class WebhooksReviewCommentPropLinksPropPullRequest(GitHubModel):
    """Link"""

    href: str = Field()


class WebhooksReviewCommentPropLinksPropSelf(GitHubModel):
    """Link"""

    href: str = Field()


model_rebuild(WebhooksReviewComment)
model_rebuild(WebhooksReviewCommentPropReactions)
model_rebuild(WebhooksReviewCommentPropUser)
model_rebuild(WebhooksReviewCommentPropLinks)
model_rebuild(WebhooksReviewCommentPropLinksPropHtml)
model_rebuild(WebhooksReviewCommentPropLinksPropPullRequest)
model_rebuild(WebhooksReviewCommentPropLinksPropSelf)

__all__ = (
    "WebhooksReviewComment",
    "WebhooksReviewCommentPropLinks",
    "WebhooksReviewCommentPropLinksPropHtml",
    "WebhooksReviewCommentPropLinksPropPullRequest",
    "WebhooksReviewCommentPropLinksPropSelf",
    "WebhooksReviewCommentPropReactions",
    "WebhooksReviewCommentPropUser",
)
