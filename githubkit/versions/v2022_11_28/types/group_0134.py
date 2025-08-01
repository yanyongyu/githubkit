"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0135 import (
    RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryPropertyType,
)


class RepositoryRulesetConditionsRepositoryPropertyTargetType(TypedDict):
    """Repository ruleset conditions for repository properties

    Parameters for a repository property condition
    """

    repository_property: (
        RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryPropertyType
    )


__all__ = ("RepositoryRulesetConditionsRepositoryPropertyTargetType",)
