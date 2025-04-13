"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0418 import EnterpriseWebhooksType
from .group_0419 import SimpleInstallationType
from .group_0420 import OrganizationSimpleWebhooksType


class WebhookCustomPropertyDeletedType(TypedDict):
    """custom property deleted event"""

    action: Literal["deleted"]
    definition: WebhookCustomPropertyDeletedPropDefinitionType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    sender: NotRequired[SimpleUserType]


class WebhookCustomPropertyDeletedPropDefinitionType(TypedDict):
    """WebhookCustomPropertyDeletedPropDefinition"""

    property_name: str


__all__ = (
    "WebhookCustomPropertyDeletedPropDefinitionType",
    "WebhookCustomPropertyDeletedType",
)
