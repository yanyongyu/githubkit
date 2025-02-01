"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0401 import OrganizationSimpleWebhooks
from .group_0402 import RepositoryWebhooks
from .group_0632 import WebhookPingPropHook


class WebhookPing(GitHubModel):
    """WebhookPing"""

    hook: Missing[WebhookPingPropHook] = Field(
        default=UNSET, title="Webhook", description="The webhook that is being pinged"
    )
    hook_id: Missing[int] = Field(
        default=UNSET, description="The ID of the webhook that triggered the ping."
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
    sender: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )
    zen: Missing[str] = Field(default=UNSET, description="Random string of GitHub zen.")


model_rebuild(WebhookPing)

__all__ = ("WebhookPing",)
