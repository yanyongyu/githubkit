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

from .group_0357 import EnterpriseWebhooks
from .group_0358 import SimpleInstallation
from .group_0359 import OrganizationSimpleWebhooks
from .group_0360 import RepositoryWebhooks
from .group_0361 import SimpleUserWebhooks


class WebhookInstallationTargetRenamed(GitHubModel):
    """WebhookInstallationTargetRenamed"""

    account: WebhookInstallationTargetRenamedPropAccount = Field()
    action: Literal["renamed"] = Field()
    changes: WebhookInstallationTargetRenamedPropChanges = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
    )
    installation: SimpleInstallation = Field(
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: Missing[SimpleUserWebhooks] = Field(
        default=UNSET,
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )
    target_type: str = Field()


class WebhookInstallationTargetRenamedPropAccount(GitHubModel):
    """WebhookInstallationTargetRenamedPropAccount"""

    archived_at: Missing[Union[str, None]] = Field(default=UNSET)
    avatar_url: str = Field()
    created_at: Missing[str] = Field(default=UNSET)
    description: Missing[None] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers: Missing[int] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following: Missing[int] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    has_organization_projects: Missing[bool] = Field(default=UNSET)
    has_repository_projects: Missing[bool] = Field(default=UNSET)
    hooks_url: Missing[str] = Field(default=UNSET)
    html_url: str = Field()
    id: int = Field()
    is_verified: Missing[bool] = Field(default=UNSET)
    issues_url: Missing[str] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    members_url: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    node_id: str = Field()
    organizations_url: Missing[str] = Field(default=UNSET)
    public_gists: Missing[int] = Field(default=UNSET)
    public_members_url: Missing[str] = Field(default=UNSET)
    public_repos: Missing[int] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    slug: Missing[str] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    website_url: Missing[None] = Field(default=UNSET)


class WebhookInstallationTargetRenamedPropChanges(GitHubModel):
    """WebhookInstallationTargetRenamedPropChanges"""

    login: Missing[WebhookInstallationTargetRenamedPropChangesPropLogin] = Field(
        default=UNSET
    )
    slug: Missing[WebhookInstallationTargetRenamedPropChangesPropSlug] = Field(
        default=UNSET
    )


class WebhookInstallationTargetRenamedPropChangesPropLogin(GitHubModel):
    """WebhookInstallationTargetRenamedPropChangesPropLogin"""

    from_: str = Field(alias="from")


class WebhookInstallationTargetRenamedPropChangesPropSlug(GitHubModel):
    """WebhookInstallationTargetRenamedPropChangesPropSlug"""

    from_: str = Field(alias="from")


model_rebuild(WebhookInstallationTargetRenamed)
model_rebuild(WebhookInstallationTargetRenamedPropAccount)
model_rebuild(WebhookInstallationTargetRenamedPropChanges)
model_rebuild(WebhookInstallationTargetRenamedPropChangesPropLogin)
model_rebuild(WebhookInstallationTargetRenamedPropChangesPropSlug)

__all__ = (
    "WebhookInstallationTargetRenamed",
    "WebhookInstallationTargetRenamedPropAccount",
    "WebhookInstallationTargetRenamedPropChanges",
    "WebhookInstallationTargetRenamedPropChangesPropLogin",
    "WebhookInstallationTargetRenamedPropChangesPropSlug",
)
