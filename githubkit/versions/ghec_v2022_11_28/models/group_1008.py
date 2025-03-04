"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0081 import RepositoryRulesetBypassActor
from .group_0096 import (
    RepositoryRuleCreation,
    RepositoryRuleDeletion,
    RepositoryRuleNonFastForward,
    RepositoryRuleOneof15,
    RepositoryRuleOneof17,
    RepositoryRuleRequiredSignatures,
)
from .group_0097 import RepositoryRuleUpdate
from .group_0099 import RepositoryRuleOneof16, RepositoryRuleRequiredLinearHistory
from .group_0100 import RepositoryRuleMergeQueue
from .group_0102 import RepositoryRuleRequiredDeployments
from .group_0105 import RepositoryRulePullRequest
from .group_0107 import RepositoryRuleRequiredStatusChecks
from .group_0109 import RepositoryRuleCommitMessagePattern
from .group_0111 import RepositoryRuleCommitAuthorEmailPattern
from .group_0113 import RepositoryRuleCommitterEmailPattern
from .group_0115 import RepositoryRuleBranchNamePattern
from .group_0117 import RepositoryRuleTagNamePattern
from .group_0120 import RepositoryRuleWorkflows
from .group_0122 import RepositoryRuleCodeScanning
from .group_0124 import RepositoryRuleOneof18
from .group_0127 import OrgRulesetConditionsOneof0
from .group_0128 import OrgRulesetConditionsOneof1
from .group_0129 import OrgRulesetConditionsOneof2


class OrgsOrgRulesetsRulesetIdPutBody(GitHubModel):
    """OrgsOrgRulesetsRulesetIdPutBody"""

    name: Missing[str] = Field(default=UNSET, description="The name of the ruleset.")
    target: Missing[Literal["branch", "tag", "push", "repository"]] = Field(
        default=UNSET, description="The target of the ruleset"
    )
    enforcement: Missing[Literal["disabled", "active", "evaluate"]] = Field(
        default=UNSET,
        description="The enforcement level of the ruleset. `evaluate` allows admins to test rules before enforcing them. Admins can view insights on the Rule Insights page. `evaluate` is not available for the `repository` target.",
    )
    bypass_actors: Missing[list[RepositoryRulesetBypassActor]] = Field(
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
        description="Conditions for an organization ruleset.\nThe branch and tag rulesets conditions object should contain both `repository_name` and `ref_name` properties, or both `repository_id` and `ref_name` properties, or both `repository_property` and `ref_name` properties.\nThe push rulesets conditions object does not require the `ref_name` property.\nFor repository policy rulesets, the conditions object should only contain the `repository_name`, the `repository_id`, or the `repository_property`.",
    )
    rules: Missing[
        list[
            Union[
                RepositoryRuleCreation,
                RepositoryRuleUpdate,
                RepositoryRuleDeletion,
                RepositoryRuleRequiredLinearHistory,
                RepositoryRuleMergeQueue,
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
                RepositoryRuleOneof15,
                RepositoryRuleOneof16,
                RepositoryRuleOneof17,
                RepositoryRuleOneof18,
                RepositoryRuleWorkflows,
                RepositoryRuleCodeScanning,
            ]
        ]
    ] = Field(default=UNSET, description="An array of rules within the ruleset.")


model_rebuild(OrgsOrgRulesetsRulesetIdPutBody)

__all__ = ("OrgsOrgRulesetsRulesetIdPutBody",)
