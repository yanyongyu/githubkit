"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0028 import CodeSecurityConfiguration


class CodeSecurityConfigurationForRepository(GitHubModel):
    """CodeSecurityConfigurationForRepository

    Code security configuration associated with a repository and attachment status
    """

    status: Missing[
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
    ] = Field(
        default=UNSET,
        description="The attachment status of the code security configuration on the repository.",
    )
    configuration: Missing[CodeSecurityConfiguration] = Field(
        default=UNSET, description="A code security configuration"
    )


model_rebuild(CodeSecurityConfigurationForRepository)

__all__ = ("CodeSecurityConfigurationForRepository",)
