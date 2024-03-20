"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0390 import EnterpriseWebhooks
from .group_0391 import SimpleInstallation
from .group_0392 import OrganizationSimpleWebhooks
from .group_0393 import RepositoryWebhooks


class WebhookMembershipAdded(GitHubModel):
    """membership added event"""

    action: Literal["added"] = Field()
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
    member: Union[WebhookMembershipAddedPropMember, None] = Field(title="User")
    organization: OrganizationSimpleWebhooks = Field(
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    scope: Literal["team"] = Field(
        description="The scope of the membership. Currently, can only be `team`."
    )
    sender: Union[WebhookMembershipAddedPropSender, None] = Field(title="User")
    team: WebhookMembershipAddedPropTeam = Field(
        title="Team",
        description="Groups of organization members that gives permissions on specified repositories.",
    )


class WebhookMembershipAddedPropMember(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookMembershipAddedPropSender(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookMembershipAddedPropTeam(GitHubModel):
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
    parent: Missing[Union[WebhookMembershipAddedPropTeamPropParent, None]] = Field(
        default=UNSET
    )
    permission: Missing[str] = Field(
        default=UNSET,
        description="Permission that the team will have for its repositories",
    )
    privacy: Missing[Literal["open", "closed", "secret"]] = Field(default=UNSET)
    notification_setting: Missing[
        Literal["notifications_enabled", "notifications_disabled"]
    ] = Field(default=UNSET)
    repositories_url: Missing[str] = Field(default=UNSET)
    slug: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET, description="URL for the team")


class WebhookMembershipAddedPropTeamPropParent(GitHubModel):
    """WebhookMembershipAddedPropTeamPropParent"""

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
    notification_setting: Literal[
        "notifications_enabled", "notifications_disabled"
    ] = Field(
        description="Whether team members will receive notifications when their team is @mentioned"
    )
    repositories_url: str = Field()
    slug: str = Field()
    url: str = Field(description="URL for the team")


model_rebuild(WebhookMembershipAdded)
model_rebuild(WebhookMembershipAddedPropMember)
model_rebuild(WebhookMembershipAddedPropSender)
model_rebuild(WebhookMembershipAddedPropTeam)
model_rebuild(WebhookMembershipAddedPropTeamPropParent)

__all__ = (
    "WebhookMembershipAdded",
    "WebhookMembershipAddedPropMember",
    "WebhookMembershipAddedPropSender",
    "WebhookMembershipAddedPropTeam",
    "WebhookMembershipAddedPropTeamPropParent",
)
