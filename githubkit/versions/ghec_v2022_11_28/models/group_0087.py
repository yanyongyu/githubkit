"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0088 import (
    RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryName,
)


class RepositoryRulesetConditionsRepositoryNameTarget(GitHubModel):
    """Repository ruleset conditions for repository names

    Parameters for a repository name condition
    """

    repository_name: RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryName = Field()


model_rebuild(RepositoryRulesetConditionsRepositoryNameTarget)

__all__ = ("RepositoryRulesetConditionsRepositoryNameTarget",)
