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
from .group_0474 import WebhooksRepositoriesItems


class WebhookInstallationCreated(GitHubModel):
    """installation created event"""

    action: Literal["created"] = Field()
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
    repositories: Missing[list[WebhooksRepositoriesItems]] = Field(
        default=UNSET,
        description="An array of repository objects that the installation can access.",
    )
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    requester: Missing[Union[WebhooksUser, None]] = Field(default=UNSET, title="User")
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


model_rebuild(WebhookInstallationCreated)

__all__ = ("WebhookInstallationCreated",)
