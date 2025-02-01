"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0081 import (
    EnterpriseRulesetConditionsOrganizationNameTargetPropOrganizationName,
)


class EnterpriseRulesetConditionsOrganizationNameTarget(GitHubModel):
    """Repository ruleset conditions for organization names

    Parameters for an organization name condition
    """

    organization_name: EnterpriseRulesetConditionsOrganizationNameTargetPropOrganizationName = Field()


model_rebuild(EnterpriseRulesetConditionsOrganizationNameTarget)

__all__ = ("EnterpriseRulesetConditionsOrganizationNameTarget",)
