"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0018 import Installation
from .group_0456 import EnterpriseWebhooks
from .group_0458 import OrganizationSimpleWebhooks
from .group_0459 import RepositoryWebhooks
from .group_0469 import WebhooksUser
from .group_0475 import WebhooksRepositoriesAddedItems


class WebhookInstallationRepositoriesRemoved(GitHubModel):
    """installation_repositories removed event"""

    action: Literal["removed"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."',
    )
    installation: Installation = Field(title="Installation", description="Installation")
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repositories_added: list[WebhooksRepositoriesAddedItems] = Field(
        description="An array of repository objects, which were added to the installation."
    )
    repositories_removed: list[
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
    requester: Union[WebhooksUser, None] = Field(title="User")
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItems(GitHubModel):
    """WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItems"""

    full_name: str = Field()
    id: int = Field(description="Unique identifier of the repository")
    name: str = Field(description="The name of the repository.")
    node_id: str = Field()
    private: bool = Field(description="Whether the repository is private or public.")


model_rebuild(WebhookInstallationRepositoriesRemoved)
model_rebuild(WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItems)

__all__ = (
    "WebhookInstallationRepositoriesRemoved",
    "WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItems",
)
