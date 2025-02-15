"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0421 import MetaType
from .group_0426 import UserEmailsResponseItemsType, UserNameResponseType
from .group_0427 import UserRoleItemsType
from .group_0431 import ScimEnterpriseUserResponseAllof1PropGroupsItemsType


class ScimEnterpriseUserResponseType(TypedDict):
    """ScimEnterpriseUserResponse"""

    schemas: list[Literal["urn:ietf:params:scim:schemas:core:2.0:User"]]
    external_id: NotRequired[Union[str, None]]
    active: bool
    user_name: NotRequired[str]
    name: NotRequired[UserNameResponseType]
    display_name: NotRequired[Union[str, None]]
    emails: list[UserEmailsResponseItemsType]
    roles: NotRequired[list[UserRoleItemsType]]
    id: str
    groups: NotRequired[list[ScimEnterpriseUserResponseAllof1PropGroupsItemsType]]
    meta: MetaType


class ScimEnterpriseUserListType(TypedDict):
    """ScimEnterpriseUserList"""

    schemas: list[Literal["urn:ietf:params:scim:api:messages:2.0:ListResponse"]]
    total_results: int
    resources: list[ScimEnterpriseUserResponseType]
    start_index: int
    items_per_page: int


__all__ = (
    "ScimEnterpriseUserListType",
    "ScimEnterpriseUserResponseType",
)
