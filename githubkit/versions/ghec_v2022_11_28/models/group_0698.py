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
from .group_0473 import SimpleInstallation
from .group_0474 import OrganizationSimpleWebhooks
from .group_0475 import RepositoryWebhooks
from .group_0501 import MergeGroup


class WebhookMergeGroupChecksRequested(GitHubModel):
    """WebhookMergeGroupChecksRequested"""

    action: Literal["checks_requested"] = Field()
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    merge_group: MergeGroup = Field(
        title="Merge Group",
        description="A group of pull requests that the merge queue has grouped together to be merged.",
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


model_rebuild(WebhookMergeGroupChecksRequested)

__all__ = ("WebhookMergeGroupChecksRequested",)
