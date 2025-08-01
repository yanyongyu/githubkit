"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0426 import EnterpriseWebhooks
from .group_0427 import SimpleInstallation
from .group_0428 import OrganizationSimpleWebhooks
from .group_0429 import RepositoryWebhooks


class WebhookSecretScanningScanCompleted(GitHubModel):
    """secret_scanning_scan completed event"""

    action: Literal["completed"] = Field()
    type: Literal["backfill", "custom-pattern-backfill", "pattern-version-backfill"] = (
        Field(description="What type of scan was completed")
    )
    source: Literal["git", "issues", "pull-requests", "discussions", "wiki"] = Field(
        description="What type of content was scanned"
    )
    started_at: datetime = Field(
        description="The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    completed_at: datetime = Field(
        description="The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    secret_types: Missing[Union[list[str], None]] = Field(
        default=UNSET,
        description="List of patterns that were updated. This will be empty for normal backfill scans or custom pattern updates",
    )
    custom_pattern_name: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="If the scan was triggered by a custom pattern update, this will be the name of the pattern that was updated",
    )
    custom_pattern_scope: Missing[
        Union[None, Literal["repository", "organization", "enterprise"]]
    ] = Field(
        default=UNSET,
        description="If the scan was triggered by a custom pattern update, this will be the scope of the pattern that was updated",
    )
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    sender: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )


model_rebuild(WebhookSecretScanningScanCompleted)

__all__ = ("WebhookSecretScanningScanCompleted",)
