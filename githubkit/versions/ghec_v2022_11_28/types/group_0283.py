"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0059 import CodeSecurityConfigurationType


class CodeSecurityConfigurationForRepositoryType(TypedDict):
    """CodeSecurityConfigurationForRepository

    Code security configuration associated with a repository and attachment status
    """

    status: NotRequired[
        Literal[
            "attached",
            "attaching",
            "detached",
            "removed",
            "enforced",
            "failed",
            "updating",
            "removed_by_enterprise",
        ]
    ]
    configuration: NotRequired[CodeSecurityConfigurationType]


__all__ = ("CodeSecurityConfigurationForRepositoryType",)
