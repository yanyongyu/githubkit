"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class RepositoryRulesetBypassActor(GitHubModel):
    """Repository Ruleset Bypass Actor

    An actor that can bypass rules in a ruleset
    """

    actor_id: Missing[Union[int, None]] = Field(
        default=UNSET,
        description="The ID of the actor that can bypass a ruleset. If `actor_type` is `OrganizationAdmin`, this should be `1`. If `actor_type` is `DeployKey`, this should be null. `OrganizationAdmin` is not applicable for personal repositories.",
    )
    actor_type: Literal[
        "Integration", "OrganizationAdmin", "RepositoryRole", "Team", "DeployKey"
    ] = Field(description="The type of actor that can bypass a ruleset.")
    bypass_mode: Literal["always", "pull_request"] = Field(
        description="When the specified actor can bypass the ruleset. `pull_request` means that an actor can only bypass rules on pull requests. `pull_request` is not applicable for the `DeployKey` actor type."
    )


model_rebuild(RepositoryRulesetBypassActor)

__all__ = ("RepositoryRulesetBypassActor",)
