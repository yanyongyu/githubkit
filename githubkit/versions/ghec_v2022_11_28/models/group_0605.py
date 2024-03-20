"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof0(GitHubModel):
    """Marketplace Purchase"""

    account: WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof0PropAccount = Field()
    billing_cycle: str = Field()
    free_trial_ends_on: Union[str, None] = Field()
    next_billing_date: Missing[Union[str, None]] = Field(default=UNSET)
    on_free_trial: bool = Field()
    plan: WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof0PropPlan = (
        Field()
    )
    unit_count: int = Field()


class WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof0PropAccount(
    GitHubModel
):
    """WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof0PropAccount"""

    id: int = Field()
    login: str = Field()
    node_id: str = Field()
    organization_billing_email: Union[str, None] = Field()
    type: str = Field()


class WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof0PropPlan(
    GitHubModel
):
    """WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof0PropPlan"""

    bullets: List[str] = Field()
    description: str = Field()
    has_free_trial: bool = Field()
    id: int = Field()
    monthly_price_in_cents: int = Field()
    name: str = Field()
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"] = Field()
    unit_name: Union[str, None] = Field()
    yearly_price_in_cents: int = Field()


model_rebuild(WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof0)
model_rebuild(
    WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof0PropAccount
)
model_rebuild(WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof0PropPlan)

__all__ = (
    "WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof0",
    "WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof0PropAccount",
    "WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof0PropPlan",
)
