"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import Annotated, Union
from typing_extensions import TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import (
    WebhookExemptionRequestCancelled,
    WebhookExemptionRequestCompleted,
    WebhookExemptionRequestCreated,
    WebhookExemptionRequestResponseDismissed,
    WebhookExemptionRequestResponseSubmitted,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookExemptionRequestCancelled,
        WebhookExemptionRequestCompleted,
        WebhookExemptionRequestCreated,
        WebhookExemptionRequestResponseDismissed,
        WebhookExemptionRequestResponseSubmitted,
    ],
    Field(discriminator="action"),
]

DismissalRequestSecretScanningEvent: TypeAlias = Event

action_types: dict[str, type[GitHubModel]] = {
    "cancelled": WebhookExemptionRequestCancelled,
    "completed": WebhookExemptionRequestCompleted,
    "created": WebhookExemptionRequestCreated,
    "response_dismissed": WebhookExemptionRequestResponseDismissed,
    "response_submitted": WebhookExemptionRequestResponseSubmitted,
}

dismissal_request_secret_scanning_action_types = action_types

__all__ = (
    "DismissalRequestSecretScanningEvent",
    "Event",
    "action_types",
    "dismissal_request_secret_scanning_action_types",
)
