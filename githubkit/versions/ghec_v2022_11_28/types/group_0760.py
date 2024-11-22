"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired

from .group_0153 import RepositoryRuleUpdateType
from .group_0180 import RepositoryRuleOneof18Type
from .group_0176 import RepositoryRuleWorkflowsType
from .group_0156 import RepositoryRuleMergeQueueType
from .group_0161 import RepositoryRulePullRequestType
from .group_0178 import RepositoryRuleCodeScanningType
from .group_0173 import RepositoryRuleTagNamePatternType
from .group_0171 import RepositoryRuleBranchNamePatternType
from .group_0158 import RepositoryRuleRequiredDeploymentsType
from .group_0163 import RepositoryRuleRequiredStatusChecksType
from .group_0165 import RepositoryRuleCommitMessagePatternType
from .group_0169 import RepositoryRuleCommitterEmailPatternType
from .group_0167 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0155 import (
    RepositoryRuleOneof16Type,
    RepositoryRuleRequiredLinearHistoryType,
)
from .group_0761 import (
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsType,
)
from .group_0152 import (
    RepositoryRuleOneof15Type,
    RepositoryRuleOneof17Type,
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleRequiredSignaturesType,
)


class WebhookRepositoryRulesetEditedPropChangesPropRulesType(TypedDict):
    """WebhookRepositoryRulesetEditedPropChangesPropRules"""

    added: NotRequired[
        list[
            Union[
                RepositoryRuleCreationType,
                RepositoryRuleUpdateType,
                RepositoryRuleDeletionType,
                RepositoryRuleRequiredLinearHistoryType,
                RepositoryRuleMergeQueueType,
                RepositoryRuleRequiredDeploymentsType,
                RepositoryRuleRequiredSignaturesType,
                RepositoryRulePullRequestType,
                RepositoryRuleRequiredStatusChecksType,
                RepositoryRuleNonFastForwardType,
                RepositoryRuleCommitMessagePatternType,
                RepositoryRuleCommitAuthorEmailPatternType,
                RepositoryRuleCommitterEmailPatternType,
                RepositoryRuleBranchNamePatternType,
                RepositoryRuleTagNamePatternType,
                RepositoryRuleOneof15Type,
                RepositoryRuleOneof16Type,
                RepositoryRuleOneof17Type,
                RepositoryRuleOneof18Type,
                RepositoryRuleWorkflowsType,
                RepositoryRuleCodeScanningType,
            ]
        ]
    ]
    deleted: NotRequired[
        list[
            Union[
                RepositoryRuleCreationType,
                RepositoryRuleUpdateType,
                RepositoryRuleDeletionType,
                RepositoryRuleRequiredLinearHistoryType,
                RepositoryRuleMergeQueueType,
                RepositoryRuleRequiredDeploymentsType,
                RepositoryRuleRequiredSignaturesType,
                RepositoryRulePullRequestType,
                RepositoryRuleRequiredStatusChecksType,
                RepositoryRuleNonFastForwardType,
                RepositoryRuleCommitMessagePatternType,
                RepositoryRuleCommitAuthorEmailPatternType,
                RepositoryRuleCommitterEmailPatternType,
                RepositoryRuleBranchNamePatternType,
                RepositoryRuleTagNamePatternType,
                RepositoryRuleOneof15Type,
                RepositoryRuleOneof16Type,
                RepositoryRuleOneof17Type,
                RepositoryRuleOneof18Type,
                RepositoryRuleWorkflowsType,
                RepositoryRuleCodeScanningType,
            ]
        ]
    ]
    updated: NotRequired[
        list[WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsType]
    ]


__all__ = ("WebhookRepositoryRulesetEditedPropChangesPropRulesType",)
