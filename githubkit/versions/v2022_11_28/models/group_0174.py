"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0173 import RulesetVersionPropActor
from .group_0176 import RulesetVersionWithStateAllof1PropState


class RulesetVersionWithState(GitHubModel):
    """RulesetVersionWithState"""

    version_id: int = Field(description="The ID of the previous version of the ruleset")
    actor: RulesetVersionPropActor = Field(
        description="The actor who updated the ruleset"
    )
    updated_at: datetime = Field()
    state: RulesetVersionWithStateAllof1PropState = Field(
        description="The state of the ruleset version"
    )


model_rebuild(RulesetVersionWithState)

__all__ = ("RulesetVersionWithState",)
