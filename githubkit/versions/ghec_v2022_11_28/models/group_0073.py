"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0071 import MarketplaceListingPlan


class MarketplacePurchasePropMarketplacePendingChange(GitHubModel):
    """MarketplacePurchasePropMarketplacePendingChange"""

    is_installed: Missing[bool] = Field(default=UNSET)
    effective_date: Missing[str] = Field(default=UNSET)
    unit_count: Missing[Union[int, None]] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    plan: Missing[MarketplaceListingPlan] = Field(
        default=UNSET,
        title="Marketplace Listing Plan",
        description="Marketplace Listing Plan",
    )


class MarketplacePurchasePropMarketplacePurchase(GitHubModel):
    """MarketplacePurchasePropMarketplacePurchase"""

    billing_cycle: Missing[str] = Field(default=UNSET)
    next_billing_date: Missing[Union[str, None]] = Field(default=UNSET)
    is_installed: Missing[bool] = Field(default=UNSET)
    unit_count: Missing[Union[int, None]] = Field(default=UNSET)
    on_free_trial: Missing[bool] = Field(default=UNSET)
    free_trial_ends_on: Missing[Union[str, None]] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)
    plan: Missing[MarketplaceListingPlan] = Field(
        default=UNSET,
        title="Marketplace Listing Plan",
        description="Marketplace Listing Plan",
    )


model_rebuild(MarketplacePurchasePropMarketplacePendingChange)
model_rebuild(MarketplacePurchasePropMarketplacePurchase)

__all__ = (
    "MarketplacePurchasePropMarketplacePendingChange",
    "MarketplacePurchasePropMarketplacePurchase",
)
