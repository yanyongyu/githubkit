"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0112 import RepositoryRulesetConditionsPropRefNameType


class RepositoryRulesetConditionsType(TypedDict):
    """Repository ruleset conditions for ref names

    Parameters for a repository ruleset ref name condition
    """

    ref_name: NotRequired[RepositoryRulesetConditionsPropRefNameType]


__all__ = ("RepositoryRulesetConditionsType",)
