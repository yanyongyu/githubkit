"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyType(
    TypedDict
):
    """ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBody"""

    dismissal_restrictions: NotRequired[
        ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropDismissalRestrictionsType
    ]
    dismiss_stale_reviews: NotRequired[bool]
    require_code_owner_reviews: NotRequired[bool]
    required_approving_review_count: NotRequired[int]
    require_last_push_approval: NotRequired[bool]
    bypass_pull_request_allowances: NotRequired[
        ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropBypassPullRequestAllowancesType
    ]


class ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropDismissalRestrictionsType(
    TypedDict
):
    """ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropDis
    missalRestrictions

    Specify which users, teams, and apps can dismiss pull request reviews. Pass an
    empty `dismissal_restrictions` object to disable. User and team
    `dismissal_restrictions` are only available for organization-owned repositories.
    Omit this parameter for personal repositories.
    """

    users: NotRequired[List[str]]
    teams: NotRequired[List[str]]
    apps: NotRequired[List[str]]


class ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropBypassPullRequestAllowancesType(
    TypedDict
):
    """ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropByp
    assPullRequestAllowances

    Allow specific users, teams, or apps to bypass pull request requirements.
    """

    users: NotRequired[List[str]]
    teams: NotRequired[List[str]]
    apps: NotRequired[List[str]]


__all__ = (
    "ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyType",
    "ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropDismissalRestrictionsType",
    "ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropBypassPullRequestAllowancesType",
)
