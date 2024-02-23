"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class TeamsTeamIdReposOwnerRepoPutBody(GitHubModel):
    """TeamsTeamIdReposOwnerRepoPutBody"""

    permission: Missing[Literal["pull", "push", "admin"]] = Field(
        default=UNSET,
        description="The permission to grant the team on this repository. If no permission is specified, the team's `permission` attribute will be used to determine what permission to grant the team on this repository.",
    )


model_rebuild(TeamsTeamIdReposOwnerRepoPutBody)

__all__ = ("TeamsTeamIdReposOwnerRepoPutBody",)
