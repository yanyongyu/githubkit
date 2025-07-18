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


class EnterprisesEnterpriseSettingsBillingCostCentersPostResponse200(GitHubModel):
    """EnterprisesEnterpriseSettingsBillingCostCentersPostResponse200"""

    id: Missing[str] = Field(
        default=UNSET, description="Unique identifier for the cost center"
    )
    name: Missing[str] = Field(default=UNSET, description="Name of the cost center")
    resources: Missing[
        list[
            EnterprisesEnterpriseSettingsBillingCostCentersPostResponse200PropResourcesItems
        ]
    ] = Field(
        default=UNSET, description="List of resources assigned to this cost center"
    )


class EnterprisesEnterpriseSettingsBillingCostCentersPostResponse200PropResourcesItems(
    GitHubModel
):
    """EnterprisesEnterpriseSettingsBillingCostCentersPostResponse200PropResourcesItems"""

    type: Missing[str] = Field(
        default=UNSET, description="Type of resource (User, Org, or Repo)"
    )
    name: Missing[str] = Field(default=UNSET, description="Name/login of the resource")


model_rebuild(EnterprisesEnterpriseSettingsBillingCostCentersPostResponse200)
model_rebuild(
    EnterprisesEnterpriseSettingsBillingCostCentersPostResponse200PropResourcesItems
)

__all__ = (
    "EnterprisesEnterpriseSettingsBillingCostCentersPostResponse200",
    "EnterprisesEnterpriseSettingsBillingCostCentersPostResponse200PropResourcesItems",
)
