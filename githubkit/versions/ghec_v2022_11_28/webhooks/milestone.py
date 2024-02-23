"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import Dict, Type, Union
from typing_extensions import Annotated, TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import (
    WebhookMilestoneClosed,
    WebhookMilestoneEdited,
    WebhookMilestoneOpened,
    WebhookMilestoneCreated,
    WebhookMilestoneDeleted,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookMilestoneClosed,
        WebhookMilestoneCreated,
        WebhookMilestoneDeleted,
        WebhookMilestoneEdited,
        WebhookMilestoneOpened,
    ],
    Field(discriminator="action"),
]

MilestoneEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "closed": WebhookMilestoneClosed,
    "created": WebhookMilestoneCreated,
    "deleted": WebhookMilestoneDeleted,
    "edited": WebhookMilestoneEdited,
    "opened": WebhookMilestoneOpened,
}

milestone_action_types = action_types

__all__ = ("Event", "MilestoneEvent", "action_types", "milestone_action_types")
