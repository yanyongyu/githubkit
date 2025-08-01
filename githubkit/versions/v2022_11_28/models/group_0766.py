"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0128 import RepositoryRulesetConditions
from .group_0767 import (
    WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItems,
)


class WebhookRepositoryRulesetEditedPropChangesPropConditions(GitHubModel):
    """WebhookRepositoryRulesetEditedPropChangesPropConditions"""

    added: Missing[list[RepositoryRulesetConditions]] = Field(default=UNSET)
    deleted: Missing[list[RepositoryRulesetConditions]] = Field(default=UNSET)
    updated: Missing[
        list[WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItems]
    ] = Field(default=UNSET)


model_rebuild(WebhookRepositoryRulesetEditedPropChangesPropConditions)

__all__ = ("WebhookRepositoryRulesetEditedPropChangesPropConditions",)
