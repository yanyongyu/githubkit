"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0053 import MarketplaceListingPlan


class UserMarketplacePurchase(GitHubModel):
    """User Marketplace Purchase

    User Marketplace Purchase
    """

    billing_cycle: str = Field()
    next_billing_date: Union[datetime, None] = Field()
    unit_count: Union[int, None] = Field()
    on_free_trial: bool = Field()
    free_trial_ends_on: Union[datetime, None] = Field()
    updated_at: Union[datetime, None] = Field()
    account: MarketplaceAccount = Field(title="Marketplace Account")
    plan: MarketplaceListingPlan = Field(
        title="Marketplace Listing Plan", description="Marketplace Listing Plan"
    )


class MarketplaceAccount(GitHubModel):
    """Marketplace Account"""

    url: str = Field()
    id: int = Field()
    type: str = Field()
    node_id: Missing[str] = Field(default=UNSET)
    login: str = Field()
    email: Missing[Union[str, None]] = Field(default=UNSET)
    organization_billing_email: Missing[Union[str, None]] = Field(default=UNSET)


model_rebuild(UserMarketplacePurchase)
model_rebuild(MarketplaceAccount)

__all__ = (
    "MarketplaceAccount",
    "UserMarketplacePurchase",
)
