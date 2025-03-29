"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0080 import RepositoryRulesetBypassActorType
from .group_0085 import RepositoryRulesetConditionsType
from .group_0095 import (
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleRequiredSignaturesType,
)
from .group_0096 import RepositoryRuleUpdateType
from .group_0098 import RepositoryRuleRequiredLinearHistoryType
from .group_0099 import RepositoryRuleMergeQueueType
from .group_0101 import RepositoryRuleRequiredDeploymentsType
from .group_0104 import RepositoryRulePullRequestType
from .group_0106 import RepositoryRuleRequiredStatusChecksType
from .group_0108 import RepositoryRuleCommitMessagePatternType
from .group_0110 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0112 import RepositoryRuleCommitterEmailPatternType
from .group_0114 import RepositoryRuleBranchNamePatternType
from .group_0116 import RepositoryRuleTagNamePatternType
from .group_0118 import RepositoryRuleFilePathRestrictionType
from .group_0120 import RepositoryRuleMaxFilePathLengthType
from .group_0122 import RepositoryRuleFileExtensionRestrictionType
from .group_0124 import RepositoryRuleMaxFileSizeType
from .group_0127 import RepositoryRuleWorkflowsType
from .group_0129 import RepositoryRuleCodeScanningType


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
