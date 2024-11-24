"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Any, Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired


class ScimUserListType(TypedDict):
    """SCIM User List

    SCIM User List
    """

    schemas: list[str]
    total_results: int
    items_per_page: int
    start_index: int
    resources: list[ScimUserType]


class ScimUserType(TypedDict):
    """SCIM /Users

    SCIM /Users provisioning endpoints
    """

    schemas: list[str]
    id: str
    external_id: NotRequired[Union[str, None]]
    user_name: NotRequired[Union[str, None]]
    display_name: NotRequired[Union[str, None]]
    name: NotRequired[ScimUserPropNameType]
    emails: list[ScimUserPropEmailsItemsType]
    active: bool
    meta: ScimUserPropMetaType
    organization_id: NotRequired[int]
    operations: NotRequired[list[ScimUserPropOperationsItemsType]]
    groups: NotRequired[list[ScimUserPropGroupsItemsType]]
    roles: NotRequired[list[ScimUserPropRolesItemsType]]


class ScimUserPropNameType(TypedDict):
    """ScimUserPropName

    Examples:
        {'givenName': 'Jane', 'familyName': 'User'}
    """

    given_name: NotRequired[Union[str, None]]
    family_name: NotRequired[Union[str, None]]
    formatted: NotRequired[Union[str, None]]


class ScimUserPropEmailsItemsType(TypedDict):
    """ScimUserPropEmailsItems"""

    value: str
    primary: NotRequired[bool]
    type: NotRequired[str]


class ScimUserPropMetaType(TypedDict):
    """ScimUserPropMeta"""

    resource_type: NotRequired[str]
    created: NotRequired[datetime]
    last_modified: NotRequired[datetime]
    location: NotRequired[str]


class ScimUserPropGroupsItemsType(TypedDict):
    """ScimUserPropGroupsItems"""

    value: NotRequired[str]
    display: NotRequired[str]


class ScimUserPropRolesItemsType(TypedDict):
    """ScimUserPropRolesItems"""

    value: NotRequired[str]
    primary: NotRequired[bool]
    type: NotRequired[str]
    display: NotRequired[str]


class ScimUserPropOperationsItemsType(TypedDict):
    """ScimUserPropOperationsItems"""

    op: Literal["add", "remove", "replace"]
    path: NotRequired[str]
    value: NotRequired[
        Union[str, ScimUserPropOperationsItemsPropValueOneof1Type, list[Any]]
    ]


class ScimUserPropOperationsItemsPropValueOneof1Type(TypedDict):
    """ScimUserPropOperationsItemsPropValueOneof1"""


__all__ = (
    "ScimUserListType",
    "ScimUserPropEmailsItemsType",
    "ScimUserPropGroupsItemsType",
    "ScimUserPropMetaType",
    "ScimUserPropNameType",
    "ScimUserPropOperationsItemsPropValueOneof1Type",
    "ScimUserPropOperationsItemsType",
    "ScimUserPropRolesItemsType",
    "ScimUserType",
)
