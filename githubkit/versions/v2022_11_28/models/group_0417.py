"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class WebhooksMarketplacePurchase(GitHubModel):
    """Marketplace Purchase"""

    account: WebhooksMarketplacePurchasePropAccount = Field()
    billing_cycle: str = Field()
    free_trial_ends_on: Union[str, None] = Field()
    next_billing_date: Union[str, None] = Field()
    on_free_trial: bool = Field()
    plan: WebhooksMarketplacePurchasePropPlan = Field()
    unit_count: int = Field()


class WebhooksMarketplacePurchasePropAccount(GitHubModel):
    """WebhooksMarketplacePurchasePropAccount"""

    id: int = Field()
    login: str = Field()
    node_id: str = Field()
    organization_billing_email: Union[str, None] = Field()
    type: str = Field()


class WebhooksMarketplacePurchasePropPlan(GitHubModel):
    """WebhooksMarketplacePurchasePropPlan"""

    bullets: list[Union[str, None]] = Field()
    description: str = Field()
    has_free_trial: bool = Field()
    id: int = Field()
    monthly_price_in_cents: int = Field()
    name: str = Field()
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"] = Field()
    unit_name: Union[str, None] = Field()
    yearly_price_in_cents: int = Field()


model_rebuild(WebhooksMarketplacePurchase)
model_rebuild(WebhooksMarketplacePurchasePropAccount)
model_rebuild(WebhooksMarketplacePurchasePropPlan)

__all__ = (
    "WebhooksMarketplacePurchase",
    "WebhooksMarketplacePurchasePropAccount",
    "WebhooksMarketplacePurchasePropPlan",
)
