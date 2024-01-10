"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union
from typing_extensions import Annotated

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0170 import (
    ProtectedBranchPullRequestReviewPropDismissalRestrictions,
    ProtectedBranchPullRequestReviewPropBypassPullRequestAllowances,
)


class ProtectedBranchPullRequestReview(GitHubModel):
    """Protected Branch Pull Request Review

    Protected Branch Pull Request Review
    """

    url: Missing[str] = Field(default=UNSET)
    dismissal_restrictions: Missing[
        ProtectedBranchPullRequestReviewPropDismissalRestrictions
    ] = Field(default=UNSET)
    bypass_pull_request_allowances: Missing[
        ProtectedBranchPullRequestReviewPropBypassPullRequestAllowances
    ] = Field(
        default=UNSET,
        description="Allow specific users, teams, or apps to bypass pull request requirements.",
    )
    dismiss_stale_reviews: bool = Field()
    require_code_owner_reviews: bool = Field()
    required_approving_review_count: Missing[int] = Field(le=6.0, default=UNSET)
    require_last_push_approval: Missing[bool] = Field(
        default=UNSET,
        description="Whether the most recent push must be approved by someone other than the person who pushed it.",
    )


model_rebuild(ProtectedBranchPullRequestReview)

__all__ = ("ProtectedBranchPullRequestReview",)
