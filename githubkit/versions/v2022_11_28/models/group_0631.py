"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0366 import ProjectsV2Item
from .group_0356 import SimpleInstallation
from .group_0359 import SimpleUserWebhooks
from .group_0357 import OrganizationSimpleWebhooks


class WebhookProjectsV2ItemEdited(GitHubModel):
    """Projects v2 Item Edited Event"""

    action: Literal["edited"] = Field()
    changes: Missing[
        Union[
            WebhookProjectsV2ItemEditedPropChangesOneof0,
            WebhookProjectsV2ItemEditedPropChangesOneof1,
        ]
    ] = Field(default=UNSET)
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
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookProjectsV2ItemEditedPropChangesOneof0(GitHubModel):
    """WebhookProjectsV2ItemEditedPropChangesOneof0"""

    field_value: WebhookProjectsV2ItemEditedPropChangesOneof0PropFieldValue = Field()


class WebhookProjectsV2ItemEditedPropChangesOneof0PropFieldValue(GitHubModel):
    """WebhookProjectsV2ItemEditedPropChangesOneof0PropFieldValue"""

    field_node_id: Missing[str] = Field(default=UNSET)
    field_type: Missing[str] = Field(default=UNSET)


class WebhookProjectsV2ItemEditedPropChangesOneof1(GitHubModel):
    """WebhookProjectsV2ItemEditedPropChangesOneof1"""

    body: WebhookProjectsV2ItemEditedPropChangesOneof1PropBody = Field()


class WebhookProjectsV2ItemEditedPropChangesOneof1PropBody(GitHubModel):
    """WebhookProjectsV2ItemEditedPropChangesOneof1PropBody"""

    from_: Missing[Union[str, None]] = Field(default=UNSET, alias="from")
    to: Missing[Union[str, None]] = Field(default=UNSET)


model_rebuild(WebhookProjectsV2ItemEdited)
model_rebuild(WebhookProjectsV2ItemEditedPropChangesOneof0)
model_rebuild(WebhookProjectsV2ItemEditedPropChangesOneof0PropFieldValue)
model_rebuild(WebhookProjectsV2ItemEditedPropChangesOneof1)
model_rebuild(WebhookProjectsV2ItemEditedPropChangesOneof1PropBody)

__all__ = (
    "WebhookProjectsV2ItemEdited",
    "WebhookProjectsV2ItemEditedPropChangesOneof0",
    "WebhookProjectsV2ItemEditedPropChangesOneof0PropFieldValue",
    "WebhookProjectsV2ItemEditedPropChangesOneof1",
    "WebhookProjectsV2ItemEditedPropChangesOneof1PropBody",
)
