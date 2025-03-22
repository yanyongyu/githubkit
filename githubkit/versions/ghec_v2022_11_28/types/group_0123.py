"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0124 import RepositoryRuleFileExtensionRestrictionPropParametersType


class RepositoryRuleFileExtensionRestrictionType(TypedDict):
    """file_extension_restriction

    Prevent commits that include files with specified file extensions from being
    pushed to the commit graph.
    """

    type: Literal["file_extension_restriction"]
    parameters: NotRequired[RepositoryRuleFileExtensionRestrictionPropParametersType]


__all__ = ("RepositoryRuleFileExtensionRestrictionType",)
