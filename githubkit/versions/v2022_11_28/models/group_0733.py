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

from .group_0109 import RepositoryRuleUpdate
from .group_0129 import RepositoryRuleWorkflows
from .group_0114 import RepositoryRulePullRequest
from .group_0126 import RepositoryRuleTagNamePattern
from .group_0124 import RepositoryRuleBranchNamePattern
from .group_0112 import RepositoryRuleRequiredDeployments
from .group_0116 import RepositoryRuleRequiredStatusChecks
from .group_0118 import RepositoryRuleCommitMessagePattern
from .group_0111 import RepositoryRuleRequiredLinearHistory
from .group_0122 import RepositoryRuleCommitterEmailPattern
from .group_0120 import RepositoryRuleCommitAuthorEmailPattern
from .group_0734 import (
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems,
)
from .group_0108 import (
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
                RepositoryRuleWorkflows,
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
                RepositoryRuleWorkflows,
            ]
        ]
    ] = Field(default=UNSET)
    updated: Missing[
        List[WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems]
    ] = Field(default=UNSET)


model_rebuild(WebhookRepositoryRulesetEditedPropChangesPropRules)

__all__ = ("WebhookRepositoryRulesetEditedPropChangesPropRules",)
