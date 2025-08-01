"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0223 import ProtectedBranchPullRequestReview
from .group_0225 import BranchRestrictionPolicy


class BranchProtection(GitHubModel):
    """Branch Protection

    Branch Protection
    """

    url: Missing[str] = Field(default=UNSET)
    enabled: Missing[bool] = Field(default=UNSET)
    required_status_checks: Missing[ProtectedBranchRequiredStatusCheck] = Field(
        default=UNSET,
        title="Protected Branch Required Status Check",
        description="Protected Branch Required Status Check",
    )
    enforce_admins: Missing[ProtectedBranchAdminEnforced] = Field(
        default=UNSET,
        title="Protected Branch Admin Enforced",
        description="Protected Branch Admin Enforced",
    )
    required_pull_request_reviews: Missing[ProtectedBranchPullRequestReview] = Field(
        default=UNSET,
        title="Protected Branch Pull Request Review",
        description="Protected Branch Pull Request Review",
    )
    restrictions: Missing[BranchRestrictionPolicy] = Field(
        default=UNSET,
        title="Branch Restriction Policy",
        description="Branch Restriction Policy",
    )
    required_linear_history: Missing[BranchProtectionPropRequiredLinearHistory] = Field(
        default=UNSET
    )
    allow_force_pushes: Missing[BranchProtectionPropAllowForcePushes] = Field(
        default=UNSET
    )
    allow_deletions: Missing[BranchProtectionPropAllowDeletions] = Field(default=UNSET)
    block_creations: Missing[BranchProtectionPropBlockCreations] = Field(default=UNSET)
    required_conversation_resolution: Missing[
        BranchProtectionPropRequiredConversationResolution
    ] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    protection_url: Missing[str] = Field(default=UNSET)
    required_signatures: Missing[BranchProtectionPropRequiredSignatures] = Field(
        default=UNSET
    )
    lock_branch: Missing[BranchProtectionPropLockBranch] = Field(
        default=UNSET,
        description="Whether to set the branch as read-only. If this is true, users will not be able to push to the branch.",
    )
    allow_fork_syncing: Missing[BranchProtectionPropAllowForkSyncing] = Field(
        default=UNSET,
        description="Whether users can pull changes from upstream when the branch is locked. Set to `true` to allow fork syncing. Set to `false` to prevent fork syncing.",
    )


class ProtectedBranchAdminEnforced(GitHubModel):
    """Protected Branch Admin Enforced

    Protected Branch Admin Enforced
    """

    url: str = Field()
    enabled: bool = Field()


class BranchProtectionPropRequiredLinearHistory(GitHubModel):
    """BranchProtectionPropRequiredLinearHistory"""

    enabled: Missing[bool] = Field(default=UNSET)


class BranchProtectionPropAllowForcePushes(GitHubModel):
    """BranchProtectionPropAllowForcePushes"""

    enabled: Missing[bool] = Field(default=UNSET)


class BranchProtectionPropAllowDeletions(GitHubModel):
    """BranchProtectionPropAllowDeletions"""

    enabled: Missing[bool] = Field(default=UNSET)


class BranchProtectionPropBlockCreations(GitHubModel):
    """BranchProtectionPropBlockCreations"""

    enabled: Missing[bool] = Field(default=UNSET)


class BranchProtectionPropRequiredConversationResolution(GitHubModel):
    """BranchProtectionPropRequiredConversationResolution"""

    enabled: Missing[bool] = Field(default=UNSET)


class BranchProtectionPropRequiredSignatures(GitHubModel):
    """BranchProtectionPropRequiredSignatures"""

    url: str = Field()
    enabled: bool = Field()


class BranchProtectionPropLockBranch(GitHubModel):
    """BranchProtectionPropLockBranch

    Whether to set the branch as read-only. If this is true, users will not be able
    to push to the branch.
    """

    enabled: Missing[bool] = Field(default=UNSET)


class BranchProtectionPropAllowForkSyncing(GitHubModel):
    """BranchProtectionPropAllowForkSyncing

    Whether users can pull changes from upstream when the branch is locked. Set to
    `true` to allow fork syncing. Set to `false` to prevent fork syncing.
    """

    enabled: Missing[bool] = Field(default=UNSET)


class ProtectedBranchRequiredStatusCheck(GitHubModel):
    """Protected Branch Required Status Check

    Protected Branch Required Status Check
    """

    url: Missing[str] = Field(default=UNSET)
    enforcement_level: Missing[str] = Field(default=UNSET)
    contexts: list[str] = Field()
    checks: list[ProtectedBranchRequiredStatusCheckPropChecksItems] = Field()
    contexts_url: Missing[str] = Field(default=UNSET)
    strict: Missing[bool] = Field(default=UNSET)


class ProtectedBranchRequiredStatusCheckPropChecksItems(GitHubModel):
    """ProtectedBranchRequiredStatusCheckPropChecksItems"""

    context: str = Field()
    app_id: Union[int, None] = Field()


model_rebuild(BranchProtection)
model_rebuild(ProtectedBranchAdminEnforced)
model_rebuild(BranchProtectionPropRequiredLinearHistory)
model_rebuild(BranchProtectionPropAllowForcePushes)
model_rebuild(BranchProtectionPropAllowDeletions)
model_rebuild(BranchProtectionPropBlockCreations)
model_rebuild(BranchProtectionPropRequiredConversationResolution)
model_rebuild(BranchProtectionPropRequiredSignatures)
model_rebuild(BranchProtectionPropLockBranch)
model_rebuild(BranchProtectionPropAllowForkSyncing)
model_rebuild(ProtectedBranchRequiredStatusCheck)
model_rebuild(ProtectedBranchRequiredStatusCheckPropChecksItems)

__all__ = (
    "BranchProtection",
    "BranchProtectionPropAllowDeletions",
    "BranchProtectionPropAllowForcePushes",
    "BranchProtectionPropAllowForkSyncing",
    "BranchProtectionPropBlockCreations",
    "BranchProtectionPropLockBranch",
    "BranchProtectionPropRequiredConversationResolution",
    "BranchProtectionPropRequiredLinearHistory",
    "BranchProtectionPropRequiredSignatures",
    "ProtectedBranchAdminEnforced",
    "ProtectedBranchRequiredStatusCheck",
    "ProtectedBranchRequiredStatusCheckPropChecksItems",
)
