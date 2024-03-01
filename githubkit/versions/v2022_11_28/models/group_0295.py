"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser


class PullRequestReview(GitHubModel):
    """Pull Request Review

    Pull Request Reviews are reviews on pull requests.
    """

    id: int = Field(description="Unique identifier of the review")
    node_id: str = Field()
    user: Union[None, SimpleUser] = Field()
    body: str = Field(description="The text of the review.")
    state: str = Field()
    html_url: str = Field()
    pull_request_url: str = Field()
    links: PullRequestReviewPropLinks = Field(alias="_links")
    submitted_at: Missing[datetime] = Field(default=UNSET)
    commit_id: Union[str, None] = Field(
        description="A commit SHA for the review. If the commit object was garbage collected or forcibly deleted, then it no longer exists in Git and this value will be `null`."
    )
    body_html: Missing[str] = Field(default=UNSET)
    body_text: Missing[str] = Field(default=UNSET)
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


class PullRequestReviewPropLinks(GitHubModel):
    """PullRequestReviewPropLinks"""

    html: PullRequestReviewPropLinksPropHtml = Field()
    pull_request: PullRequestReviewPropLinksPropPullRequest = Field()


class PullRequestReviewPropLinksPropHtml(GitHubModel):
    """PullRequestReviewPropLinksPropHtml"""

    href: str = Field()


class PullRequestReviewPropLinksPropPullRequest(GitHubModel):
    """PullRequestReviewPropLinksPropPullRequest"""

    href: str = Field()


model_rebuild(PullRequestReview)
model_rebuild(PullRequestReviewPropLinks)
model_rebuild(PullRequestReviewPropLinksPropHtml)
model_rebuild(PullRequestReviewPropLinksPropPullRequest)

__all__ = (
    "PullRequestReview",
    "PullRequestReviewPropLinks",
    "PullRequestReviewPropLinksPropHtml",
    "PullRequestReviewPropLinksPropPullRequest",
)
