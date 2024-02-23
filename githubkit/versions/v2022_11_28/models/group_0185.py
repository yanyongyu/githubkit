"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0186 import (
    ProtectedBranchPropRequiredPullRequestReviewsPropDismissalRestrictions,
    ProtectedBranchPropRequiredPullRequestReviewsPropBypassPullRequestAllowances,
)


class ProtectedBranchPropRequiredPullRequestReviews(GitHubModel):
    """ProtectedBranchPropRequiredPullRequestReviews"""

    url: str = Field()
    dismiss_stale_reviews: Missing[bool] = Field(default=UNSET)
    require_code_owner_reviews: Missing[bool] = Field(default=UNSET)
    required_approving_review_count: Missing[int] = Field(default=UNSET)
    require_last_push_approval: Missing[bool] = Field(
        default=UNSET,
        description="Whether the most recent push must be approved by someone other than the person who pushed it.",
    )
    dismissal_restrictions: Missing[
        ProtectedBranchPropRequiredPullRequestReviewsPropDismissalRestrictions
    ] = Field(default=UNSET)
    bypass_pull_request_allowances: Missing[
        ProtectedBranchPropRequiredPullRequestReviewsPropBypassPullRequestAllowances
    ] = Field(default=UNSET)


model_rebuild(ProtectedBranchPropRequiredPullRequestReviews)

__all__ = ("ProtectedBranchPropRequiredPullRequestReviews",)
