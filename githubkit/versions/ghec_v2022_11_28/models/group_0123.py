"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0124 import RepositoryRulesetConditionsRepositoryIdTargetPropRepositoryId


class RepositoryRulesetConditionsRepositoryIdTarget(GitHubModel):
    """Repository ruleset conditions for repository IDs

    Parameters for a repository ID condition
    """

    repository_id: RepositoryRulesetConditionsRepositoryIdTargetPropRepositoryId = (
        Field()
    )


model_rebuild(RepositoryRulesetConditionsRepositoryIdTarget)

__all__ = ("RepositoryRulesetConditionsRepositoryIdTarget",)
