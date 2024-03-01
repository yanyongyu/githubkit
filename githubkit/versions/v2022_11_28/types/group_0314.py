"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0125 import RepositoryRuleBranchNamePatternPropParametersType


class RepositoryRuleDetailedOneof12Type(TypedDict):
    """RepositoryRuleDetailedOneof12"""

    type: Literal["branch_name_pattern"]
    parameters: NotRequired[RepositoryRuleBranchNamePatternPropParametersType]
    ruleset_source_type: NotRequired[Literal["Repository", "Organization"]]
    ruleset_source: NotRequired[str]
    ruleset_id: NotRequired[int]


__all__ = ("RepositoryRuleDetailedOneof12Type",)
