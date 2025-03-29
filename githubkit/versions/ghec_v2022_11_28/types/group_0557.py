"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0213 import CustomPropertyValueType
from .group_0471 import EnterpriseWebhooksType
from .group_0472 import SimpleInstallationType
from .group_0473 import OrganizationSimpleWebhooksType
from .group_0474 import RepositoryWebhooksType


class WebhookCustomPropertyValuesUpdatedType(TypedDict):
    """Custom property values updated event"""

    action: Literal["updated"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    repository: RepositoryWebhooksType
    organization: OrganizationSimpleWebhooksType
    sender: NotRequired[SimpleUserType]
    new_property_values: list[CustomPropertyValueType]
    old_property_values: list[CustomPropertyValueType]


__all__ = ("WebhookCustomPropertyValuesUpdatedType",)
