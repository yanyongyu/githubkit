"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class ExternalGroupsType(TypedDict):
    """ExternalGroups

    A list of external groups available to be connected to a team
    """

    groups: NotRequired[List[ExternalGroupsPropGroupsItemsType]]


class ExternalGroupsPropGroupsItemsType(TypedDict):
    """ExternalGroupsPropGroupsItems"""

    group_id: int
    group_name: str
    updated_at: str


__all__ = (
    "ExternalGroupsType",
    "ExternalGroupsPropGroupsItemsType",
)
