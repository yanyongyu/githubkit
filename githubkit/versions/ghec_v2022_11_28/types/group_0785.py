"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0085 import RepositoryRulesetConditionsType
from .group_0786 import (
    WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsType,
)


class WebhookRepositoryRulesetEditedPropChangesPropConditionsType(TypedDict):
    """WebhookRepositoryRulesetEditedPropChangesPropConditions"""

    added: NotRequired[list[RepositoryRulesetConditionsType]]
    deleted: NotRequired[list[RepositoryRulesetConditionsType]]
    updated: NotRequired[
        list[
            WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsType
        ]
    ]


__all__ = ("WebhookRepositoryRulesetEditedPropChangesPropConditionsType",)
