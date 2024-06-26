"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class RepositoryRuleRequiredLinearHistoryType(TypedDict):
    """required_linear_history

    Prevent merge commits from being pushed to matching refs.
    """

    type: Literal["required_linear_history"]


class RepositoryRuleOneof15Type(TypedDict):
    """max_file_path_length

    Note: max_file_path_length is in beta and subject to change.

    Prevent commits that include file paths that exceed a specified character limit
    from being pushed to the commit graph.
    """

    type: Literal["max_file_path_length"]
    parameters: NotRequired[RepositoryRuleOneof15PropParametersType]


class RepositoryRuleOneof15PropParametersType(TypedDict):
    """RepositoryRuleOneof15PropParameters"""

    max_file_path_length: int


__all__ = (
    "RepositoryRuleRequiredLinearHistoryType",
    "RepositoryRuleOneof15Type",
    "RepositoryRuleOneof15PropParametersType",
)
