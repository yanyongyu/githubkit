"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0079 import RepositoryRulesetBypassActorType
from .group_0090 import EnterpriseRulesetConditionsOneof0Type
from .group_0091 import EnterpriseRulesetConditionsOneof1Type
from .group_0092 import EnterpriseRulesetConditionsOneof2Type
from .group_0093 import EnterpriseRulesetConditionsOneof3Type
from .group_0094 import (
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleOneof15Type,
    RepositoryRuleOneof17Type,
    RepositoryRuleRequiredSignaturesType,
)
from .group_0095 import RepositoryRuleUpdateType
from .group_0097 import (
    RepositoryRuleOneof16Type,
    RepositoryRuleRequiredLinearHistoryType,
)
from .group_0098 import RepositoryRuleMergeQueueType
from .group_0100 import RepositoryRuleRequiredDeploymentsType
from .group_0103 import RepositoryRulePullRequestType
from .group_0105 import RepositoryRuleRequiredStatusChecksType
from .group_0107 import RepositoryRuleCommitMessagePatternType
from .group_0109 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0111 import RepositoryRuleCommitterEmailPatternType
from .group_0113 import RepositoryRuleBranchNamePatternType
from .group_0115 import RepositoryRuleTagNamePatternType
from .group_0118 import RepositoryRuleWorkflowsType
from .group_0120 import RepositoryRuleCodeScanningType
from .group_0122 import RepositoryRuleOneof18Type


class EnterprisesEnterpriseRulesetsPostBodyType(TypedDict):
    """EnterprisesEnterpriseRulesetsPostBody"""

    name: str
    target: NotRequired[Literal["branch", "tag", "push", "repository"]]
    enforcement: Literal["disabled", "active", "evaluate"]
    bypass_actors: NotRequired[list[RepositoryRulesetBypassActorType]]
    conditions: NotRequired[
        Union[
            EnterpriseRulesetConditionsOneof0Type,
            EnterpriseRulesetConditionsOneof1Type,
            EnterpriseRulesetConditionsOneof2Type,
            EnterpriseRulesetConditionsOneof3Type,
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
                RepositoryRuleOneof15Type,
                RepositoryRuleOneof16Type,
                RepositoryRuleOneof17Type,
                RepositoryRuleOneof18Type,
                RepositoryRuleWorkflowsType,
                RepositoryRuleCodeScanningType,
            ]
        ]
    ]


__all__ = ("EnterprisesEnterpriseRulesetsPostBodyType",)
