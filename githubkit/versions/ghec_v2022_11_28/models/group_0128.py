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
from .group_0125 import (
    RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryProperty,
)


class OrgRulesetConditionsOneof2(GitHubModel):
    """repository_property_and_ref_name

    Conditions to target repositories by property and refs by name
    """

    ref_name: Missing[RepositoryRulesetConditionsPropRefName] = Field(default=UNSET)
    repository_property: RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryProperty = Field()


model_rebuild(OrgRulesetConditionsOneof2)

__all__ = ("OrgRulesetConditionsOneof2",)
