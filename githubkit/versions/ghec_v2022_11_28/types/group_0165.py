"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0166 import (
    MarketplacePurchasePropMarketplacePendingChangeType,
    MarketplacePurchasePropMarketplacePurchaseType,
)


class MarketplacePurchaseType(TypedDict):
    """Marketplace Purchase

    Marketplace Purchase
    """

    url: str
    type: str
    id: int
    login: str
    organization_billing_email: NotRequired[str]
    email: NotRequired[Union[str, None]]
    marketplace_pending_change: NotRequired[
        Union[MarketplacePurchasePropMarketplacePendingChangeType, None]
    ]
    marketplace_purchase: MarketplacePurchasePropMarketplacePurchaseType


__all__ = ("MarketplacePurchaseType",)
