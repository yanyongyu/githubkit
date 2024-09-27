"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoBranchesBranchProtectionPutBody(GitHubModel):
    """ReposOwnerRepoBranchesBranchProtectionPutBody"""

    required_status_checks: Union[
        ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredStatusChecks, None
    ] = Field(
        description="Require status checks to pass before merging. Set to `null` to disable."
    )
    enforce_admins: Union[bool, None] = Field(
        description="Enforce all configured restrictions for administrators. Set to `true` to enforce required status checks for repository administrators. Set to `null` to disable."
    )
    required_pull_request_reviews: Union[
        ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredPullRequestReviews,
        None,
    ] = Field(
        description="Require at least one approving review on a pull request, before merging. Set to `null` to disable."
    )
    restrictions: Union[
        ReposOwnerRepoBranchesBranchProtectionPutBodyPropRestrictions, None
    ] = Field(
        description="Restrict who can push to the protected branch. User, app, and team `restrictions` are only available for organization-owned repositories. Set to `null` to disable."
    )
    required_linear_history: Missing[bool] = Field(
        default=UNSET,
        description='Enforces a linear commit Git history, which prevents anyone from pushing merge commits to a branch. Set to `true` to enforce a linear commit history. Set to `false` to disable a linear commit Git history. Your repository must allow squash merging or rebase merging before you can enable a linear commit history. Default: `false`. For more information, see "[Requiring a linear commit history](https://docs.github.com/github/administering-a-repository/requiring-a-linear-commit-history)" in the GitHub Help documentation.',
    )
    allow_force_pushes: Missing[Union[bool, None]] = Field(
        default=UNSET,
        description='Permits force pushes to the protected branch by anyone with write access to the repository. Set to `true` to allow force pushes. Set to `false` or `null` to block force pushes. Default: `false`. For more information, see "[Enabling force pushes to a protected branch](https://docs.github.com/github/administering-a-repository/enabling-force-pushes-to-a-protected-branch)" in the GitHub Help documentation."',
    )
    allow_deletions: Missing[bool] = Field(
        default=UNSET,
        description='Allows deletion of the protected branch by anyone with write access to the repository. Set to `false` to prevent deletion of the protected branch. Default: `false`. For more information, see "[Enabling force pushes to a protected branch](https://docs.github.com/github/administering-a-repository/enabling-force-pushes-to-a-protected-branch)" in the GitHub Help documentation.',
    )
    block_creations: Missing[bool] = Field(
        default=UNSET,
        description="If set to `true`, the `restrictions` branch protection settings which limits who can push will also block pushes which create new branches, unless the push is initiated by a user, team, or app which has the ability to push. Set to `true` to restrict new branch creation. Default: `false`.",
    )
    required_conversation_resolution: Missing[bool] = Field(
        default=UNSET,
        description="Requires all conversations on code to be resolved before a pull request can be merged into a branch that matches this rule. Set to `false` to disable. Default: `false`.",
    )
    lock_branch: Missing[bool] = Field(
        default=UNSET,
        description="Whether to set the branch as read-only. If this is true, users will not be able to push to the branch. Default: `false`.",
    )
    allow_fork_syncing: Missing[bool] = Field(
        default=UNSET,
        description="Whether users can pull changes from upstream when the branch is locked. Set to `true` to allow fork syncing. Set to `false` to prevent fork syncing. Default: `false`.",
    )


class ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredStatusChecks(
    GitHubModel
):
    """ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredStatusChecks

    Require status checks to pass before merging. Set to `null` to disable.
    """

    strict: bool = Field(
        description="Require branches to be up to date before merging."
    )
    contexts: List[str] = Field(
        description="**Deprecated**: The list of status checks to require in order to merge into this branch. If any of these checks have recently been set by a particular GitHub App, they will be required to come from that app in future for the branch to merge. Use `checks` instead of `contexts` for more fine-grained control."
    )
    checks: Missing[
        List[
            ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredStatusChecksPropChecksItems
        ]
    ] = Field(
        default=UNSET,
        description="The list of status checks to require in order to merge into this branch.",
    )


class ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredStatusChecksPropChecksItems(
    GitHubModel
):
    """ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredStatusChecksPropChecksI
    tems
    """

    context: str = Field(description="The name of the required check")
    app_id: Missing[int] = Field(
        default=UNSET,
        description="The ID of the GitHub App that must provide this check. Omit this field to automatically select the GitHub App that has recently provided this check, or any app if it was not set by a GitHub App. Pass -1 to explicitly allow any app to set the status.",
    )


class ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredPullRequestReviews(
    GitHubModel
):
    """ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredPullRequestReviews

    Require at least one approving review on a pull request, before merging. Set to
    `null` to disable.
    """

    dismissal_restrictions: Missing[
        ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredPullRequestReviewsPropDismissalRestrictions
    ] = Field(
        default=UNSET,
        description="Specify which users, teams, and apps can dismiss pull request reviews. Pass an empty `dismissal_restrictions` object to disable. User and team `dismissal_restrictions` are only available for organization-owned repositories. Omit this parameter for personal repositories.",
    )
    dismiss_stale_reviews: Missing[bool] = Field(
        default=UNSET,
        description="Set to `true` if you want to automatically dismiss approving reviews when someone pushes a new commit.",
    )
    require_code_owner_reviews: Missing[bool] = Field(
        default=UNSET,
        description="Blocks merging pull requests until [code owners](https://docs.github.com/articles/about-code-owners/) review them.",
    )
    required_approving_review_count: Missing[int] = Field(
        default=UNSET,
        description="Specify the number of reviewers required to approve pull requests. Use a number between 1 and 6 or 0 to not require reviewers.",
    )
    require_last_push_approval: Missing[bool] = Field(
        default=UNSET,
        description="Whether the most recent push must be approved by someone other than the person who pushed it. Default: `false`.",
    )
    bypass_pull_request_allowances: Missing[
        ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredPullRequestReviewsPropBypassPullRequestAllowances
    ] = Field(
        default=UNSET,
        description="Allow specific users, teams, or apps to bypass pull request requirements.",
    )


class ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredPullRequestReviewsPropDismissalRestrictions(
    GitHubModel
):
    """ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredPullRequestReviewsPropD
    ismissalRestrictions

    Specify which users, teams, and apps can dismiss pull request reviews. Pass an
    empty `dismissal_restrictions` object to disable. User and team
    `dismissal_restrictions` are only available for organization-owned repositories.
    Omit this parameter for personal repositories.
    """

    users: Missing[List[str]] = Field(
        default=UNSET, description="The list of user `login`s with dismissal access"
    )
    teams: Missing[List[str]] = Field(
        default=UNSET, description="The list of team `slug`s with dismissal access"
    )
    apps: Missing[List[str]] = Field(
        default=UNSET, description="The list of app `slug`s with dismissal access"
    )


class ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredPullRequestReviewsPropBypassPullRequestAllowances(
    GitHubModel
):
    """ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredPullRequestReviewsPropB
    ypassPullRequestAllowances

    Allow specific users, teams, or apps to bypass pull request requirements.
    """

    users: Missing[List[str]] = Field(
        default=UNSET,
        description="The list of user `login`s allowed to bypass pull request requirements.",
    )
    teams: Missing[List[str]] = Field(
        default=UNSET,
        description="The list of team `slug`s allowed to bypass pull request requirements.",
    )
    apps: Missing[List[str]] = Field(
        default=UNSET,
        description="The list of app `slug`s allowed to bypass pull request requirements.",
    )


class ReposOwnerRepoBranchesBranchProtectionPutBodyPropRestrictions(GitHubModel):
    """ReposOwnerRepoBranchesBranchProtectionPutBodyPropRestrictions

    Restrict who can push to the protected branch. User, app, and team
    `restrictions` are only available for organization-owned repositories. Set to
    `null` to disable.
    """

    users: List[str] = Field(description="The list of user `login`s with push access")
    teams: List[str] = Field(description="The list of team `slug`s with push access")
    apps: Missing[List[str]] = Field(
        default=UNSET, description="The list of app `slug`s with push access"
    )


model_rebuild(ReposOwnerRepoBranchesBranchProtectionPutBody)
model_rebuild(ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredStatusChecks)
model_rebuild(
    ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredStatusChecksPropChecksItems
)
model_rebuild(
    ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredPullRequestReviews
)
model_rebuild(
    ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredPullRequestReviewsPropDismissalRestrictions
)
model_rebuild(
    ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredPullRequestReviewsPropBypassPullRequestAllowances
)
model_rebuild(ReposOwnerRepoBranchesBranchProtectionPutBodyPropRestrictions)

__all__ = (
    "ReposOwnerRepoBranchesBranchProtectionPutBody",
    "ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredStatusChecks",
    "ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredStatusChecksPropChecksItems",
    "ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredPullRequestReviews",
    "ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredPullRequestReviewsPropDismissalRestrictions",
    "ReposOwnerRepoBranchesBranchProtectionPutBodyPropRequiredPullRequestReviewsPropBypassPullRequestAllowances",
    "ReposOwnerRepoBranchesBranchProtectionPutBodyPropRestrictions",
)
