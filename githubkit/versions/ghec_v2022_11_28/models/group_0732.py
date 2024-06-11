"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0133 import RepositoryRuleUpdate
from .group_0157 import RepositoryRuleOneof17
from .group_0153 import RepositoryRuleWorkflows
from .group_0138 import RepositoryRulePullRequest
from .group_0155 import RepositoryRuleCodeScanning
from .group_0150 import RepositoryRuleTagNamePattern
from .group_0148 import RepositoryRuleBranchNamePattern
from .group_0136 import RepositoryRuleRequiredDeployments
from .group_0140 import RepositoryRuleRequiredStatusChecks
from .group_0142 import RepositoryRuleCommitMessagePattern
from .group_0146 import RepositoryRuleCommitterEmailPattern
from .group_0144 import RepositoryRuleCommitAuthorEmailPattern
from .group_0135 import RepositoryRuleOneof15, RepositoryRuleRequiredLinearHistory
from .group_0733 import (
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems,
)
from .group_0132 import (
    RepositoryRuleOneof14,
    RepositoryRuleOneof16,
    RepositoryRuleCreation,
    RepositoryRuleDeletion,
    RepositoryRuleNonFastForward,
    RepositoryRuleRequiredSignatures,
)


class WebhookRepositoryRulesetEditedPropChangesPropRules(GitHubModel):
    """WebhookRepositoryRulesetEditedPropChangesPropRules"""

    added: Missing[
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
    deleted: Missing[
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
    updated: Missing[
        List[WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems]
    ] = Field(default=UNSET)


model_rebuild(WebhookRepositoryRulesetEditedPropChangesPropRules)

__all__ = ("WebhookRepositoryRulesetEditedPropChangesPropRules",)
