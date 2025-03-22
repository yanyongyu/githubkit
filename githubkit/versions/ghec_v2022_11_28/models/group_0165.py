"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0166 import (
    MarketplacePurchasePropMarketplacePendingChange,
    MarketplacePurchasePropMarketplacePurchase,
)


class MarketplacePurchase(GitHubModel):
    """Marketplace Purchase

    Marketplace Purchase
    """

    url: str = Field()
    type: str = Field()
    id: int = Field()
    login: str = Field()
    organization_billing_email: Missing[str] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    marketplace_pending_change: Missing[
        Union[MarketplacePurchasePropMarketplacePendingChange, None]
    ] = Field(default=UNSET)
    marketplace_purchase: MarketplacePurchasePropMarketplacePurchase = Field()


model_rebuild(MarketplacePurchase)

__all__ = ("MarketplacePurchase",)
