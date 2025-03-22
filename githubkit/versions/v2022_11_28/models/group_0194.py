"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0193 import RateLimit
from .group_0195 import RateLimitOverviewPropResources


class RateLimitOverview(GitHubModel):
    """Rate Limit Overview

    Rate Limit Overview
    """

    resources: RateLimitOverviewPropResources = Field()
    rate: RateLimit = Field(title="Rate Limit")


model_rebuild(RateLimitOverview)

__all__ = ("RateLimitOverview",)
