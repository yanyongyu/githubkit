"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0218 import (
    ProtectedBranchPullRequestReviewPropBypassPullRequestAllowancesType,
    ProtectedBranchPullRequestReviewPropDismissalRestrictionsType,
)


class ProtectedBranchPullRequestReviewType(TypedDict):
    """Protected Branch Pull Request Review

    Protected Branch Pull Request Review
    """

    url: NotRequired[str]
    dismissal_restrictions: NotRequired[
        ProtectedBranchPullRequestReviewPropDismissalRestrictionsType
    ]
    bypass_pull_request_allowances: NotRequired[
        ProtectedBranchPullRequestReviewPropBypassPullRequestAllowancesType
    ]
    dismiss_stale_reviews: bool
    require_code_owner_reviews: bool
    required_approving_review_count: NotRequired[int]
    require_last_push_approval: NotRequired[bool]


__all__ = ("ProtectedBranchPullRequestReviewType",)
