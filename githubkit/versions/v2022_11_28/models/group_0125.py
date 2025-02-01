"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0126 import (
    RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryProperty,
)


class RepositoryRulesetConditionsRepositoryPropertyTarget(GitHubModel):
    """Repository ruleset conditions for repository properties

    Parameters for a repository property condition
    """

    repository_property: RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryProperty = Field()


model_rebuild(RepositoryRulesetConditionsRepositoryPropertyTarget)

__all__ = ("RepositoryRulesetConditionsRepositoryPropertyTarget",)
