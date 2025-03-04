"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import Annotated, Union
from typing_extensions import TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import WebhookMemberAdded, WebhookMemberEdited, WebhookMemberRemoved

Event: TypeAlias = Annotated[
    Union[
        WebhookMemberAdded,
        WebhookMemberEdited,
        WebhookMemberRemoved,
    ],
    Field(discriminator="action"),
]

MemberEvent: TypeAlias = Event

action_types: dict[str, type[GitHubModel]] = {
    "added": WebhookMemberAdded,
    "edited": WebhookMemberEdited,
    "removed": WebhookMemberRemoved,
}

member_action_types = action_types

__all__ = ("Event", "MemberEvent", "action_types", "member_action_types")
