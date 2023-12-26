"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from typing import Dict, Type, Union
from typing_extensions import Annotated, TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import WebhookLabelEdited, WebhookLabelCreated, WebhookLabelDeleted

Event: TypeAlias = Annotated[
    Union[
        WebhookLabelCreated,
        WebhookLabelDeleted,
        WebhookLabelEdited,
    ],
    Field(discriminator="action"),
]

LabelEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "created": WebhookLabelCreated,
    "deleted": WebhookLabelDeleted,
    "edited": WebhookLabelEdited,
}

label_action_types = action_types

__all__ = ("Event", "LabelEvent", "action_types", "label_action_types")
