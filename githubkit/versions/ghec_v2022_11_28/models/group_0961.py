"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0117 import RepositoryRulesetBypassActor
from .group_0126 import OrgRulesetConditionsOneof0
from .group_0127 import OrgRulesetConditionsOneof1
from .group_0128 import OrgRulesetConditionsOneof2
from .group_0129 import (
    RepositoryRuleCreation,
    RepositoryRuleDeletion,
    RepositoryRuleNonFastForward,
    RepositoryRuleRequiredSignatures,
)
from .group_0130 import RepositoryRuleUpdate
from .group_0132 import RepositoryRuleRequiredLinearHistory
from .group_0133 import RepositoryRuleRequiredDeployments
from .group_0135 import RepositoryRulePullRequest
from .group_0137 import RepositoryRuleRequiredStatusChecks
from .group_0139 import RepositoryRuleCommitMessagePattern
from .group_0141 import RepositoryRuleCommitAuthorEmailPattern
from .group_0143 import RepositoryRuleCommitterEmailPattern
from .group_0145 import RepositoryRuleBranchNamePattern
from .group_0147 import RepositoryRuleTagNamePattern
from .group_0150 import RepositoryRuleWorkflows


class OrgsOrgRulesetsRulesetIdPutBody(GitHubModel):
    """OrgsOrgRulesetsRulesetIdPutBody"""

    name: Missing[str] = Field(default=UNSET, description="The name of the ruleset.")
    target: Missing[Literal["branch", "tag"]] = Field(
        default=UNSET, description="The target of the ruleset."
    )
    enforcement: Missing[Literal["disabled", "active", "evaluate"]] = Field(
        default=UNSET,
        description="The enforcement level of the ruleset. `evaluate` allows admins to test rules before enforcing them. Admins can view insights on the Rule Insights page.",
    )
    bypass_actors: Missing[List[RepositoryRulesetBypassActor]] = Field(
        default=UNSET,
        description="The actors that can bypass the rules in this ruleset",
    )
    conditions: Missing[
        Union[
            OrgRulesetConditionsOneof0,
            OrgRulesetConditionsOneof1,
            OrgRulesetConditionsOneof2,
        ]
    ] = Field(
        default=UNSET,
        title="Organization ruleset conditions",
        description="Conditions for an organization ruleset. The conditions object should contain both `repository_name` and `ref_name` properties or both `repository_id` and `ref_name` properties.\n",
    )
    rules: Missing[
        List[
            Union[
                RepositoryRuleCreation,
                RepositoryRuleUpdate,
                RepositoryRuleDeletion,
                RepositoryRuleRequiredLinearHistory,
                RepositoryRuleRequiredDeployments,
                RepositoryRuleRequiredSignatures,
                RepositoryRulePullRequest,
                RepositoryRuleRequiredStatusChecks,
                RepositoryRuleNonFastForward,
                RepositoryRuleCommitMessagePattern,
                RepositoryRuleCommitAuthorEmailPattern,
                RepositoryRuleCommitterEmailPattern,
                RepositoryRuleBranchNamePattern,
                RepositoryRuleTagNamePattern,
                RepositoryRuleWorkflows,
            ]
        ]
    ] = Field(default=UNSET, description="An array of rules within the ruleset.")


model_rebuild(OrgsOrgRulesetsRulesetIdPutBody)

__all__ = ("OrgsOrgRulesetsRulesetIdPutBody",)
