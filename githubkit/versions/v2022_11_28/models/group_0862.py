"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgCopilotBillingSelectedTeamsPostResponse201(GitHubModel):
    """OrgsOrgCopilotBillingSelectedTeamsPostResponse201

    The total number of seat assignments created.
    """

    seats_created: int = Field()


model_rebuild(OrgsOrgCopilotBillingSelectedTeamsPostResponse201)

__all__ = ("OrgsOrgCopilotBillingSelectedTeamsPostResponse201",)
