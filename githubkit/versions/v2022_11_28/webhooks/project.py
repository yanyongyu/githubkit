"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from typing import Dict, Type, Union
from typing_extensions import Annotated, TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import (
    WebhookProjectClosed,
    WebhookProjectEdited,
    WebhookProjectCreated,
    WebhookProjectDeleted,
    WebhookProjectReopened,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookProjectClosed,
        WebhookProjectCreated,
        WebhookProjectDeleted,
        WebhookProjectEdited,
        WebhookProjectReopened,
    ],
    Field(discriminator="action"),
]

ProjectEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "closed": WebhookProjectClosed,
    "created": WebhookProjectCreated,
    "deleted": WebhookProjectDeleted,
    "edited": WebhookProjectEdited,
    "reopened": WebhookProjectReopened,
}

project_action_types = action_types

__all__ = ("Event", "ProjectEvent", "action_types", "project_action_types")
