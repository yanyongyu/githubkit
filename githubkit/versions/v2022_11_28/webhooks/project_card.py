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
    WebhookProjectCardConverted,
    WebhookProjectCardCreated,
    WebhookProjectCardDeleted,
    WebhookProjectCardEdited,
    WebhookProjectCardMoved,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookProjectCardConverted,
        WebhookProjectCardCreated,
        WebhookProjectCardDeleted,
        WebhookProjectCardEdited,
        WebhookProjectCardMoved,
    ],
    Field(discriminator="action"),
]

ProjectCardEvent: TypeAlias = Event

action_types: dict[str, type[GitHubModel]] = {
    "converted": WebhookProjectCardConverted,
    "created": WebhookProjectCardCreated,
    "deleted": WebhookProjectCardDeleted,
    "edited": WebhookProjectCardEdited,
    "moved": WebhookProjectCardMoved,
}

project_card_action_types = action_types

__all__ = ("Event", "ProjectCardEvent", "action_types", "project_card_action_types")
