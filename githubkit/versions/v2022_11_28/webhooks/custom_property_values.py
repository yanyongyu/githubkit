"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from typing_extensions import TypeAlias

from ..models import WebhookCustomPropertyValuesUpdated

Event: TypeAlias = WebhookCustomPropertyValuesUpdated

CustomPropertyValuesEvent: TypeAlias = Event

action_types = WebhookCustomPropertyValuesUpdated

custom_property_values_action_types = action_types

__all__ = (
    "Event",
    "CustomPropertyValuesEvent",
    "action_types",
    "custom_property_values_action_types",
)
