"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0108 import (
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleRequiredSignaturesType,
)
from .group_0109 import RepositoryRuleUpdateType
from .group_0111 import RepositoryRuleRequiredLinearHistoryType
from .group_0112 import RepositoryRuleRequiredDeploymentsType
from .group_0114 import RepositoryRulePullRequestType
from .group_0116 import RepositoryRuleRequiredStatusChecksType
from .group_0118 import RepositoryRuleCommitMessagePatternType
from .group_0120 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0122 import RepositoryRuleCommitterEmailPatternType
from .group_0124 import RepositoryRuleBranchNamePatternType
from .group_0126 import RepositoryRuleTagNamePatternType
from .group_0129 import RepositoryRuleWorkflowsType
from .group_0734 import (
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsType,
)


class WebhookRepositoryRulesetEditedPropChangesPropRulesType(TypedDict):
    """WebhookRepositoryRulesetEditedPropChangesPropRules"""

    added: NotRequired[
        List[
            Union[
                RepositoryRuleCreationType,
                RepositoryRuleUpdateType,
                RepositoryRuleDeletionType,
                RepositoryRuleRequiredLinearHistoryType,
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
                RepositoryRuleWorkflowsType,
            ]
        ]
    ]
    deleted: NotRequired[
        List[
            Union[
                RepositoryRuleCreationType,
                RepositoryRuleUpdateType,
                RepositoryRuleDeletionType,
                RepositoryRuleRequiredLinearHistoryType,
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
                RepositoryRuleWorkflowsType,
            ]
        ]
    ]
    updated: NotRequired[
        List[WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsType]
    ]


__all__ = ("WebhookRepositoryRulesetEditedPropChangesPropRulesType",)
