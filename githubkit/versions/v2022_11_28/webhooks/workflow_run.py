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
    WebhookWorkflowRunCompleted,
    WebhookWorkflowRunRequested,
    WebhookWorkflowRunInProgress,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookWorkflowRunCompleted,
        WebhookWorkflowRunInProgress,
        WebhookWorkflowRunRequested,
    ],
    Field(discriminator="action"),
]

WorkflowRunEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "completed": WebhookWorkflowRunCompleted,
    "in_progress": WebhookWorkflowRunInProgress,
    "requested": WebhookWorkflowRunRequested,
}

workflow_run_action_types = action_types

__all__ = ("Event", "WorkflowRunEvent", "action_types", "workflow_run_action_types")
