"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing_extensions import TypeAlias

from ..models import WebhookMetaDeleted

Event: TypeAlias = WebhookMetaDeleted

MetaEvent: TypeAlias = Event

action_types = WebhookMetaDeleted

meta_action_types = action_types

__all__ = ("Event", "MetaEvent", "action_types", "meta_action_types")
