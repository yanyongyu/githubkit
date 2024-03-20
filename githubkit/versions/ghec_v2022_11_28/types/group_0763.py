"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing_extensions import TypedDict, NotRequired

from .group_0766 import WebhookRepositoryRulesetEditedPropChangesPropRulesType
from .group_0764 import WebhookRepositoryRulesetEditedPropChangesPropConditionsType


class WebhookRepositoryRulesetEditedPropChangesType(TypedDict):
    """WebhookRepositoryRulesetEditedPropChanges"""

    name: NotRequired[WebhookRepositoryRulesetEditedPropChangesPropNameType]
    enforcement: NotRequired[
        WebhookRepositoryRulesetEditedPropChangesPropEnforcementType
    ]
    conditions: NotRequired[WebhookRepositoryRulesetEditedPropChangesPropConditionsType]
    rules: NotRequired[WebhookRepositoryRulesetEditedPropChangesPropRulesType]


class WebhookRepositoryRulesetEditedPropChangesPropNameType(TypedDict):
    """WebhookRepositoryRulesetEditedPropChangesPropName"""

    from_: NotRequired[str]


class WebhookRepositoryRulesetEditedPropChangesPropEnforcementType(TypedDict):
    """WebhookRepositoryRulesetEditedPropChangesPropEnforcement"""

    from_: NotRequired[str]


__all__ = (
    "WebhookRepositoryRulesetEditedPropChangesType",
    "WebhookRepositoryRulesetEditedPropChangesPropNameType",
    "WebhookRepositoryRulesetEditedPropChangesPropEnforcementType",
)