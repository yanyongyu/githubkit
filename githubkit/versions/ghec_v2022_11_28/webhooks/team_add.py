"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing_extensions import TypeAlias

from ..models import WebhookTeamAdd

Event: TypeAlias = WebhookTeamAdd

TeamAddEvent: TypeAlias = Event

action_types = WebhookTeamAdd

team_add_action_types = action_types

__all__ = ("Event", "TeamAddEvent", "action_types", "team_add_action_types")
