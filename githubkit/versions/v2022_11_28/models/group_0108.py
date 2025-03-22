"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0087 import TeamSimple


class TeamRoleAssignment(GitHubModel):
    """A Role Assignment for a Team

    The Relationship a Team has with a role.
    """

    assignment: Missing[Literal["direct", "indirect", "mixed"]] = Field(
        default=UNSET,
        description="Determines if the team has a direct, indirect, or mixed relationship to a role",
    )
    id: int = Field()
    node_id: str = Field()
    name: str = Field()
    slug: str = Field()
    description: Union[str, None] = Field()
    privacy: Missing[str] = Field(default=UNSET)
    notification_setting: Missing[str] = Field(default=UNSET)
    permission: str = Field()
    permissions: Missing[TeamRoleAssignmentPropPermissions] = Field(default=UNSET)
    url: str = Field()
    html_url: str = Field()
    members_url: str = Field()
    repositories_url: str = Field()
    parent: Union[None, TeamSimple] = Field()


class TeamRoleAssignmentPropPermissions(GitHubModel):
    """TeamRoleAssignmentPropPermissions"""

    pull: bool = Field()
    triage: bool = Field()
    push: bool = Field()
    maintain: bool = Field()
    admin: bool = Field()


model_rebuild(TeamRoleAssignment)
model_rebuild(TeamRoleAssignmentPropPermissions)

__all__ = (
    "TeamRoleAssignment",
    "TeamRoleAssignmentPropPermissions",
)
