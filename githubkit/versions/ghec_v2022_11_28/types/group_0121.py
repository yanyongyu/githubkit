"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0122 import RepositoryRuleMaxFilePathLengthPropParametersType


class RepositoryRuleMaxFilePathLengthType(TypedDict):
    """max_file_path_length

    Prevent commits that include file paths that exceed the specified character
    limit from being pushed to the commit graph.
    """

    type: Literal["max_file_path_length"]
    parameters: NotRequired[RepositoryRuleMaxFilePathLengthPropParametersType]


__all__ = ("RepositoryRuleMaxFilePathLengthType",)
