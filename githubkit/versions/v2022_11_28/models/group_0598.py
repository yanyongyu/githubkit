"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0352 import SimpleInstallation
from .group_0355 import SimpleUserWebhooks
from .group_0353 import OrganizationSimpleWebhooks
from .group_0360 import PersonalAccessTokenRequest


class WebhookPersonalAccessTokenRequestCreated(GitHubModel):
    """personal_access_token_request created event"""

    action: Literal["created"] = Field()
    personal_access_token_request: PersonalAccessTokenRequest = Field(
        title="Personal Access Token Request",
        description="Details of a Personal Access Token Request.",
    )
    organization: OrganizationSimpleWebhooks = Field(
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )
    installation: SimpleInstallation = Field(
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )


model_rebuild(WebhookPersonalAccessTokenRequestCreated)

__all__ = ("WebhookPersonalAccessTokenRequestCreated",)
