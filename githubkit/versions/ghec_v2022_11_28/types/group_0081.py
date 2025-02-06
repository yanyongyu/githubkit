"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0082 import (
    EnterpriseRulesetConditionsOrganizationNameTargetPropOrganizationNameType,
)


class EnterpriseRulesetConditionsOrganizationNameTargetType(TypedDict):
    """Repository ruleset conditions for organization names

    Parameters for an organization name condition
    """

    organization_name: (
        EnterpriseRulesetConditionsOrganizationNameTargetPropOrganizationNameType
    )


__all__ = ("EnterpriseRulesetConditionsOrganizationNameTargetType",)
