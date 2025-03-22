"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0418 import EnterpriseWebhooks
from .group_0419 import SimpleInstallation
from .group_0420 import OrganizationSimpleWebhooks
from .group_0448 import PersonalAccessTokenRequest


class WebhookPersonalAccessTokenRequestDenied(GitHubModel):
    """personal_access_token_request denied event"""

    action: Literal["denied"] = Field()
    personal_access_token_request: PersonalAccessTokenRequest = Field(
        title="Personal Access Token Request",
        description="Details of a Personal Access Token Request.",
    )
    organization: OrganizationSimpleWebhooks = Field(
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."',
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    installation: SimpleInstallation = Field(
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )


model_rebuild(WebhookPersonalAccessTokenRequestDenied)

__all__ = ("WebhookPersonalAccessTokenRequestDenied",)
