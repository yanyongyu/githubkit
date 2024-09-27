"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0141 import RepositoryRuleUpdate
from .group_0167 import RepositoryRuleOneof18
from .group_0163 import RepositoryRuleWorkflows
from .group_0144 import RepositoryRuleMergeQueue
from .group_0148 import RepositoryRulePullRequest
from .group_0165 import RepositoryRuleCodeScanning
from .group_0129 import RepositoryRulesetConditions
from .group_0128 import RepositoryRulesetBypassActor
from .group_0160 import RepositoryRuleTagNamePattern
from .group_0158 import RepositoryRuleBranchNamePattern
from .group_0146 import RepositoryRuleRequiredDeployments
from .group_0150 import RepositoryRuleRequiredStatusChecks
from .group_0152 import RepositoryRuleCommitMessagePattern
from .group_0156 import RepositoryRuleCommitterEmailPattern
from .group_0154 import RepositoryRuleCommitAuthorEmailPattern
from .group_0143 import RepositoryRuleOneof16, RepositoryRuleRequiredLinearHistory
from .group_0140 import (
    RepositoryRuleOneof15,
    RepositoryRuleOneof17,
    RepositoryRuleCreation,
    RepositoryRuleDeletion,
    RepositoryRuleNonFastForward,
    RepositoryRuleRequiredSignatures,
)


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
    bypass_actors: Missing[List[RepositoryRulesetBypassActor]] = Field(
        default=UNSET,
        description="The actors that can bypass the rules in this ruleset",
    )
    conditions: Missing[RepositoryRulesetConditions] = Field(
        default=UNSET,
        title="Repository ruleset conditions for ref names",
        description="Parameters for a repository ruleset ref name condition",
    )
    rules: Missing[
        List[
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
