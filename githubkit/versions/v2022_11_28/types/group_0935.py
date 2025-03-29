"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0120 import RepositoryRulesetBypassActorType
from .group_0129 import OrgRulesetConditionsOneof0Type
from .group_0130 import OrgRulesetConditionsOneof1Type
from .group_0131 import OrgRulesetConditionsOneof2Type
from .group_0132 import (
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleRequiredSignaturesType,
)
from .group_0133 import RepositoryRuleUpdateType
from .group_0135 import RepositoryRuleRequiredLinearHistoryType
from .group_0136 import RepositoryRuleMergeQueueType
from .group_0138 import RepositoryRuleRequiredDeploymentsType
from .group_0141 import RepositoryRulePullRequestType
from .group_0143 import RepositoryRuleRequiredStatusChecksType
from .group_0145 import RepositoryRuleCommitMessagePatternType
from .group_0147 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0149 import RepositoryRuleCommitterEmailPatternType
from .group_0151 import RepositoryRuleBranchNamePatternType
from .group_0153 import RepositoryRuleTagNamePatternType
from .group_0155 import RepositoryRuleFilePathRestrictionType
from .group_0157 import RepositoryRuleMaxFilePathLengthType
from .group_0159 import RepositoryRuleFileExtensionRestrictionType
from .group_0161 import RepositoryRuleMaxFileSizeType
from .group_0164 import RepositoryRuleWorkflowsType
from .group_0166 import RepositoryRuleCodeScanningType


class OrgsOrgRulesetsRulesetIdPutBodyType(TypedDict):
    """OrgsOrgRulesetsRulesetIdPutBody"""

    name: NotRequired[str]
    target: NotRequired[Literal["branch", "tag", "push", "repository"]]
    enforcement: NotRequired[Literal["disabled", "active", "evaluate"]]
    bypass_actors: NotRequired[list[RepositoryRulesetBypassActorType]]
    conditions: NotRequired[
        Union[
            OrgRulesetConditionsOneof0Type,
            OrgRulesetConditionsOneof1Type,
            OrgRulesetConditionsOneof2Type,
        ]
    ]
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


__all__ = ("OrgsOrgRulesetsRulesetIdPutBodyType",)
