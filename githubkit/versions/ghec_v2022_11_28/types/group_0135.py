"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0086 import RepositoryRulesetConditionsPropRefNameType
from .group_0088 import (
    RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryPropertyType,
)


class OrgRulesetConditionsOneof2Type(TypedDict):
    """repository_property_and_ref_name

    Conditions to target repositories by property and refs by name
    """

    ref_name: NotRequired[RepositoryRulesetConditionsPropRefNameType]
    repository_property: (
        RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryPropertyType
    )


__all__ = ("OrgRulesetConditionsOneof2Type",)
