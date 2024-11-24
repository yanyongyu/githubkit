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

from .group_0002 import SimpleUser
from .group_0384 import EnterpriseWebhooks
from .group_0385 import SimpleInstallation
from .group_0386 import OrganizationSimpleWebhooks
from .group_0387 import RepositoryWebhooks


class WebhookPageBuild(GitHubModel):
    """page_build event"""

    build: WebhookPageBuildPropBuild = Field(
        description="The [List GitHub Pages builds](https://docs.github.com/rest/pages/pages#list-github-pages-builds) itself."
    )
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."',
    )
    id: int = Field()
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
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class WebhookPageBuildPropBuild(GitHubModel):
    """WebhookPageBuildPropBuild

    The [List GitHub Pages builds](https://docs.github.com/rest/pages/pages#list-
    github-pages-builds) itself.
    """

    commit: Union[str, None] = Field()
    created_at: str = Field()
    duration: int = Field()
    error: WebhookPageBuildPropBuildPropError = Field()
    pusher: Union[WebhookPageBuildPropBuildPropPusher, None] = Field(title="User")
    status: str = Field()
    updated_at: str = Field()
    url: str = Field()


class WebhookPageBuildPropBuildPropError(GitHubModel):
    """WebhookPageBuildPropBuildPropError"""

    message: Union[str, None] = Field()


class WebhookPageBuildPropBuildPropPusher(GitHubModel):
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
    user_view_type: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookPageBuild)
model_rebuild(WebhookPageBuildPropBuild)
model_rebuild(WebhookPageBuildPropBuildPropError)
model_rebuild(WebhookPageBuildPropBuildPropPusher)

__all__ = (
    "WebhookPageBuild",
    "WebhookPageBuildPropBuild",
    "WebhookPageBuildPropBuildPropError",
    "WebhookPageBuildPropBuildPropPusher",
)
