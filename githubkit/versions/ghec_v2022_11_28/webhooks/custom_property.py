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
    WebhookCustomPropertyCreated,
    WebhookCustomPropertyDeleted,
    WebhookCustomPropertyPromotedToEnterprise,
    WebhookCustomPropertyUpdated,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookCustomPropertyCreated,
        WebhookCustomPropertyDeleted,
        WebhookCustomPropertyPromotedToEnterprise,
        WebhookCustomPropertyUpdated,
    ],
    Field(discriminator="action"),
]

CustomPropertyEvent: TypeAlias = Event

action_types: dict[str, type[GitHubModel]] = {
    "created": WebhookCustomPropertyCreated,
    "deleted": WebhookCustomPropertyDeleted,
    "promote_to_enterprise": WebhookCustomPropertyPromotedToEnterprise,
    "updated": WebhookCustomPropertyUpdated,
}

custom_property_action_types = action_types

__all__ = (
    "CustomPropertyEvent",
    "Event",
    "action_types",
    "custom_property_action_types",
)
