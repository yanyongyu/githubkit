"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0078 import CustomPropertyType
from .group_0471 import EnterpriseWebhooksType
from .group_0472 import SimpleInstallationType
from .group_0473 import OrganizationSimpleWebhooksType


class WebhookCustomPropertyPromotedToEnterpriseType(TypedDict):
    """custom property promoted to business event"""

    action: Literal["promote_to_enterprise"]
    definition: CustomPropertyType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookCustomPropertyPromotedToEnterpriseType",)
