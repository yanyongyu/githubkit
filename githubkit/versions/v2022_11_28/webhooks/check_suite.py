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
    WebhookCheckSuiteCompleted,
    WebhookCheckSuiteRequested,
    WebhookCheckSuiteRerequested,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookCheckSuiteCompleted,
        WebhookCheckSuiteRequested,
        WebhookCheckSuiteRerequested,
    ],
    Field(discriminator="action"),
]

CheckSuiteEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "completed": WebhookCheckSuiteCompleted,
    "requested": WebhookCheckSuiteRequested,
    "rerequested": WebhookCheckSuiteRerequested,
}

check_suite_action_types = action_types

__all__ = ("Event", "CheckSuiteEvent", "action_types", "check_suite_action_types")
