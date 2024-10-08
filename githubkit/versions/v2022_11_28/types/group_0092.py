"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired

from .group_0028 import TeamSimpleType


class TeamRoleAssignmentType(TypedDict):
    """A Role Assignment for a Team

    The Relationship a Team has with a role.
    """

    id: int
    node_id: str
    name: str
    slug: str
    description: Union[str, None]
    privacy: NotRequired[str]
    notification_setting: NotRequired[str]
    permission: str
    permissions: NotRequired[TeamRoleAssignmentPropPermissionsType]
    url: str
    html_url: str
    members_url: str
    repositories_url: str
    parent: Union[None, TeamSimpleType]


class TeamRoleAssignmentPropPermissionsType(TypedDict):
    """TeamRoleAssignmentPropPermissions"""

    pull: bool
    triage: bool
    push: bool
    maintain: bool
    admin: bool


__all__ = (
    "TeamRoleAssignmentType",
    "TeamRoleAssignmentPropPermissionsType",
)
