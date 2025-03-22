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

from .group_0133 import (
    RepositoryRuleCreation,
    RepositoryRuleDeletion,
    RepositoryRuleNonFastForward,
    RepositoryRuleRequiredSignatures,
)
from .group_0134 import RepositoryRuleUpdate
from .group_0136 import RepositoryRuleRequiredLinearHistory
from .group_0137 import RepositoryRuleMergeQueue
from .group_0139 import RepositoryRuleRequiredDeployments
from .group_0142 import RepositoryRulePullRequest
from .group_0144 import RepositoryRuleRequiredStatusChecks
from .group_0146 import RepositoryRuleCommitMessagePattern
from .group_0148 import RepositoryRuleCommitAuthorEmailPattern
from .group_0150 import RepositoryRuleCommitterEmailPattern
from .group_0152 import RepositoryRuleBranchNamePattern
from .group_0154 import RepositoryRuleTagNamePattern
from .group_0156 import RepositoryRuleFilePathRestriction
from .group_0158 import RepositoryRuleMaxFilePathLength
from .group_0160 import RepositoryRuleFileExtensionRestriction
from .group_0162 import RepositoryRuleMaxFileSize
from .group_0165 import RepositoryRuleWorkflows
from .group_0167 import RepositoryRuleCodeScanning
from .group_0759 import (
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
