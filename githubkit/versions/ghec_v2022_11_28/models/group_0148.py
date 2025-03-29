"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class BillingUsageReport(GitHubModel):
    """BillingUsageReport"""

    usage_items: Missing[list[BillingUsageReportPropUsageItemsItems]] = Field(
        default=UNSET, alias="usageItems"
    )


class BillingUsageReportPropUsageItemsItems(GitHubModel):
    """BillingUsageReportPropUsageItemsItems"""

    date: str = Field(description="Date of the usage line item.")
    product: str = Field(description="Product name.")
    sku: str = Field(description="SKU name.")
    quantity: int = Field(description="Quantity of the usage line item.")
    unit_type: str = Field(
        alias="unitType", description="Unit type of the usage line item."
    )
    price_per_unit: float = Field(
        alias="pricePerUnit", description="Price per unit of the usage line item."
    )
    gross_amount: float = Field(
        alias="grossAmount", description="Gross amount of the usage line item."
    )
    discount_amount: float = Field(
        alias="discountAmount", description="Discount amount of the usage line item."
    )
    net_amount: float = Field(
        alias="netAmount", description="Net amount of the usage line item."
    )
    organization_name: str = Field(
        alias="organizationName", description="Name of the organization."
    )
    repository_name: Missing[str] = Field(
        default=UNSET, alias="repositoryName", description="Name of the repository."
    )


model_rebuild(BillingUsageReport)
model_rebuild(BillingUsageReportPropUsageItemsItems)

__all__ = (
    "BillingUsageReport",
    "BillingUsageReportPropUsageItemsItems",
)
