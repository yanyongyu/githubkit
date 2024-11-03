"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0147 import RepositoryRuleUpdateType
from .group_0173 import RepositoryRuleOneof18Type
from .group_0169 import RepositoryRuleWorkflowsType
from .group_0150 import RepositoryRuleMergeQueueType
from .group_0154 import RepositoryRulePullRequestType
from .group_0171 import RepositoryRuleCodeScanningType
from .group_0135 import RepositoryRulesetConditionsType
from .group_0134 import RepositoryRulesetBypassActorType
from .group_0166 import RepositoryRuleTagNamePatternType
from .group_0164 import RepositoryRuleBranchNamePatternType
from .group_0152 import RepositoryRuleRequiredDeploymentsType
from .group_0156 import RepositoryRuleRequiredStatusChecksType
from .group_0158 import RepositoryRuleCommitMessagePatternType
from .group_0162 import RepositoryRuleCommitterEmailPatternType
from .group_0160 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0149 import (
    RepositoryRuleOneof16Type,
    RepositoryRuleRequiredLinearHistoryType,
)
from .group_0146 import (
    RepositoryRuleOneof15Type,
    RepositoryRuleOneof17Type,
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleRequiredSignaturesType,
)


class ReposOwnerRepoRulesetsRulesetIdPutBodyType(TypedDict):
    """ReposOwnerRepoRulesetsRulesetIdPutBody"""

    name: NotRequired[str]
    target: NotRequired[Literal["branch", "tag", "push"]]
    enforcement: NotRequired[Literal["disabled", "active", "evaluate"]]
    bypass_actors: NotRequired[list[RepositoryRulesetBypassActorType]]
    conditions: NotRequired[RepositoryRulesetConditionsType]
    rules: NotRequired[
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


__all__ = ("ReposOwnerRepoRulesetsRulesetIdPutBodyType",)
