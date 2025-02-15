"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0134 import RulesetVersionWithStateAllof1PropState


class RulesetVersionWithStateAllof1(GitHubModel):
    """RulesetVersionWithStateAllof1"""

    state: RulesetVersionWithStateAllof1PropState = Field(
        description="The state of the ruleset version"
    )


model_rebuild(RulesetVersionWithStateAllof1)

__all__ = ("RulesetVersionWithStateAllof1",)
