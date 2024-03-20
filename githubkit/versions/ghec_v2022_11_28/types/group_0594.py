"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired


class WebhookMarketplacePurchaseChangedPropMarketplacePurchaseAllof0Type(TypedDict):
    """Marketplace Purchase"""

    account: WebhookMarketplacePurchaseChangedPropMarketplacePurchaseAllof0PropAccountType
    billing_cycle: str
    free_trial_ends_on: Union[str, None]
    next_billing_date: NotRequired[Union[str, None]]
    on_free_trial: bool
    plan: WebhookMarketplacePurchaseChangedPropMarketplacePurchaseAllof0PropPlanType
    unit_count: int


class WebhookMarketplacePurchaseChangedPropMarketplacePurchaseAllof0PropAccountType(
    TypedDict
):
    """WebhookMarketplacePurchaseChangedPropMarketplacePurchaseAllof0PropAccount"""

    id: int
    login: str
    node_id: str
    organization_billing_email: Union[str, None]
    type: str


class WebhookMarketplacePurchaseChangedPropMarketplacePurchaseAllof0PropPlanType(
    TypedDict
):
    """WebhookMarketplacePurchaseChangedPropMarketplacePurchaseAllof0PropPlan"""

    bullets: List[str]
    description: str
    has_free_trial: bool
    id: int
    monthly_price_in_cents: int
    name: str
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]
    unit_name: Union[str, None]
    yearly_price_in_cents: int


__all__ = (
    "WebhookMarketplacePurchaseChangedPropMarketplacePurchaseAllof0Type",
    "WebhookMarketplacePurchaseChangedPropMarketplacePurchaseAllof0PropAccountType",
    "WebhookMarketplacePurchaseChangedPropMarketplacePurchaseAllof0PropPlanType",
)
