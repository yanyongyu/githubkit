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

from .group_0015 import Installation
from .group_0351 import EnterpriseWebhooks
from .group_0354 import RepositoryWebhooks
from .group_0355 import SimpleUserWebhooks
from .group_0353 import OrganizationSimpleWebhooks


class WebhookInstallationNewPermissionsAccepted(GitHubModel):
    """installation new_permissions_accepted event"""

    action: Literal["new_permissions_accepted"] = Field()
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
    repositories: Missing[
        List[WebhookInstallationNewPermissionsAcceptedPropRepositoriesItems]
    ] = Field(
        default=UNSET,
        description="An array of repository objects that the installation can access.",
    )
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    requester: Missing[None] = Field(default=UNSET)
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookInstallationNewPermissionsAcceptedPropRepositoriesItems(GitHubModel):
    """WebhookInstallationNewPermissionsAcceptedPropRepositoriesItems"""

    full_name: str = Field()
    id: int = Field(description="Unique identifier of the repository")
    name: str = Field(description="The name of the repository.")
    node_id: str = Field()
    private: bool = Field(description="Whether the repository is private or public.")


model_rebuild(WebhookInstallationNewPermissionsAccepted)
model_rebuild(WebhookInstallationNewPermissionsAcceptedPropRepositoriesItems)

__all__ = (
    "WebhookInstallationNewPermissionsAccepted",
    "WebhookInstallationNewPermissionsAcceptedPropRepositoriesItems",
)
