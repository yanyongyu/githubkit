"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0418 import EnterpriseWebhooksType
from .group_0419 import SimpleInstallationType
from .group_0420 import OrganizationSimpleWebhooksType
from .group_0421 import RepositoryWebhooksType
from .group_0422 import WebhooksRuleType


class WebhookBranchProtectionRuleEditedType(TypedDict):
    """branch protection rule edited event"""

    action: Literal["edited"]
    changes: NotRequired[WebhookBranchProtectionRuleEditedPropChangesType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    rule: WebhooksRuleType
    sender: SimpleUserType


class WebhookBranchProtectionRuleEditedPropChangesType(TypedDict):
    """WebhookBranchProtectionRuleEditedPropChanges

    If the action was `edited`, the changes to the rule.
    """

    admin_enforced: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforcedType
    ]
    authorized_actor_names: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNamesType
    ]
    authorized_actors_only: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnlyType
    ]
    authorized_dismissal_actors_only: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnlyType
    ]
    linear_history_requirement_enforcement_level: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevelType
    ]
    lock_branch_enforcement_level: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropLockBranchEnforcementLevelType
    ]
    lock_allows_fork_sync: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropLockAllowsForkSyncType
    ]
    pull_request_reviews_enforcement_level: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropPullRequestReviewsEnforcementLevelType
    ]
    require_last_push_approval: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropRequireLastPushApprovalType
    ]
    required_status_checks: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksType
    ]
    required_status_checks_enforcement_level: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevelType
    ]


class WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforcedType(TypedDict):
    """WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced"""

    from_: Union[bool, None]


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNamesType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames"""

    from_: list[str]


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnlyType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly"""

    from_: Union[bool, None]


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnlyType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly"""

    from_: Union[bool, None]


class WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevelType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcem
    entLevel
    """

    from_: Literal["off", "non_admins", "everyone"]


class WebhookBranchProtectionRuleEditedPropChangesPropLockBranchEnforcementLevelType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropLockBranchEnforcementLevel"""

    from_: Literal["off", "non_admins", "everyone"]


class WebhookBranchProtectionRuleEditedPropChangesPropLockAllowsForkSyncType(TypedDict):
    """WebhookBranchProtectionRuleEditedPropChangesPropLockAllowsForkSync"""

    from_: Union[bool, None]


class WebhookBranchProtectionRuleEditedPropChangesPropPullRequestReviewsEnforcementLevelType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropPullRequestReviewsEnforcementLev
    el
    """

    from_: Literal["off", "non_admins", "everyone"]


class WebhookBranchProtectionRuleEditedPropChangesPropRequireLastPushApprovalType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropRequireLastPushApproval"""

    from_: Union[bool, None]


class WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks"""

    from_: list[str]


class WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevelType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementL
    evel
    """

    from_: Literal["off", "non_admins", "everyone"]


__all__ = (
    "WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforcedType",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNamesType",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnlyType",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnlyType",
    "WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevelType",
    "WebhookBranchProtectionRuleEditedPropChangesPropLockAllowsForkSyncType",
    "WebhookBranchProtectionRuleEditedPropChangesPropLockBranchEnforcementLevelType",
    "WebhookBranchProtectionRuleEditedPropChangesPropPullRequestReviewsEnforcementLevelType",
    "WebhookBranchProtectionRuleEditedPropChangesPropRequireLastPushApprovalType",
    "WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevelType",
    "WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksType",
    "WebhookBranchProtectionRuleEditedPropChangesType",
    "WebhookBranchProtectionRuleEditedType",
)
