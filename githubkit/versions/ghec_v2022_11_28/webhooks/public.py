"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing_extensions import TypeAlias

from ..models import WebhookPublic

Event: TypeAlias = WebhookPublic

PublicEvent: TypeAlias = Event

action_types = WebhookPublic

public_action_types = action_types

__all__ = ("Event", "PublicEvent", "action_types", "public_action_types")
