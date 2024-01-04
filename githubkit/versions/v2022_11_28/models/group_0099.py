"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0100 import (
    RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryName,
)


class RepositoryRulesetConditionsRepositoryNameTarget(GitHubModel):
    """Repository ruleset conditions for repository names

    Parameters for a repository name condition
    """

    repository_name: RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryName = (
        Field()
    )


model_rebuild(RepositoryRulesetConditionsRepositoryNameTarget)

__all__ = ("RepositoryRulesetConditionsRepositoryNameTarget",)
