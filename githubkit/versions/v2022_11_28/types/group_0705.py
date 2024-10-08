"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired

from .group_0116 import RepositoryRuleUpdateType
from .group_0142 import RepositoryRuleOneof18Type
from .group_0138 import RepositoryRuleWorkflowsType
from .group_0119 import RepositoryRuleMergeQueueType
from .group_0123 import RepositoryRulePullRequestType
from .group_0140 import RepositoryRuleCodeScanningType
from .group_0135 import RepositoryRuleTagNamePatternType
from .group_0133 import RepositoryRuleBranchNamePatternType
from .group_0121 import RepositoryRuleRequiredDeploymentsType
from .group_0125 import RepositoryRuleRequiredStatusChecksType
from .group_0127 import RepositoryRuleCommitMessagePatternType
from .group_0131 import RepositoryRuleCommitterEmailPatternType
from .group_0129 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0118 import (
    RepositoryRuleOneof16Type,
    RepositoryRuleRequiredLinearHistoryType,
)
from .group_0115 import (
    RepositoryRuleOneof15Type,
    RepositoryRuleOneof17Type,
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleRequiredSignaturesType,
)


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsType(TypedDict):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems"""

    rule: NotRequired[
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
    changes: NotRequired[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesType
    ]


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesType(
    TypedDict
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges"""

    configuration: NotRequired[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfigurationType
    ]
    rule_type: NotRequired[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleTypeType
    ]
    pattern: NotRequired[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPatternType
    ]


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfigurationType(
    TypedDict
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPro
    pConfiguration
    """

    from_: NotRequired[str]


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleTypeType(
    TypedDict
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPro
    pRuleType
    """

    from_: NotRequired[str]


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPatternType(
    TypedDict
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPro
    pPattern
    """

    from_: NotRequired[str]


__all__ = (
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsType",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesType",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfigurationType",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleTypeType",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPatternType",
)
