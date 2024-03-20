"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing_extensions import TypeAlias

from ..models import WebhookSecretScanningAlertLocationCreated

Event: TypeAlias = WebhookSecretScanningAlertLocationCreated

SecretScanningAlertLocationEvent: TypeAlias = Event

action_types = WebhookSecretScanningAlertLocationCreated

secret_scanning_alert_location_action_types = action_types

__all__ = (
    "Event",
    "SecretScanningAlertLocationEvent",
    "action_types",
    "secret_scanning_alert_location_action_types",
)
