"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0002 import SimpleUser
from .group_0420 import ProjectsV2Item
from .group_0385 import SimpleInstallation
from .group_0386 import OrganizationSimpleWebhooks


class WebhookProjectsV2ItemEdited(GitHubModel):
    """Projects v2 Item Edited Event"""

    action: Literal["edited"] = Field()
    changes: Missing[
        Union[
            WebhookProjectsV2ItemEditedPropChangesOneof0,
            WebhookProjectsV2ItemEditedPropChangesOneof1,
        ]
    ] = Field(
        default=UNSET,
        description="The changes made to the item may involve modifications in the item's fields and draft issue body.\nIt includes altered values for text, number, date, single select, and iteration fields, along with the GraphQL node ID of the changed field.",
    )
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


class WebhookProjectsV2ItemEditedPropChangesOneof0(GitHubModel):
    """WebhookProjectsV2ItemEditedPropChangesOneof0"""

    field_value: WebhookProjectsV2ItemEditedPropChangesOneof0PropFieldValue = Field()


class WebhookProjectsV2ItemEditedPropChangesOneof0PropFieldValue(GitHubModel):
    """WebhookProjectsV2ItemEditedPropChangesOneof0PropFieldValue"""

    field_node_id: Missing[str] = Field(default=UNSET)
    field_type: Missing[str] = Field(default=UNSET)
    field_name: Missing[str] = Field(default=UNSET)
    project_number: Missing[int] = Field(default=UNSET)
    from_: Missing[
        Union[str, int, ProjectsV2SingleSelectOption, ProjectsV2IterationSetting, None]
    ] = Field(default=UNSET, alias="from")
    to: Missing[
        Union[str, int, ProjectsV2SingleSelectOption, ProjectsV2IterationSetting, None]
    ] = Field(default=UNSET)


class ProjectsV2SingleSelectOption(GitHubModel):
    """Projects v2 Single Select Option

    An option for a single select field
    """

    id: str = Field()
    name: str = Field()
    color: Missing[Union[str, None]] = Field(default=UNSET)
    description: Missing[Union[str, None]] = Field(default=UNSET)


class ProjectsV2IterationSetting(GitHubModel):
    """Projects v2 Iteration Setting

    An iteration setting for an iteration field
    """

    id: str = Field()
    title: str = Field()
    duration: Missing[Union[float, None]] = Field(default=UNSET)
    start_date: Missing[Union[str, None]] = Field(default=UNSET)


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
model_rebuild(ProjectsV2SingleSelectOption)
model_rebuild(ProjectsV2IterationSetting)
model_rebuild(WebhookProjectsV2ItemEditedPropChangesOneof1)
model_rebuild(WebhookProjectsV2ItemEditedPropChangesOneof1PropBody)

__all__ = (
    "WebhookProjectsV2ItemEdited",
    "WebhookProjectsV2ItemEditedPropChangesOneof0",
    "WebhookProjectsV2ItemEditedPropChangesOneof0PropFieldValue",
    "ProjectsV2SingleSelectOption",
    "ProjectsV2IterationSetting",
    "WebhookProjectsV2ItemEditedPropChangesOneof1",
    "WebhookProjectsV2ItemEditedPropChangesOneof1PropBody",
)
