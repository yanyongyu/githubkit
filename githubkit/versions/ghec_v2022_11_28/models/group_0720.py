"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0402 import EnterpriseWebhooks
from .group_0403 import SimpleInstallation
from .group_0405 import RepositoryWebhooks
from .group_0406 import SimpleUserWebhooks
from .group_0404 import OrganizationSimpleWebhooks


class WebhookRepositoryDispatchSample(GitHubModel):
    """repository_dispatch event"""

    action: str = Field(
        description="The `event_type` that was specified in the `POST /repos/{owner}/{repo}/dispatches` request body."
    )
    branch: str = Field()
    client_payload: Union[WebhookRepositoryDispatchSamplePropClientPayload, None] = (
        Field(
            description="The `client_payload` that was specified in the `POST /repos/{owner}/{repo}/dispatches` request body."
        )
    )
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."\n',
    )
    installation: SimpleInstallation = Field(
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
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookRepositoryDispatchSamplePropClientPayload(ExtraGitHubModel):
    """WebhookRepositoryDispatchSamplePropClientPayload

    The `client_payload` that was specified in the `POST
    /repos/{owner}/{repo}/dispatches` request body.
    """


model_rebuild(WebhookRepositoryDispatchSample)
model_rebuild(WebhookRepositoryDispatchSamplePropClientPayload)

__all__ = (
    "WebhookRepositoryDispatchSample",
    "WebhookRepositoryDispatchSamplePropClientPayload",
)
