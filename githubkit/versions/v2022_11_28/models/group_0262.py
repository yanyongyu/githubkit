"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0005 import Integration


class ReviewDismissedIssueEvent(GitHubModel):
    """Review Dismissed Issue Event

    Review Dismissed Issue Event
    """

    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    actor: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    event: Literal["review_dismissed"] = Field()
    commit_id: Union[str, None] = Field()
    commit_url: Union[str, None] = Field()
    created_at: str = Field()
    performed_via_github_app: Union[None, Integration] = Field()
    dismissed_review: ReviewDismissedIssueEventPropDismissedReview = Field()


class ReviewDismissedIssueEventPropDismissedReview(GitHubModel):
    """ReviewDismissedIssueEventPropDismissedReview"""

    state: str = Field()
    review_id: int = Field()
    dismissal_message: Union[str, None] = Field()
    dismissal_commit_id: Missing[str] = Field(default=UNSET)


model_rebuild(ReviewDismissedIssueEvent)
model_rebuild(ReviewDismissedIssueEventPropDismissedReview)

__all__ = (
    "ReviewDismissedIssueEvent",
    "ReviewDismissedIssueEventPropDismissedReview",
)
