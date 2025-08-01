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

from .group_0003 import SimpleUser
from .group_0045 import ReactionRollup
from .group_0356 import ReviewCommentPropLinks


class ReviewComment(GitHubModel):
    """Legacy Review Comment

    Legacy Review Comment
    """

    url: str = Field()
    pull_request_review_id: Union[int, None] = Field()
    id: int = Field()
    node_id: str = Field()
    diff_hunk: str = Field()
    path: str = Field()
    position: Union[int, None] = Field()
    original_position: int = Field()
    commit_id: str = Field()
    original_commit_id: str = Field()
    in_reply_to_id: Missing[int] = Field(default=UNSET)
    user: Union[None, SimpleUser] = Field()
    body: str = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    html_url: str = Field()
    pull_request_url: str = Field()
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
    links: ReviewCommentPropLinks = Field(alias="_links")
    body_text: Missing[str] = Field(default=UNSET)
    body_html: Missing[str] = Field(default=UNSET)
    reactions: Missing[ReactionRollup] = Field(default=UNSET, title="Reaction Rollup")
    side: Missing[Literal["LEFT", "RIGHT"]] = Field(
        default=UNSET,
        description="The side of the first line of the range for a multi-line comment.",
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
        description="The original line of the blob to which the comment applies. The last line of the range for a multi-line comment",
    )
    start_line: Missing[Union[int, None]] = Field(
        default=UNSET,
        description="The first line of the range for a multi-line comment.",
    )
    original_start_line: Missing[Union[int, None]] = Field(
        default=UNSET,
        description="The original first line of the range for a multi-line comment.",
    )
    subject_type: Missing[Literal["line", "file"]] = Field(
        default=UNSET,
        description="The level at which the comment is targeted, can be a diff line or a file.",
    )


model_rebuild(ReviewComment)

__all__ = ("ReviewComment",)
