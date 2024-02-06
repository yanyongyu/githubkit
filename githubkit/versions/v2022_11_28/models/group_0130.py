"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import Annotated

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0109 import RepositoryRuleUpdate
from .group_0128 import RepositoryRuleWorkflows
from .group_0114 import RepositoryRulePullRequest
from .group_0105 import OrgRulesetConditionsOneof0
from .group_0106 import OrgRulesetConditionsOneof1
from .group_0107 import OrgRulesetConditionsOneof2
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


class RepositoryRuleset(GitHubModel):
    """Repository ruleset

    A set of rules to apply when specified conditions are met.
    """

    id: int = Field(description="The ID of the ruleset")
    name: str = Field(description="The name of the ruleset")
    target: Missing[Literal["branch", "tag"]] = Field(
        default=UNSET, description="The target of the ruleset"
    )
    source_type: Missing[Literal["Repository", "Organization"]] = Field(
        default=UNSET, description="The type of the source of the ruleset"
    )
    source: str = Field(description="The name of the source")
    enforcement: Literal["disabled", "active", "evaluate"] = Field(
        description="The enforcement level of the ruleset. `evaluate` allows admins to test rules before enforcing them. Admins can view insights on the Rule Insights page (`evaluate` is only available with GitHub Enterprise)."
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
                RepositoryRuleWorkflows,
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
