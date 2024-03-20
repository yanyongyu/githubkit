"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations


from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0119 import RepositoryRulesetConditionsPropRefName


class RepositoryRulesetConditions(GitHubModel):
    """Repository ruleset conditions for ref names

    Parameters for a repository ruleset ref name condition
    """

    ref_name: Missing[RepositoryRulesetConditionsPropRefName] = Field(default=UNSET)


model_rebuild(RepositoryRulesetConditions)

__all__ = ("RepositoryRulesetConditions",)
