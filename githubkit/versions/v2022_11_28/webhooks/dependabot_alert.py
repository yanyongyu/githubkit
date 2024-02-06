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
    WebhookDependabotAlertFixed,
    WebhookDependabotAlertCreated,
    WebhookDependabotAlertReopened,
    WebhookDependabotAlertDismissed,
    WebhookDependabotAlertAutoReopened,
    WebhookDependabotAlertReintroduced,
    WebhookDependabotAlertAutoDismissed,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookDependabotAlertAutoDismissed,
        WebhookDependabotAlertAutoReopened,
        WebhookDependabotAlertCreated,
        WebhookDependabotAlertDismissed,
        WebhookDependabotAlertFixed,
        WebhookDependabotAlertReintroduced,
        WebhookDependabotAlertReopened,
    ],
    Field(discriminator="action"),
]

DependabotAlertEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "auto_dismissed": WebhookDependabotAlertAutoDismissed,
    "auto_reopened": WebhookDependabotAlertAutoReopened,
    "created": WebhookDependabotAlertCreated,
    "dismissed": WebhookDependabotAlertDismissed,
    "fixed": WebhookDependabotAlertFixed,
    "reintroduced": WebhookDependabotAlertReintroduced,
    "reopened": WebhookDependabotAlertReopened,
}

dependabot_alert_action_types = action_types

__all__ = (
    "Event",
    "DependabotAlertEvent",
    "action_types",
    "dependabot_alert_action_types",
)
