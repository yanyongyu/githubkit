"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgCopilotBillingSelectedUsersDeleteBody(GitHubModel):
    """OrgsOrgCopilotBillingSelectedUsersDeleteBody"""

    selected_usernames: List[str] = Field(
        min_length=1,
        description="The usernames of the organization members for which to revoke access to GitHub Copilot.",
    )


model_rebuild(OrgsOrgCopilotBillingSelectedUsersDeleteBody)

__all__ = ("OrgsOrgCopilotBillingSelectedUsersDeleteBody",)
