"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import Union, Annotated
from typing_extensions import TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import (
    WebhookInstallationCreated,
    WebhookInstallationDeleted,
    WebhookInstallationSuspend,
    WebhookInstallationUnsuspend,
    WebhookInstallationNewPermissionsAccepted,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookInstallationCreated,
        WebhookInstallationDeleted,
        WebhookInstallationNewPermissionsAccepted,
        WebhookInstallationSuspend,
        WebhookInstallationUnsuspend,
    ],
    Field(discriminator="action"),
]

InstallationEvent: TypeAlias = Event

action_types: dict[str, type[GitHubModel]] = {
    "created": WebhookInstallationCreated,
    "deleted": WebhookInstallationDeleted,
    "new_permissions_accepted": WebhookInstallationNewPermissionsAccepted,
    "suspend": WebhookInstallationSuspend,
    "unsuspend": WebhookInstallationUnsuspend,
}

installation_action_types = action_types

__all__ = ("Event", "InstallationEvent", "action_types", "installation_action_types")
