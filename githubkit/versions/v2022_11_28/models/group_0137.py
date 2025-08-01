"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0129 import RepositoryRulesetConditionsPropRefName
from .group_0133 import RepositoryRulesetConditionsRepositoryIdTargetPropRepositoryId


class OrgRulesetConditionsOneof1(GitHubModel):
    """repository_id_and_ref_name

    Conditions to target repositories by id and refs by name
    """

    ref_name: Missing[RepositoryRulesetConditionsPropRefName] = Field(default=UNSET)
    repository_id: RepositoryRulesetConditionsRepositoryIdTargetPropRepositoryId = (
        Field()
    )


model_rebuild(OrgRulesetConditionsOneof1)

__all__ = ("OrgRulesetConditionsOneof1",)
