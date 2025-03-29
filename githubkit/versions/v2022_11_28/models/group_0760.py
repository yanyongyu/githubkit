"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0132 import (
    RepositoryRuleCreation,
    RepositoryRuleDeletion,
    RepositoryRuleNonFastForward,
    RepositoryRuleRequiredSignatures,
)
from .group_0133 import RepositoryRuleUpdate
from .group_0135 import RepositoryRuleRequiredLinearHistory
from .group_0136 import RepositoryRuleMergeQueue
from .group_0138 import RepositoryRuleRequiredDeployments
from .group_0141 import RepositoryRulePullRequest
from .group_0143 import RepositoryRuleRequiredStatusChecks
from .group_0145 import RepositoryRuleCommitMessagePattern
from .group_0147 import RepositoryRuleCommitAuthorEmailPattern
from .group_0149 import RepositoryRuleCommitterEmailPattern
from .group_0151 import RepositoryRuleBranchNamePattern
from .group_0153 import RepositoryRuleTagNamePattern
from .group_0155 import RepositoryRuleFilePathRestriction
from .group_0157 import RepositoryRuleMaxFilePathLength
from .group_0159 import RepositoryRuleFileExtensionRestriction
from .group_0161 import RepositoryRuleMaxFileSize
from .group_0164 import RepositoryRuleWorkflows
from .group_0166 import RepositoryRuleCodeScanning
from .group_0761 import (
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems,
)


class WebhookRepositoryRulesetEditedPropChangesPropRules(GitHubModel):
    """WebhookRepositoryRulesetEditedPropChangesPropRules"""

    added: Missing[
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
                RepositoryRuleFilePathRestriction,
                RepositoryRuleMaxFilePathLength,
                RepositoryRuleFileExtensionRestriction,
                RepositoryRuleMaxFileSize,
                RepositoryRuleWorkflows,
                RepositoryRuleCodeScanning,
            ]
        ]
    ] = Field(default=UNSET)
    deleted: Missing[
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
                RepositoryRuleFilePathRestriction,
                RepositoryRuleMaxFilePathLength,
                RepositoryRuleFileExtensionRestriction,
                RepositoryRuleMaxFileSize,
                RepositoryRuleWorkflows,
                RepositoryRuleCodeScanning,
            ]
        ]
    ] = Field(default=UNSET)
    updated: Missing[
        list[WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems]
    ] = Field(default=UNSET)


model_rebuild(WebhookRepositoryRulesetEditedPropChangesPropRules)

__all__ = ("WebhookRepositoryRulesetEditedPropChangesPropRules",)
