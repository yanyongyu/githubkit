"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0109 import RepositoryRuleRequiredStatusChecksPropParametersType


class RepositoryRuleDetailedOneof8Type(TypedDict):
    """RepositoryRuleDetailedOneof8"""

    type: Literal["required_status_checks"]
    parameters: NotRequired[RepositoryRuleRequiredStatusChecksPropParametersType]
    ruleset_source_type: NotRequired[Literal["Repository", "Organization"]]
    ruleset_source: NotRequired[str]
    ruleset_id: NotRequired[int]


__all__ = ("RepositoryRuleDetailedOneof8Type",)
