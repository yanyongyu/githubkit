"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0172 import RulesetVersionPropActor


class RulesetVersion(GitHubModel):
    """Ruleset version

    The historical version of a ruleset
    """

    version_id: int = Field(description="The ID of the previous version of the ruleset")
    actor: RulesetVersionPropActor = Field(
        description="The actor who updated the ruleset"
    )
    updated_at: datetime = Field()


model_rebuild(RulesetVersion)

__all__ = ("RulesetVersion",)
