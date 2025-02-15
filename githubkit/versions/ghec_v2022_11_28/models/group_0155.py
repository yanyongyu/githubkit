"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class MarketplaceListingPlan(GitHubModel):
    """Marketplace Listing Plan

    Marketplace Listing Plan
    """

    url: str = Field()
    accounts_url: str = Field()
    id: int = Field()
    number: int = Field()
    name: str = Field()
    description: str = Field()
    monthly_price_in_cents: int = Field()
    yearly_price_in_cents: int = Field()
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"] = Field()
    has_free_trial: bool = Field()
    unit_name: Union[str, None] = Field()
    state: str = Field()
    bullets: list[str] = Field()


model_rebuild(MarketplaceListingPlan)

__all__ = ("MarketplaceListingPlan",)
