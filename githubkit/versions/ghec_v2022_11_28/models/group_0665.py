"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0415 import EnterpriseWebhooks
from .group_0416 import SimpleInstallation
from .group_0418 import RepositoryWebhooks
from .group_0419 import SimpleUserWebhooks
from .group_0451 import WebhooksProjectColumn
from .group_0417 import OrganizationSimpleWebhooks


class WebhookProjectColumnEdited(GitHubModel):
    """project_column edited event"""

    action: Literal["edited"] = Field()
    changes: WebhookProjectColumnEditedPropChanges = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."',
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
    project_column: WebhooksProjectColumn = Field(title="Project Column")
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


class WebhookProjectColumnEditedPropChanges(GitHubModel):
    """WebhookProjectColumnEditedPropChanges"""

    name: Missing[WebhookProjectColumnEditedPropChangesPropName] = Field(default=UNSET)


class WebhookProjectColumnEditedPropChangesPropName(GitHubModel):
    """WebhookProjectColumnEditedPropChangesPropName"""

    from_: str = Field(alias="from")


model_rebuild(WebhookProjectColumnEdited)
model_rebuild(WebhookProjectColumnEditedPropChanges)
model_rebuild(WebhookProjectColumnEditedPropChangesPropName)

__all__ = (
    "WebhookProjectColumnEdited",
    "WebhookProjectColumnEditedPropChanges",
    "WebhookProjectColumnEditedPropChangesPropName",
)
