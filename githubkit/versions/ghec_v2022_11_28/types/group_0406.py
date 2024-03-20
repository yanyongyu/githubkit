"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0390 import EnterpriseWebhooksType
from .group_0391 import SimpleInstallationType
from .group_0392 import OrganizationSimpleWebhooksType
from .group_0393 import RepositoryWebhooksType
from .group_0394 import SimpleUserWebhooksType


class WebhookBranchProtectionRuleDeletedType(TypedDict):
    """branch protection rule deleted event"""

    action: Literal["deleted"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    rule: WebhookBranchProtectionRuleDeletedPropRuleType
    sender: SimpleUserWebhooksType


class WebhookBranchProtectionRuleDeletedPropRuleType(TypedDict):
    """branch protection rule

    The branch protection rule. Includes a `name` and all the [branch protection
    settings](https://docs.github.com/enterprise-cloud@latest//github/administering-
    a-repository/defining-the-mergeability-of-pull-requests/about-protected-
    branches#about-branch-protection-settings) applied to branches that match the
    name. Binary settings are boolean. Multi-level configurations are one of `off`,
    `non_admins`, or `everyone`. Actor and build lists are arrays of strings.
    """

    admin_enforced: bool
    allow_deletions_enforcement_level: Literal["off", "non_admins", "everyone"]
    allow_force_pushes_enforcement_level: Literal["off", "non_admins", "everyone"]
    authorized_actor_names: List[str]
    authorized_actors_only: bool
    authorized_dismissal_actors_only: bool
    create_protected: NotRequired[bool]
    created_at: datetime
    dismiss_stale_reviews_on_push: bool
    id: int
    ignore_approvals_from_contributors: bool
    linear_history_requirement_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ]
    merge_queue_enforcement_level: Literal["off", "non_admins", "everyone"]
    name: str
    pull_request_reviews_enforcement_level: Literal["off", "non_admins", "everyone"]
    repository_id: int
    require_code_owner_review: bool
    require_last_push_approval: NotRequired[bool]
    required_approving_review_count: int
    required_conversation_resolution_level: Literal["off", "non_admins", "everyone"]
    required_deployments_enforcement_level: Literal["off", "non_admins", "everyone"]
    required_status_checks: List[str]
    required_status_checks_enforcement_level: Literal["off", "non_admins", "everyone"]
    signature_requirement_enforcement_level: Literal["off", "non_admins", "everyone"]
    strict_required_status_checks_policy: bool
    updated_at: datetime


__all__ = (
    "WebhookBranchProtectionRuleDeletedType",
    "WebhookBranchProtectionRuleDeletedPropRuleType",
)
