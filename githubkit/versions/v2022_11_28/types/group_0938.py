"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0121 import RepositoryRulesetBypassActorType
from .group_0130 import OrgRulesetConditionsOneof0Type
from .group_0131 import OrgRulesetConditionsOneof1Type
from .group_0132 import OrgRulesetConditionsOneof2Type
from .group_0133 import (
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleRequiredSignaturesType,
)
from .group_0134 import RepositoryRuleUpdateType
from .group_0136 import RepositoryRuleRequiredLinearHistoryType
from .group_0137 import RepositoryRuleMergeQueueType
from .group_0139 import RepositoryRuleRequiredDeploymentsType
from .group_0142 import RepositoryRulePullRequestType
from .group_0144 import RepositoryRuleRequiredStatusChecksType
from .group_0146 import RepositoryRuleCommitMessagePatternType
from .group_0148 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0150 import RepositoryRuleCommitterEmailPatternType
from .group_0152 import RepositoryRuleBranchNamePatternType
from .group_0154 import RepositoryRuleTagNamePatternType
from .group_0156 import RepositoryRuleFilePathRestrictionType
from .group_0158 import RepositoryRuleMaxFilePathLengthType
from .group_0160 import RepositoryRuleFileExtensionRestrictionType
from .group_0162 import RepositoryRuleMaxFileSizeType
from .group_0165 import RepositoryRuleWorkflowsType
from .group_0167 import RepositoryRuleCodeScanningType


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
