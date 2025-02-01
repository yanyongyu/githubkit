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

from .group_0083 import (
    RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryName,
)
from .group_0085 import RepositoryRulesetConditionsPropRefName
from .group_0089 import (
    EnterpriseRulesetConditionsOrganizationIdTargetPropOrganizationId,
)


class EnterpriseRulesetConditionsOneof2(GitHubModel):
    """organization_id_and_repository_name

    Conditions to target organizations by id and all repositories
    """

    organization_id: EnterpriseRulesetConditionsOrganizationIdTargetPropOrganizationId = Field()
    repository_name: RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryName = Field()
    ref_name: Missing[RepositoryRulesetConditionsPropRefName] = Field(default=UNSET)


model_rebuild(EnterpriseRulesetConditionsOneof2)

__all__ = ("EnterpriseRulesetConditionsOneof2",)
