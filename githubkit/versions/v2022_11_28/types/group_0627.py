"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0418 import EnterpriseWebhooksType
from .group_0419 import SimpleInstallationType
from .group_0420 import OrganizationSimpleWebhooksType
from .group_0421 import RepositoryWebhooksType
from .group_0443 import WebhooksPreviousMarketplacePurchaseType


class WebhookMarketplacePurchasePendingChangeCancelledType(TypedDict):
    """marketplace_purchase pending_change_cancelled event"""

    action: Literal["pending_change_cancelled"]
    effective_date: str
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    marketplace_purchase: (
        WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseType
    )
    organization: NotRequired[OrganizationSimpleWebhooksType]
    previous_marketplace_purchase: NotRequired[WebhooksPreviousMarketplacePurchaseType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserType


class WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseType(
    TypedDict
):
    """Marketplace Purchase"""

    account: WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchasePropAccountType
    billing_cycle: str
    free_trial_ends_on: None
    next_billing_date: Union[str, None]
    on_free_trial: bool
    plan: WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchasePropPlanType
    unit_count: int


class WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchasePropAccountType(
    TypedDict
):
    """WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchasePropAccou
    nt
    """

    id: int
    login: str
    node_id: str
    organization_billing_email: Union[str, None]
    type: str


class WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchasePropPlanType(
    TypedDict
):
    """WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchasePropPlan"""

    bullets: list[str]
    description: str
    has_free_trial: bool
    id: int
    monthly_price_in_cents: int
    name: str
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]
    unit_name: Union[str, None]
    yearly_price_in_cents: int


__all__ = (
    "WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchasePropAccountType",
    "WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchasePropPlanType",
    "WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseType",
    "WebhookMarketplacePurchasePendingChangeCancelledType",
)
