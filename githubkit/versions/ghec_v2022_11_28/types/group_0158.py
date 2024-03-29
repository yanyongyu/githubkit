"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict, NotRequired


class GroupMappingType(TypedDict):
    """GroupMapping

    External Groups to be mapped to a team for membership
    """

    groups: NotRequired[List[GroupMappingPropGroupsItemsType]]


class GroupMappingPropGroupsItemsType(TypedDict):
    """GroupMappingPropGroupsItems"""

    group_id: str
    group_name: str
    group_description: str
    status: NotRequired[str]
    synced_at: NotRequired[Union[str, None]]


__all__ = (
    "GroupMappingType",
    "GroupMappingPropGroupsItemsType",
)
