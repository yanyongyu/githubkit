"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from typing_extensions import TypeAlias

from ..models import WebhookPing

Event: TypeAlias = WebhookPing

PingEvent: TypeAlias = Event

action_types = WebhookPing

ping_action_types = action_types

__all__ = ("Event", "PingEvent", "action_types", "ping_action_types")
