"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0098 import RepositoryRulesetConditionsPropRefName
from .group_0100 import (
    RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryName,
)


class OrgRulesetConditionsOneof0(GitHubModel):
    """repository_name_and_ref_name

    Conditions to target repositories by name and refs by name
    """

    ref_name: Missing[RepositoryRulesetConditionsPropRefName] = Field(default=UNSET)
    repository_name: (
        RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryName
    ) = Field()


model_rebuild(OrgRulesetConditionsOneof0)

__all__ = ("OrgRulesetConditionsOneof0",)
