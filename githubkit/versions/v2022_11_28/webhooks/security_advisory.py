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
    WebhookSecurityAdvisoryUpdated,
    WebhookSecurityAdvisoryPublished,
    WebhookSecurityAdvisoryWithdrawn,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookSecurityAdvisoryPublished,
        WebhookSecurityAdvisoryUpdated,
        WebhookSecurityAdvisoryWithdrawn,
    ],
    Field(discriminator="action"),
]

SecurityAdvisoryEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "published": WebhookSecurityAdvisoryPublished,
    "updated": WebhookSecurityAdvisoryUpdated,
    "withdrawn": WebhookSecurityAdvisoryWithdrawn,
}

security_advisory_action_types = action_types

__all__ = (
    "Event",
    "SecurityAdvisoryEvent",
    "action_types",
    "security_advisory_action_types",
)
