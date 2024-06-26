"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import Dict, Type, Union
from typing_extensions import Annotated, TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import (
    WebhookSecretScanningAlertCreated,
    WebhookSecretScanningAlertReopened,
    WebhookSecretScanningAlertResolved,
    WebhookSecretScanningAlertValidated,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookSecretScanningAlertCreated,
        WebhookSecretScanningAlertReopened,
        WebhookSecretScanningAlertResolved,
        WebhookSecretScanningAlertValidated,
    ],
    Field(discriminator="action"),
]

SecretScanningAlertEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "created": WebhookSecretScanningAlertCreated,
    "reopened": WebhookSecretScanningAlertReopened,
    "resolved": WebhookSecretScanningAlertResolved,
    "validated": WebhookSecretScanningAlertValidated,
}

secret_scanning_alert_action_types = action_types

__all__ = (
    "Event",
    "SecretScanningAlertEvent",
    "action_types",
    "secret_scanning_alert_action_types",
)
