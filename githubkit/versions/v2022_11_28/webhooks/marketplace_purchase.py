"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import Dict, Type, Union
from typing_extensions import Annotated, TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import (
    WebhookMarketplacePurchaseChanged,
    WebhookMarketplacePurchaseCancelled,
    WebhookMarketplacePurchasePurchased,
    WebhookMarketplacePurchasePendingChange,
    WebhookMarketplacePurchasePendingChangeCancelled,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookMarketplacePurchaseCancelled,
        WebhookMarketplacePurchaseChanged,
        WebhookMarketplacePurchasePendingChange,
        WebhookMarketplacePurchasePendingChangeCancelled,
        WebhookMarketplacePurchasePurchased,
    ],
    Field(discriminator="action"),
]

MarketplacePurchaseEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "cancelled": WebhookMarketplacePurchaseCancelled,
    "changed": WebhookMarketplacePurchaseChanged,
    "pending_change": WebhookMarketplacePurchasePendingChange,
    "pending_change_cancelled": WebhookMarketplacePurchasePendingChangeCancelled,
    "purchased": WebhookMarketplacePurchasePurchased,
}

marketplace_purchase_action_types = action_types

__all__ = (
    "Event",
    "MarketplacePurchaseEvent",
    "action_types",
    "marketplace_purchase_action_types",
)
