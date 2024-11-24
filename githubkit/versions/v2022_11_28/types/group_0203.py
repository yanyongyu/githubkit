"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired

from .group_0194 import BranchRestrictionPolicyType
from .group_0204 import ProtectedBranchPropRequiredPullRequestReviewsType


class ProtectedBranchType(TypedDict):
    """Protected Branch

    Branch protections protect branches
    """

    url: str
    required_status_checks: NotRequired[StatusCheckPolicyType]
    required_pull_request_reviews: NotRequired[
        ProtectedBranchPropRequiredPullRequestReviewsType
    ]
    required_signatures: NotRequired[ProtectedBranchPropRequiredSignaturesType]
    enforce_admins: NotRequired[ProtectedBranchPropEnforceAdminsType]
    required_linear_history: NotRequired[ProtectedBranchPropRequiredLinearHistoryType]
    allow_force_pushes: NotRequired[ProtectedBranchPropAllowForcePushesType]
    allow_deletions: NotRequired[ProtectedBranchPropAllowDeletionsType]
    restrictions: NotRequired[BranchRestrictionPolicyType]
    required_conversation_resolution: NotRequired[
        ProtectedBranchPropRequiredConversationResolutionType
    ]
    block_creations: NotRequired[ProtectedBranchPropBlockCreationsType]
    lock_branch: NotRequired[ProtectedBranchPropLockBranchType]
    allow_fork_syncing: NotRequired[ProtectedBranchPropAllowForkSyncingType]


class ProtectedBranchPropRequiredSignaturesType(TypedDict):
    """ProtectedBranchPropRequiredSignatures"""

    url: str
    enabled: bool


class ProtectedBranchPropEnforceAdminsType(TypedDict):
    """ProtectedBranchPropEnforceAdmins"""

    url: str
    enabled: bool


class ProtectedBranchPropRequiredLinearHistoryType(TypedDict):
    """ProtectedBranchPropRequiredLinearHistory"""

    enabled: bool


class ProtectedBranchPropAllowForcePushesType(TypedDict):
    """ProtectedBranchPropAllowForcePushes"""

    enabled: bool


class ProtectedBranchPropAllowDeletionsType(TypedDict):
    """ProtectedBranchPropAllowDeletions"""

    enabled: bool


class ProtectedBranchPropRequiredConversationResolutionType(TypedDict):
    """ProtectedBranchPropRequiredConversationResolution"""

    enabled: NotRequired[bool]


class ProtectedBranchPropBlockCreationsType(TypedDict):
    """ProtectedBranchPropBlockCreations"""

    enabled: bool


class ProtectedBranchPropLockBranchType(TypedDict):
    """ProtectedBranchPropLockBranch

    Whether to set the branch as read-only. If this is true, users will not be able
    to push to the branch.
    """

    enabled: NotRequired[bool]


class ProtectedBranchPropAllowForkSyncingType(TypedDict):
    """ProtectedBranchPropAllowForkSyncing

    Whether users can pull changes from upstream when the branch is locked. Set to
    `true` to allow fork syncing. Set to `false` to prevent fork syncing.
    """

    enabled: NotRequired[bool]


class StatusCheckPolicyType(TypedDict):
    """Status Check Policy

    Status Check Policy
    """

    url: str
    strict: bool
    contexts: list[str]
    checks: list[StatusCheckPolicyPropChecksItemsType]
    contexts_url: str


class StatusCheckPolicyPropChecksItemsType(TypedDict):
    """StatusCheckPolicyPropChecksItems"""

    context: str
    app_id: Union[int, None]


__all__ = (
    "ProtectedBranchPropAllowDeletionsType",
    "ProtectedBranchPropAllowForcePushesType",
    "ProtectedBranchPropAllowForkSyncingType",
    "ProtectedBranchPropBlockCreationsType",
    "ProtectedBranchPropEnforceAdminsType",
    "ProtectedBranchPropLockBranchType",
    "ProtectedBranchPropRequiredConversationResolutionType",
    "ProtectedBranchPropRequiredLinearHistoryType",
    "ProtectedBranchPropRequiredSignaturesType",
    "ProtectedBranchType",
    "StatusCheckPolicyPropChecksItemsType",
    "StatusCheckPolicyType",
)
