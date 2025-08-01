"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0457 import UserRoleItemsType


class UserType(TypedDict):
    """User"""

    schemas: list[Literal["urn:ietf:params:scim:schemas:core:2.0:User"]]
    external_id: str
    active: bool
    user_name: str
    name: NotRequired[UserNameType]
    display_name: str
    emails: list[UserEmailsItemsType]
    roles: NotRequired[list[UserRoleItemsType]]


class UserNameType(TypedDict):
    """UserName"""

    formatted: NotRequired[str]
    family_name: str
    given_name: str
    middle_name: NotRequired[str]


class UserEmailsItemsType(TypedDict):
    """UserEmailsItems"""

    value: str
    type: str
    primary: bool


__all__ = (
    "UserEmailsItemsType",
    "UserNameType",
    "UserType",
)
