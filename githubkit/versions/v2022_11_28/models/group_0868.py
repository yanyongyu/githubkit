"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgCopilotBillingSelectedTeamsDeleteBody(GitHubModel):
    """OrgsOrgCopilotBillingSelectedTeamsDeleteBody"""

    selected_teams: List[str] = Field(
        min_length=1,
        description="The names of teams from which to revoke access to GitHub Copilot.",
    )


model_rebuild(OrgsOrgCopilotBillingSelectedTeamsDeleteBody)

__all__ = ("OrgsOrgCopilotBillingSelectedTeamsDeleteBody",)
