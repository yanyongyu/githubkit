"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0351 import EnterpriseWebhooksType
from .group_0352 import SimpleInstallationType
from .group_0354 import RepositoryWebhooksType
from .group_0355 import SimpleUserWebhooksType
from .group_0092 import CustomPropertyValueType
from .group_0353 import OrganizationSimpleWebhooksType


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