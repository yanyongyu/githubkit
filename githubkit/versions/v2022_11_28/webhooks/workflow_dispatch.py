"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from typing_extensions import TypeAlias

from ..models import WebhookWorkflowDispatch

Event: TypeAlias = WebhookWorkflowDispatch

WorkflowDispatchEvent: TypeAlias = Event

action_types = WebhookWorkflowDispatch

workflow_dispatch_action_types = action_types

__all__ = (
    "Event",
    "WorkflowDispatchEvent",
    "action_types",
    "workflow_dispatch_action_types",
)
