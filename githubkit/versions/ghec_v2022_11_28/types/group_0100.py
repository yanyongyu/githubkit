"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0099 import CodeSecurityConfigurationType


class CodeSecurityDefaultConfigurationsItemsType(TypedDict):
    """CodeSecurityDefaultConfigurationsItems"""

    default_for_new_repos: NotRequired[Literal["public", "private_and_internal", "all"]]
    configuration: NotRequired[CodeSecurityConfigurationType]


__all__ = ("CodeSecurityDefaultConfigurationsItemsType",)
