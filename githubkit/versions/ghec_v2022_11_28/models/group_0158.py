"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0133 import RepositoryRuleUpdate
from .group_0157 import RepositoryRuleOneof17
from .group_0153 import RepositoryRuleWorkflows
from .group_0138 import RepositoryRulePullRequest
from .group_0129 import OrgRulesetConditionsOneof0
from .group_0130 import OrgRulesetConditionsOneof1
from .group_0131 import OrgRulesetConditionsOneof2
from .group_0155 import RepositoryRuleCodeScanning
from .group_0121 import RepositoryRulesetConditions
from .group_0120 import RepositoryRulesetBypassActor
from .group_0150 import RepositoryRuleTagNamePattern
from .group_0148 import RepositoryRuleBranchNamePattern
from .group_0136 import RepositoryRuleRequiredDeployments
from .group_0140 import RepositoryRuleRequiredStatusChecks
from .group_0142 import RepositoryRuleCommitMessagePattern
from .group_0146 import RepositoryRuleCommitterEmailPattern
from .group_0144 import RepositoryRuleCommitAuthorEmailPattern
from .group_0135 import RepositoryRuleOneof15, RepositoryRuleRequiredLinearHistory
from .group_0132 import (
    RepositoryRuleOneof14,
    RepositoryRuleOneof16,
    RepositoryRuleCreation,
    RepositoryRuleDeletion,
    RepositoryRuleNonFastForward,
    RepositoryRuleRequiredSignatures,
)


class RepositoryRuleset(GitHubModel):
    """Repository ruleset

    A set of rules to apply when specified conditions are met.
    """

    id: int = Field(description="The ID of the ruleset")
    name: str = Field(description="The name of the ruleset")
    target: Missing[Literal["branch", "tag", "push"]] = Field(
        default=UNSET,
        description="The target of the ruleset\n\n**Note**: The `push` target is in beta and is subject to change.",
    )
    source_type: Missing[Literal["Repository", "Organization"]] = Field(
        default=UNSET, description="The type of the source of the ruleset"
    )
    source: str = Field(description="The name of the source")
    enforcement: Literal["disabled", "active", "evaluate"] = Field(
        description="The enforcement level of the ruleset. `evaluate` allows admins to test rules before enforcing them. Admins can view insights on the Rule Insights page."
    )
    bypass_actors: Missing[List[RepositoryRulesetBypassActor]] = Field(
        default=UNSET,
        description="The actors that can bypass the rules in this ruleset",
    )
    current_user_can_bypass: Missing[
        Literal["always", "pull_requests_only", "never"]
    ] = Field(
        default=UNSET,
        description="The bypass type of the user making the API request for this ruleset. This field is only returned when\nquerying the repository-level endpoint.",
    )
    node_id: Missing[str] = Field(default=UNSET)
    links: Missing[RepositoryRulesetPropLinks] = Field(default=UNSET, alias="_links")
    conditions: Missing[
        Union[
            RepositoryRulesetConditions,
            OrgRulesetConditionsOneof0,
            OrgRulesetConditionsOneof1,
            OrgRulesetConditionsOneof2,
            None,
        ]
    ] = Field(default=UNSET)
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
                RepositoryRuleOneof14,
                RepositoryRuleOneof15,
                RepositoryRuleOneof16,
                RepositoryRuleOneof17,
                RepositoryRuleWorkflows,
                RepositoryRuleCodeScanning,
            ]
        ]
    ] = Field(default=UNSET)
    created_at: Missing[datetime] = Field(default=UNSET)
    updated_at: Missing[datetime] = Field(default=UNSET)


class RepositoryRulesetPropLinks(GitHubModel):
    """RepositoryRulesetPropLinks"""

    self_: Missing[RepositoryRulesetPropLinksPropSelf] = Field(
        default=UNSET, alias="self"
    )
    html: Missing[RepositoryRulesetPropLinksPropHtml] = Field(default=UNSET)


class RepositoryRulesetPropLinksPropSelf(GitHubModel):
    """RepositoryRulesetPropLinksPropSelf"""

    href: Missing[str] = Field(default=UNSET, description="The URL of the ruleset")


class RepositoryRulesetPropLinksPropHtml(GitHubModel):
    """RepositoryRulesetPropLinksPropHtml"""

    href: Missing[str] = Field(default=UNSET, description="The html URL of the ruleset")


model_rebuild(RepositoryRuleset)
model_rebuild(RepositoryRulesetPropLinks)
model_rebuild(RepositoryRulesetPropLinksPropSelf)
model_rebuild(RepositoryRulesetPropLinksPropHtml)

__all__ = (
    "RepositoryRuleset",
    "RepositoryRulesetPropLinks",
    "RepositoryRulesetPropLinksPropSelf",
    "RepositoryRulesetPropLinksPropHtml",
)
