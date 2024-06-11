"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0407 import WebhooksRule
from .group_0402 import EnterpriseWebhooks
from .group_0403 import SimpleInstallation
from .group_0405 import RepositoryWebhooks
from .group_0406 import SimpleUserWebhooks
from .group_0404 import OrganizationSimpleWebhooks


class WebhookBranchProtectionRuleEdited(GitHubModel):
    """branch protection rule edited event"""

    action: Literal["edited"] = Field()
    changes: Missing[WebhookBranchProtectionRuleEditedPropChanges] = Field(
        default=UNSET,
        description="If the action was `edited`, the changes to the rule.",
    )
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    rule: WebhooksRule = Field(
        title="branch protection rule",
        description="The branch protection rule. Includes a `name` and all the [branch protection settings](https://docs.github.com/enterprise-cloud@latest//github/administering-a-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#about-branch-protection-settings) applied to branches that match the name. Binary settings are boolean. Multi-level configurations are one of `off`, `non_admins`, or `everyone`. Actor and build lists are arrays of strings.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookBranchProtectionRuleEditedPropChanges(GitHubModel):
    """WebhookBranchProtectionRuleEditedPropChanges

    If the action was `edited`, the changes to the rule.
    """

    admin_enforced: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced
    ] = Field(default=UNSET)
    authorized_actor_names: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames
    ] = Field(default=UNSET)
    authorized_actors_only: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly
    ] = Field(default=UNSET)
    authorized_dismissal_actors_only: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly
    ] = Field(default=UNSET)
    linear_history_requirement_enforcement_level: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevel
    ] = Field(default=UNSET)
    required_status_checks: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks
    ] = Field(default=UNSET)
    required_status_checks_enforcement_level: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevel
    ] = Field(default=UNSET)


class WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced(GitHubModel):
    """WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced"""

    from_: Union[bool, None] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames(GitHubModel):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames"""

    from_: List[str] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly(GitHubModel):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly"""

    from_: Union[bool, None] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly(
    GitHubModel
):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly"""

    from_: Union[bool, None] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevel(
    GitHubModel
):
    """WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcem
    entLevel
    """

    from_: Literal["off", "non_admins", "everyone"] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks(GitHubModel):
    """WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks"""

    from_: List[str] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevel(
    GitHubModel
):
    """WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementL
    evel
    """

    from_: Literal["off", "non_admins", "everyone"] = Field(alias="from")


model_rebuild(WebhookBranchProtectionRuleEdited)
model_rebuild(WebhookBranchProtectionRuleEditedPropChanges)
model_rebuild(WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced)
model_rebuild(WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames)
model_rebuild(WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly)
model_rebuild(
    WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly
)
model_rebuild(
    WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevel
)
model_rebuild(WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks)
model_rebuild(
    WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevel
)

__all__ = (
    "WebhookBranchProtectionRuleEdited",
    "WebhookBranchProtectionRuleEditedPropChanges",
    "WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly",
    "WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevel",
    "WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks",
    "WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevel",
)
