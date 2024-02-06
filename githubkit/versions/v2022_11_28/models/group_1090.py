"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import Annotated

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0109 import RepositoryRuleUpdate
from .group_0128 import RepositoryRuleWorkflows
from .group_0114 import RepositoryRulePullRequest
from .group_0097 import RepositoryRulesetConditions
from .group_0096 import RepositoryRulesetBypassActor
from .group_0126 import RepositoryRuleTagNamePattern
from .group_0124 import RepositoryRuleBranchNamePattern
from .group_0112 import RepositoryRuleRequiredDeployments
from .group_0116 import RepositoryRuleRequiredStatusChecks
from .group_0118 import RepositoryRuleCommitMessagePattern
from .group_0111 import RepositoryRuleRequiredLinearHistory
from .group_0122 import RepositoryRuleCommitterEmailPattern
from .group_0120 import RepositoryRuleCommitAuthorEmailPattern
from .group_0108 import (
    RepositoryRuleCreation,
    RepositoryRuleDeletion,
    RepositoryRuleNonFastForward,
    RepositoryRuleRequiredSignatures,
)


class ReposOwnerRepoRulesetsPostBody(GitHubModel):
    """ReposOwnerRepoRulesetsPostBody"""

    name: str = Field(description="The name of the ruleset.")
    target: Missing[Literal["branch", "tag"]] = Field(
        default=UNSET, description="The target of the ruleset."
    )
    enforcement: Literal["disabled", "active", "evaluate"] = Field(
        description="The enforcement level of the ruleset. `evaluate` allows admins to test rules before enforcing them. Admins can view insights on the Rule Insights page (`evaluate` is only available with GitHub Enterprise)."
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


model_rebuild(ReposOwnerRepoRulesetsPostBody)

__all__ = ("ReposOwnerRepoRulesetsPostBody",)
