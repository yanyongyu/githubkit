"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import Annotated, Union
from typing_extensions import TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import WebhookRegistryPackagePublished, WebhookRegistryPackageUpdated

Event: TypeAlias = Annotated[
    Union[
        WebhookRegistryPackagePublished,
        WebhookRegistryPackageUpdated,
    ],
    Field(discriminator="action"),
]

RegistryPackageEvent: TypeAlias = Event

action_types: dict[str, type[GitHubModel]] = {
    "published": WebhookRegistryPackagePublished,
    "updated": WebhookRegistryPackageUpdated,
}

registry_package_action_types = action_types

__all__ = (
    "Event",
    "RegistryPackageEvent",
    "action_types",
    "registry_package_action_types",
)
