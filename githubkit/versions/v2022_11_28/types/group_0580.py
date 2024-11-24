"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0384 import EnterpriseWebhooksType
from .group_0385 import SimpleInstallationType
from .group_0386 import OrganizationSimpleWebhooksType
from .group_0387 import RepositoryWebhooksType
from .group_0408 import WebhooksMarketplacePurchaseType
from .group_0409 import WebhooksPreviousMarketplacePurchaseType


class WebhookMarketplacePurchasePurchasedType(TypedDict):
    """marketplace_purchase purchased event"""

    action: Literal["purchased"]
    effective_date: str
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    marketplace_purchase: WebhooksMarketplacePurchaseType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    previous_marketplace_purchase: NotRequired[WebhooksPreviousMarketplacePurchaseType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserType


__all__ = ("WebhookMarketplacePurchasePurchasedType",)
