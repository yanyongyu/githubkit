"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0132 import RepositoryRulePullRequestPropParametersType


class RepositoryRuleDetailedOneof7Type(TypedDict):
    """RepositoryRuleDetailedOneof7"""

    type: Literal["pull_request"]
    parameters: NotRequired[RepositoryRulePullRequestPropParametersType]
    ruleset_source_type: NotRequired[Literal["Repository", "Organization"]]
    ruleset_source: NotRequired[str]
    ruleset_id: NotRequired[int]


__all__ = ("RepositoryRuleDetailedOneof7Type",)
