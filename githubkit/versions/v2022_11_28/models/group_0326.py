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


class TimelineReviewedEvent(GitHubModel):
    """Timeline Reviewed Event

    Timeline Reviewed Event
    """

    event: Literal["reviewed"] = Field()
    id: int = Field(description="Unique identifier of the review")
    node_id: str = Field()
    user: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    body: Union[str, None] = Field(description="The text of the review.")
    state: str = Field()
    html_url: str = Field()
    pull_request_url: str = Field()
    links: TimelineReviewedEventPropLinks = Field(alias="_links")
    submitted_at: Missing[datetime] = Field(default=UNSET)
    commit_id: str = Field(description="A commit SHA for the review.")
    body_html: Missing[Union[str, None]] = Field(default=UNSET)
    body_text: Missing[Union[str, None]] = Field(default=UNSET)
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


class TimelineReviewedEventPropLinks(GitHubModel):
    """TimelineReviewedEventPropLinks"""

    html: TimelineReviewedEventPropLinksPropHtml = Field()
    pull_request: TimelineReviewedEventPropLinksPropPullRequest = Field()


class TimelineReviewedEventPropLinksPropHtml(GitHubModel):
    """TimelineReviewedEventPropLinksPropHtml"""

    href: str = Field()


class TimelineReviewedEventPropLinksPropPullRequest(GitHubModel):
    """TimelineReviewedEventPropLinksPropPullRequest"""

    href: str = Field()


model_rebuild(TimelineReviewedEvent)
model_rebuild(TimelineReviewedEventPropLinks)
model_rebuild(TimelineReviewedEventPropLinksPropHtml)
model_rebuild(TimelineReviewedEventPropLinksPropPullRequest)

__all__ = (
    "TimelineReviewedEvent",
    "TimelineReviewedEventPropLinks",
    "TimelineReviewedEventPropLinksPropHtml",
    "TimelineReviewedEventPropLinksPropPullRequest",
)
