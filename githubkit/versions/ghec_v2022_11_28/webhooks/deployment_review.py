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
    WebhookDeploymentReviewApproved,
    WebhookDeploymentReviewRejected,
    WebhookDeploymentReviewRequested,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookDeploymentReviewApproved,
        WebhookDeploymentReviewRejected,
        WebhookDeploymentReviewRequested,
    ],
    Field(discriminator="action"),
]

DeploymentReviewEvent: TypeAlias = Event

action_types: dict[str, type[GitHubModel]] = {
    "approved": WebhookDeploymentReviewApproved,
    "rejected": WebhookDeploymentReviewRejected,
    "requested": WebhookDeploymentReviewRequested,
}

deployment_review_action_types = action_types

__all__ = (
    "DeploymentReviewEvent",
    "Event",
    "action_types",
    "deployment_review_action_types",
)
