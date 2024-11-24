"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0140 import RepositoryRulesetBypassActor
from .group_0141 import RepositoryRulesetConditions
from .group_0152 import (
    RepositoryRuleOneof15,
    RepositoryRuleOneof17,
    RepositoryRuleCreation,
    RepositoryRuleDeletion,
    RepositoryRuleNonFastForward,
    RepositoryRuleRequiredSignatures,
)
from .group_0153 import RepositoryRuleUpdate
from .group_0155 import RepositoryRuleOneof16, RepositoryRuleRequiredLinearHistory
from .group_0156 import RepositoryRuleMergeQueue
from .group_0158 import RepositoryRuleRequiredDeployments
from .group_0161 import RepositoryRulePullRequest
from .group_0163 import RepositoryRuleRequiredStatusChecks
from .group_0165 import RepositoryRuleCommitMessagePattern
from .group_0167 import RepositoryRuleCommitAuthorEmailPattern
from .group_0169 import RepositoryRuleCommitterEmailPattern
from .group_0171 import RepositoryRuleBranchNamePattern
from .group_0173 import RepositoryRuleTagNamePattern
from .group_0176 import RepositoryRuleWorkflows
from .group_0178 import RepositoryRuleCodeScanning
from .group_0180 import RepositoryRuleOneof18


class ReposOwnerRepoRulesetsRulesetIdPutBody(GitHubModel):
    """ReposOwnerRepoRulesetsRulesetIdPutBody"""

    name: Missing[str] = Field(default=UNSET, description="The name of the ruleset.")
    target: Missing[Literal["branch", "tag", "push"]] = Field(
        default=UNSET, description="The target of the ruleset"
    )
    enforcement: Missing[Literal["disabled", "active", "evaluate"]] = Field(
        default=UNSET,
        description="The enforcement level of the ruleset. `evaluate` allows admins to test rules before enforcing them. Admins can view insights on the Rule Insights page.",
    )
    bypass_actors: Missing[list[RepositoryRulesetBypassActor]] = Field(
        default=UNSET,
        description="The actors that can bypass the rules in this ruleset",
    )
    conditions: Missing[RepositoryRulesetConditions] = Field(
        default=UNSET,
        title="Repository ruleset conditions for ref names",
        description="Parameters for a repository ruleset ref name condition",
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


model_rebuild(ReposOwnerRepoRulesetsRulesetIdPutBody)

__all__ = ("ReposOwnerRepoRulesetsRulesetIdPutBody",)
