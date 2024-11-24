"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import date
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser
from .group_0428 import SimpleInstallation
from .group_0429 import OrganizationSimpleWebhooks
from .group_0466 import ProjectsV2StatusUpdate


class WebhookProjectsV2StatusUpdateEdited(GitHubModel):
    """Projects v2 Status Update Edited Event"""

    action: Literal["edited"] = Field()
    changes: Missing[WebhookProjectsV2StatusUpdateEditedPropChanges] = Field(
        default=UNSET
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: OrganizationSimpleWebhooks = Field(
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    projects_v2_status_update: ProjectsV2StatusUpdate = Field(
        title="Projects v2 Status Update",
        description="An status update belonging to a project",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class WebhookProjectsV2StatusUpdateEditedPropChanges(GitHubModel):
    """WebhookProjectsV2StatusUpdateEditedPropChanges"""

    body: Missing[WebhookProjectsV2StatusUpdateEditedPropChangesPropBody] = Field(
        default=UNSET
    )
    status: Missing[WebhookProjectsV2StatusUpdateEditedPropChangesPropStatus] = Field(
        default=UNSET
    )
    start_date: Missing[WebhookProjectsV2StatusUpdateEditedPropChangesPropStartDate] = (
        Field(default=UNSET)
    )
    target_date: Missing[
        WebhookProjectsV2StatusUpdateEditedPropChangesPropTargetDate
    ] = Field(default=UNSET)


class WebhookProjectsV2StatusUpdateEditedPropChangesPropBody(GitHubModel):
    """WebhookProjectsV2StatusUpdateEditedPropChangesPropBody"""

    from_: Missing[Union[str, None]] = Field(default=UNSET, alias="from")
    to: Missing[Union[str, None]] = Field(default=UNSET)


class WebhookProjectsV2StatusUpdateEditedPropChangesPropStatus(GitHubModel):
    """WebhookProjectsV2StatusUpdateEditedPropChangesPropStatus"""

    from_: Missing[
        Union[None, Literal["INACTIVE", "ON_TRACK", "AT_RISK", "OFF_TRACK", "COMPLETE"]]
    ] = Field(default=UNSET, alias="from")
    to: Missing[
        Union[None, Literal["INACTIVE", "ON_TRACK", "AT_RISK", "OFF_TRACK", "COMPLETE"]]
    ] = Field(default=UNSET)


class WebhookProjectsV2StatusUpdateEditedPropChangesPropStartDate(GitHubModel):
    """WebhookProjectsV2StatusUpdateEditedPropChangesPropStartDate"""

    from_: Missing[Union[date, None]] = Field(default=UNSET, alias="from")
    to: Missing[Union[date, None]] = Field(default=UNSET)


class WebhookProjectsV2StatusUpdateEditedPropChangesPropTargetDate(GitHubModel):
    """WebhookProjectsV2StatusUpdateEditedPropChangesPropTargetDate"""

    from_: Missing[Union[date, None]] = Field(default=UNSET, alias="from")
    to: Missing[Union[date, None]] = Field(default=UNSET)


model_rebuild(WebhookProjectsV2StatusUpdateEdited)
model_rebuild(WebhookProjectsV2StatusUpdateEditedPropChanges)
model_rebuild(WebhookProjectsV2StatusUpdateEditedPropChangesPropBody)
model_rebuild(WebhookProjectsV2StatusUpdateEditedPropChangesPropStatus)
model_rebuild(WebhookProjectsV2StatusUpdateEditedPropChangesPropStartDate)
model_rebuild(WebhookProjectsV2StatusUpdateEditedPropChangesPropTargetDate)

__all__ = (
    "WebhookProjectsV2StatusUpdateEdited",
    "WebhookProjectsV2StatusUpdateEditedPropChanges",
    "WebhookProjectsV2StatusUpdateEditedPropChangesPropBody",
    "WebhookProjectsV2StatusUpdateEditedPropChangesPropStartDate",
    "WebhookProjectsV2StatusUpdateEditedPropChangesPropStatus",
    "WebhookProjectsV2StatusUpdateEditedPropChangesPropTargetDate",
)
