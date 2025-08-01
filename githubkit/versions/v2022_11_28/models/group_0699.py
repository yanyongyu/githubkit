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
from .group_0427 import SimpleInstallation
from .group_0428 import OrganizationSimpleWebhooks
from .group_0462 import ProjectsV2Item


class WebhookProjectsV2ItemReordered(GitHubModel):
    """Projects v2 Item Reordered Event"""

    action: Literal["reordered"] = Field()
    changes: WebhookProjectsV2ItemReorderedPropChanges = Field()
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


class WebhookProjectsV2ItemReorderedPropChanges(GitHubModel):
    """WebhookProjectsV2ItemReorderedPropChanges"""

    previous_projects_v2_item_node_id: Missing[
        WebhookProjectsV2ItemReorderedPropChangesPropPreviousProjectsV2ItemNodeId
    ] = Field(default=UNSET)


class WebhookProjectsV2ItemReorderedPropChangesPropPreviousProjectsV2ItemNodeId(
    GitHubModel
):
    """WebhookProjectsV2ItemReorderedPropChangesPropPreviousProjectsV2ItemNodeId"""

    from_: Missing[Union[str, None]] = Field(default=UNSET, alias="from")
    to: Missing[Union[str, None]] = Field(default=UNSET)


model_rebuild(WebhookProjectsV2ItemReordered)
model_rebuild(WebhookProjectsV2ItemReorderedPropChanges)
model_rebuild(WebhookProjectsV2ItemReorderedPropChangesPropPreviousProjectsV2ItemNodeId)

__all__ = (
    "WebhookProjectsV2ItemReordered",
    "WebhookProjectsV2ItemReorderedPropChanges",
    "WebhookProjectsV2ItemReorderedPropChangesPropPreviousProjectsV2ItemNodeId",
)
