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


class RulesetVersionPropActor(GitHubModel):
    """RulesetVersionPropActor

    The actor who updated the ruleset
    """

    id: Missing[int] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)


model_rebuild(RulesetVersionPropActor)

__all__ = ("RulesetVersionPropActor",)
