"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0110 import RepositoryRulesetBypassActorType
from .group_0111 import RepositoryRulesetConditionsType
from .group_0122 import (
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleOneof15Type,
    RepositoryRuleOneof17Type,
    RepositoryRuleRequiredSignaturesType,
)
from .group_0123 import RepositoryRuleUpdateType
from .group_0125 import (
    RepositoryRuleOneof16Type,
    RepositoryRuleRequiredLinearHistoryType,
)
from .group_0126 import RepositoryRuleMergeQueueType
from .group_0128 import RepositoryRuleRequiredDeploymentsType
from .group_0131 import RepositoryRulePullRequestType
from .group_0133 import RepositoryRuleRequiredStatusChecksType
from .group_0135 import RepositoryRuleCommitMessagePatternType
from .group_0137 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0139 import RepositoryRuleCommitterEmailPatternType
from .group_0141 import RepositoryRuleBranchNamePatternType
from .group_0143 import RepositoryRuleTagNamePatternType
from .group_0146 import RepositoryRuleWorkflowsType
from .group_0148 import RepositoryRuleCodeScanningType
from .group_0150 import RepositoryRuleOneof18Type


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
