"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0094 import (
    EnterpriseRulesetConditionsOrganizationIdTargetPropOrganizationIdType,
)


class EnterpriseRulesetConditionsOrganizationIdTargetType(TypedDict):
    """Repository ruleset conditions for organization IDs

    Parameters for an organization ID condition
    """

    organization_id: (
        EnterpriseRulesetConditionsOrganizationIdTargetPropOrganizationIdType
    )


__all__ = ("EnterpriseRulesetConditionsOrganizationIdTargetType",)
