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

from .group_0095 import (
    RepositoryRuleCreation,
    RepositoryRuleDeletion,
    RepositoryRuleNonFastForward,
    RepositoryRuleOneof15,
    RepositoryRuleOneof17,
    RepositoryRuleRequiredSignatures,
)
from .group_0096 import RepositoryRuleUpdate
from .group_0098 import RepositoryRuleOneof16, RepositoryRuleRequiredLinearHistory
from .group_0099 import RepositoryRuleMergeQueue
from .group_0101 import RepositoryRuleRequiredDeployments
from .group_0104 import RepositoryRulePullRequest
from .group_0106 import RepositoryRuleRequiredStatusChecks
from .group_0108 import RepositoryRuleCommitMessagePattern
from .group_0110 import RepositoryRuleCommitAuthorEmailPattern
from .group_0112 import RepositoryRuleCommitterEmailPattern
from .group_0114 import RepositoryRuleBranchNamePattern
from .group_0116 import RepositoryRuleTagNamePattern
from .group_0119 import RepositoryRuleWorkflows
from .group_0121 import RepositoryRuleCodeScanning
from .group_0123 import RepositoryRuleOneof18
from .group_0793 import (
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
                RepositoryRuleOneof15,
                RepositoryRuleOneof16,
                RepositoryRuleOneof17,
                RepositoryRuleOneof18,
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
                RepositoryRuleOneof15,
                RepositoryRuleOneof16,
                RepositoryRuleOneof17,
                RepositoryRuleOneof18,
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
