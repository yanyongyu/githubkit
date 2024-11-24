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

from .group_0111 import RepositoryRulesetConditions


class WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItems(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItems"""

    condition: Missing[RepositoryRulesetConditions] = Field(
        default=UNSET,
        title="Repository ruleset conditions for ref names",
        description="Parameters for a repository ruleset ref name condition",
    )
    changes: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChanges
    ] = Field(default=UNSET)


class WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChanges(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChang
    es
    """

    condition_type: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropConditionType
    ] = Field(default=UNSET)
    target: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropTarget
    ] = Field(default=UNSET)
    include: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropInclude
    ] = Field(default=UNSET)
    exclude: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropExclude
    ] = Field(default=UNSET)


class WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropConditionType(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChang
    esPropConditionType
    """

    from_: Missing[str] = Field(default=UNSET, alias="from")


class WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropTarget(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChang
    esPropTarget
    """

    from_: Missing[str] = Field(default=UNSET, alias="from")


class WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropInclude(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChang
    esPropInclude
    """

    from_: Missing[list[str]] = Field(default=UNSET, alias="from")


class WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropExclude(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChang
    esPropExclude
    """

    from_: Missing[list[str]] = Field(default=UNSET, alias="from")


model_rebuild(WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItems)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChanges
)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropConditionType
)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropTarget
)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropInclude
)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropExclude
)

__all__ = (
    "WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItems",
    "WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChanges",
    "WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropConditionType",
    "WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropExclude",
    "WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropInclude",
    "WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropTarget",
)
