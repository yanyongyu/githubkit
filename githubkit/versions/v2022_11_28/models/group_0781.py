"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0355 import EnterpriseWebhooks
from .group_0356 import SimpleInstallation
from .group_0358 import RepositoryWebhooks
from .group_0359 import SimpleUserWebhooks
from .group_0357 import OrganizationSimpleWebhooks


class WebhookTeamAdd(GitHubModel):
    """team_add event"""

    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
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
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )
    team: WebhookTeamAddPropTeam = Field(
        title="Team",
        description="Groups of organization members that gives permissions on specified repositories.",
    )


class WebhookTeamAddPropTeam(GitHubModel):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: Missing[bool] = Field(default=UNSET)
    description: Missing[Union[str, None]] = Field(
        default=UNSET, description="Description of the team"
    )
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field(description="Unique identifier of the team")
    members_url: Missing[str] = Field(default=UNSET)
    name: str = Field(description="Name of the team")
    node_id: Missing[str] = Field(default=UNSET)
    parent: Missing[Union[WebhookTeamAddPropTeamPropParent, None]] = Field(
        default=UNSET
    )
    permission: Missing[str] = Field(
        default=UNSET,
        description="Permission that the team will have for its repositories",
    )
    privacy: Missing[Literal["open", "closed", "secret"]] = Field(default=UNSET)
    notification_setting: Missing[
        Literal["notifications_enabled", "notifications_disabled"]
    ] = Field(
        default=UNSET,
        description="Whether team members will receive notifications when their team is @mentioned",
    )
    repositories_url: Missing[str] = Field(default=UNSET)
    slug: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET, description="URL for the team")


class WebhookTeamAddPropTeamPropParent(GitHubModel):
    """WebhookTeamAddPropTeamPropParent"""

    description: Union[str, None] = Field(description="Description of the team")
    html_url: str = Field()
    id: int = Field(description="Unique identifier of the team")
    members_url: str = Field()
    name: str = Field(description="Name of the team")
    node_id: str = Field()
    permission: str = Field(
        description="Permission that the team will have for its repositories"
    )
    privacy: Literal["open", "closed", "secret"] = Field()
    notification_setting: Literal["notifications_enabled", "notifications_disabled"] = (
        Field(
            description="Whether team members will receive notifications when their team is @mentioned"
        )
    )
    repositories_url: str = Field()
    slug: str = Field()
    url: str = Field(description="URL for the team")


model_rebuild(WebhookTeamAdd)
model_rebuild(WebhookTeamAddPropTeam)
model_rebuild(WebhookTeamAddPropTeamPropParent)

__all__ = (
    "WebhookTeamAdd",
    "WebhookTeamAddPropTeam",
    "WebhookTeamAddPropTeamPropParent",
)
