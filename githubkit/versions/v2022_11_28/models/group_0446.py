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

from .group_0015 import Installation
from .group_0357 import EnterpriseWebhooks
from .group_0360 import RepositoryWebhooks
from .group_0361 import SimpleUserWebhooks
from .group_0359 import OrganizationSimpleWebhooks


class WebhookInstallationRepositoriesRemoved(GitHubModel):
    """installation_repositories removed event"""

    action: Literal["removed"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Installation = Field(title="Installation", description="Installation")
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repositories_added: List[
        WebhookInstallationRepositoriesRemovedPropRepositoriesAddedItems
    ] = Field(
        description="An array of repository objects, which were added to the installation."
    )
    repositories_removed: List[
        WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItems
    ] = Field(
        description="An array of repository objects, which were removed from the installation."
    )
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    repository_selection: Literal["all", "selected"] = Field(
        description="Describe whether all repositories have been selected or there's a selection involved"
    )
    requester: Union[WebhookInstallationRepositoriesRemovedPropRequester, None] = Field(
        title="User"
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookInstallationRepositoriesRemovedPropRepositoriesAddedItems(GitHubModel):
    """WebhookInstallationRepositoriesRemovedPropRepositoriesAddedItems"""

    full_name: str = Field()
    id: int = Field(description="Unique identifier of the repository")
    name: str = Field(description="The name of the repository.")
    node_id: str = Field()
    private: bool = Field(description="Whether the repository is private or public.")


class WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItems(GitHubModel):
    """WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItems"""

    full_name: str = Field()
    id: int = Field(description="Unique identifier of the repository")
    name: str = Field(description="The name of the repository.")
    node_id: str = Field()
    private: bool = Field(description="Whether the repository is private or public.")


class WebhookInstallationRepositoriesRemovedPropRequester(GitHubModel):
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


model_rebuild(WebhookInstallationRepositoriesRemoved)
model_rebuild(WebhookInstallationRepositoriesRemovedPropRepositoriesAddedItems)
model_rebuild(WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItems)
model_rebuild(WebhookInstallationRepositoriesRemovedPropRequester)

__all__ = (
    "WebhookInstallationRepositoriesRemoved",
    "WebhookInstallationRepositoriesRemovedPropRepositoriesAddedItems",
    "WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItems",
    "WebhookInstallationRepositoriesRemovedPropRequester",
)
