"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import Annotated, Union
from typing_extensions import TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import (
    WebhookOrganizationDeleted,
    WebhookOrganizationMemberAdded,
    WebhookOrganizationMemberInvited,
    WebhookOrganizationMemberRemoved,
    WebhookOrganizationRenamed,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookOrganizationDeleted,
        WebhookOrganizationMemberAdded,
        WebhookOrganizationMemberInvited,
        WebhookOrganizationMemberRemoved,
        WebhookOrganizationRenamed,
    ],
    Field(discriminator="action"),
]

OrganizationEvent: TypeAlias = Event

action_types: dict[str, type[GitHubModel]] = {
    "deleted": WebhookOrganizationDeleted,
    "member_added": WebhookOrganizationMemberAdded,
    "member_invited": WebhookOrganizationMemberInvited,
    "member_removed": WebhookOrganizationMemberRemoved,
    "renamed": WebhookOrganizationRenamed,
}

organization_action_types = action_types

__all__ = ("Event", "OrganizationEvent", "action_types", "organization_action_types")
