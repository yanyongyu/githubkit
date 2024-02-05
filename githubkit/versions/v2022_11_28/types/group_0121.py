"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class RepositoryRuleCommitAuthorEmailPatternPropParametersType(TypedDict):
    """RepositoryRuleCommitAuthorEmailPatternPropParameters"""

    name: NotRequired[str]
    negate: NotRequired[bool]
    operator: Literal["starts_with", "ends_with", "contains", "regex"]
    pattern: str


__all__ = ("RepositoryRuleCommitAuthorEmailPatternPropParametersType",)
