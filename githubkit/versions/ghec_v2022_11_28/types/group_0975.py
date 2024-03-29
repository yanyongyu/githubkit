"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class OrgsOrgTeamsTeamSlugTeamSyncGroupMappingsPatchBodyType(TypedDict):
    """OrgsOrgTeamsTeamSlugTeamSyncGroupMappingsPatchBody"""

    groups: NotRequired[
        List[OrgsOrgTeamsTeamSlugTeamSyncGroupMappingsPatchBodyPropGroupsItemsType]
    ]


class OrgsOrgTeamsTeamSlugTeamSyncGroupMappingsPatchBodyPropGroupsItemsType(TypedDict):
    """OrgsOrgTeamsTeamSlugTeamSyncGroupMappingsPatchBodyPropGroupsItems"""

    group_id: str
    group_name: str
    group_description: str


__all__ = (
    "OrgsOrgTeamsTeamSlugTeamSyncGroupMappingsPatchBodyType",
    "OrgsOrgTeamsTeamSlugTeamSyncGroupMappingsPatchBodyPropGroupsItemsType",
)
