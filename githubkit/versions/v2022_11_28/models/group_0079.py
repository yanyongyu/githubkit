"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser


class OrganizationInvitation(GitHubModel):
    """Organization Invitation

    Organization Invitation
    """

    id: int = Field()
    login: Union[str, None] = Field()
    email: Union[str, None] = Field()
    role: str = Field()
    created_at: str = Field()
    failed_at: Missing[Union[str, None]] = Field(default=UNSET)
    failed_reason: Missing[Union[str, None]] = Field(default=UNSET)
    inviter: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    team_count: int = Field()
    node_id: str = Field()
    invitation_teams_url: str = Field()
    invitation_source: Missing[str] = Field(default=UNSET)


model_rebuild(OrganizationInvitation)

__all__ = ("OrganizationInvitation",)
