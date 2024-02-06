"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgCopilotBillingSelectedTeamsPostBody(GitHubModel):
    """OrgsOrgCopilotBillingSelectedTeamsPostBody"""

    selected_teams: List[str] = Field(
        min_length=1,
        description="List of team names within the organization to which to grant access to GitHub Copilot.",
    )


model_rebuild(OrgsOrgCopilotBillingSelectedTeamsPostBody)

__all__ = ("OrgsOrgCopilotBillingSelectedTeamsPostBody",)
