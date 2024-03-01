"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200(GitHubModel):
    """OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200

    The total number of seat assignments cancelled.
    """

    seats_cancelled: int = Field()


model_rebuild(OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200)

__all__ = ("OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200",)
