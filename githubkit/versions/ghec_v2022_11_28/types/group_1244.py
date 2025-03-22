"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0081 import RepositoryRulesetBypassActorType
from .group_0086 import RepositoryRulesetConditionsType
from .group_0096 import (
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleRequiredSignaturesType,
)
from .group_0097 import RepositoryRuleUpdateType
from .group_0099 import RepositoryRuleRequiredLinearHistoryType
from .group_0100 import RepositoryRuleMergeQueueType
from .group_0102 import RepositoryRuleRequiredDeploymentsType
from .group_0105 import RepositoryRulePullRequestType
from .group_0107 import RepositoryRuleRequiredStatusChecksType
from .group_0109 import RepositoryRuleCommitMessagePatternType
from .group_0111 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0113 import RepositoryRuleCommitterEmailPatternType
from .group_0115 import RepositoryRuleBranchNamePatternType
from .group_0117 import RepositoryRuleTagNamePatternType
from .group_0119 import RepositoryRuleFilePathRestrictionType
from .group_0121 import RepositoryRuleMaxFilePathLengthType
from .group_0123 import RepositoryRuleFileExtensionRestrictionType
from .group_0125 import RepositoryRuleMaxFileSizeType
from .group_0128 import RepositoryRuleWorkflowsType
from .group_0130 import RepositoryRuleCodeScanningType


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
                RepositoryRuleFilePathRestrictionType,
                RepositoryRuleMaxFilePathLengthType,
                RepositoryRuleFileExtensionRestrictionType,
                RepositoryRuleMaxFileSizeType,
                RepositoryRuleWorkflowsType,
                RepositoryRuleCodeScanningType,
            ]
        ]
    ]


__all__ = ("ReposOwnerRepoRulesetsRulesetIdPutBodyType",)
