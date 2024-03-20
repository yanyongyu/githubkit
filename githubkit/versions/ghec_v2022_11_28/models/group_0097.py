"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ExternalGroup(GitHubModel):
    """ExternalGroup

    Information about an external group's usage and its members
    """

    group_id: int = Field(description="The internal ID of the group")
    group_name: str = Field(description="The display name for the group")
    updated_at: Missing[str] = Field(
        default=UNSET, description="The date when the group was last updated_at"
    )
    teams: List[ExternalGroupPropTeamsItems] = Field(
        description="An array of teams linked to this group"
    )
    members: List[ExternalGroupPropMembersItems] = Field(
        description="An array of external members linked to this group"
    )


class ExternalGroupPropTeamsItems(GitHubModel):
    """ExternalGroupPropTeamsItems"""

    team_id: int = Field(description="The id for a team")
    team_name: str = Field(description="The name of the team")


class ExternalGroupPropMembersItems(GitHubModel):
    """ExternalGroupPropMembersItems"""

    member_id: int = Field(description="The internal user ID of the identity")
    member_login: str = Field(description="The handle/login for the user")
    member_name: str = Field(description="The user display name/profile name")
    member_email: str = Field(description="An email attached to a user")


model_rebuild(ExternalGroup)
model_rebuild(ExternalGroupPropTeamsItems)
model_rebuild(ExternalGroupPropMembersItems)

__all__ = (
    "ExternalGroup",
    "ExternalGroupPropTeamsItems",
    "ExternalGroupPropMembersItems",
)
