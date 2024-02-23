"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryName(GitHubModel):
    """RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryName"""

    include: Missing[List[str]] = Field(
        default=UNSET,
        description="Array of repository names or patterns to include. One of these patterns must match for the condition to pass. Also accepts `~ALL` to include all repositories.",
    )
    exclude: Missing[List[str]] = Field(
        default=UNSET,
        description="Array of repository names or patterns to exclude. The condition will not pass if any of these patterns match.",
    )
    protected: Missing[bool] = Field(
        default=UNSET,
        description="Whether renaming of target repositories is prevented.",
    )


model_rebuild(RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryName)

__all__ = ("RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryName",)
