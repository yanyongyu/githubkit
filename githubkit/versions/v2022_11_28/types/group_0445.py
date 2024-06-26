"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0367 import EnterpriseWebhooksType
from .group_0368 import SimpleInstallationType
from .group_0370 import RepositoryWebhooksType
from .group_0371 import SimpleUserWebhooksType
from .group_0093 import CustomPropertyValueType
from .group_0369 import OrganizationSimpleWebhooksType


class WebhookCustomPropertyValuesUpdatedType(TypedDict):
    """Custom property values updated event"""

    action: Literal["updated"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    repository: RepositoryWebhooksType
    organization: OrganizationSimpleWebhooksType
    sender: NotRequired[SimpleUserWebhooksType]
    new_property_values: List[CustomPropertyValueType]
    old_property_values: List[CustomPropertyValueType]


__all__ = ("WebhookCustomPropertyValuesUpdatedType",)
