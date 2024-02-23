"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0PropAccount(
    GitHubModel
):
    """WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0Pro
    pAccount
    """

    id: int = Field()
    login: str = Field()
    node_id: str = Field()
    organization_billing_email: Union[str, None] = Field()
    type: str = Field()


class WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0PropPlan(
    GitHubModel
):
    """WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0Pro
    pPlan
    """

    bullets: List[str] = Field()
    description: str = Field()
    has_free_trial: bool = Field()
    id: int = Field()
    monthly_price_in_cents: int = Field()
    name: str = Field()
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"] = Field()
    unit_name: Union[str, None] = Field()
    yearly_price_in_cents: int = Field()


model_rebuild(
    WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0PropAccount
)
model_rebuild(
    WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0PropPlan
)

__all__ = (
    "WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0PropAccount",
    "WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0PropPlan",
)
