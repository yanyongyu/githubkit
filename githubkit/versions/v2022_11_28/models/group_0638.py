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

from .group_0002 import SimpleUser
from .group_0386 import SimpleInstallation
from .group_0387 import OrganizationSimpleWebhooks
from .group_0421 import ProjectsV2Item


class WebhookProjectsV2ItemConverted(GitHubModel):
    """Projects v2 Item Converted Event"""

    action: Literal["converted"] = Field()
    changes: WebhookProjectsV2ItemConvertedPropChanges = Field()
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: OrganizationSimpleWebhooks = Field(
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    projects_v2_item: ProjectsV2Item = Field(
        title="Projects v2 Item", description="An item belonging to a project"
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class WebhookProjectsV2ItemConvertedPropChanges(GitHubModel):
    """WebhookProjectsV2ItemConvertedPropChanges"""

    content_type: Missing[WebhookProjectsV2ItemConvertedPropChangesPropContentType] = (
        Field(default=UNSET)
    )


class WebhookProjectsV2ItemConvertedPropChangesPropContentType(GitHubModel):
    """WebhookProjectsV2ItemConvertedPropChangesPropContentType"""

    from_: Missing[Union[str, None]] = Field(default=UNSET, alias="from")
    to: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookProjectsV2ItemConverted)
model_rebuild(WebhookProjectsV2ItemConvertedPropChanges)
model_rebuild(WebhookProjectsV2ItemConvertedPropChangesPropContentType)

__all__ = (
    "WebhookProjectsV2ItemConverted",
    "WebhookProjectsV2ItemConvertedPropChanges",
    "WebhookProjectsV2ItemConvertedPropChangesPropContentType",
)
