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
    WebhookTeamAddedToRepository,
    WebhookTeamCreated,
    WebhookTeamDeleted,
    WebhookTeamEdited,
    WebhookTeamRemovedFromRepository,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookTeamAddedToRepository,
        WebhookTeamCreated,
        WebhookTeamDeleted,
        WebhookTeamEdited,
        WebhookTeamRemovedFromRepository,
    ],
    Field(discriminator="action"),
]

TeamEvent: TypeAlias = Event

action_types: dict[str, type[GitHubModel]] = {
    "added_to_repository": WebhookTeamAddedToRepository,
    "created": WebhookTeamCreated,
    "deleted": WebhookTeamDeleted,
    "edited": WebhookTeamEdited,
    "removed_from_repository": WebhookTeamRemovedFromRepository,
}

team_action_types = action_types

__all__ = ("Event", "TeamEvent", "action_types", "team_action_types")
