"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0451 import EnterpriseWebhooksType
from .group_0452 import SimpleInstallationType
from .group_0453 import OrganizationSimpleWebhooksType
from .group_0454 import RepositoryWebhooksType
from .group_0477 import WebhooksMarketplacePurchaseType
from .group_0478 import WebhooksPreviousMarketplacePurchaseType


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
