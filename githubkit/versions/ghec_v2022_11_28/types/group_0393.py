"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0392 import MetaType


class ScimEnterpriseGroupResponseType(TypedDict):
    """ScimEnterpriseGroupResponse"""

    schemas: list[
        Literal[
            "urn:ietf:params:scim:schemas:core:2.0:Group",
            "urn:ietf:params:scim:api:messages:2.0:ListResponse",
        ]
    ]
    external_id: NotRequired[Union[str, None]]
    display_name: NotRequired[Union[str, None]]
    members: NotRequired[list[ScimEnterpriseGroupResponseMergedMembersType]]
    id: NotRequired[str]
    meta: NotRequired[MetaType]


class ScimEnterpriseGroupResponseMergedMembersType(TypedDict):
    """ScimEnterpriseGroupResponseMergedMembers"""

    value: str
    ref: str
    display: NotRequired[str]


class ScimEnterpriseGroupListType(TypedDict):
    """ScimEnterpriseGroupList"""

    schemas: list[Literal["urn:ietf:params:scim:api:messages:2.0:ListResponse"]]
    total_results: int
    resources: list[ScimEnterpriseGroupResponseType]
    start_index: int
    items_per_page: int


__all__ = (
    "ScimEnterpriseGroupListType",
    "ScimEnterpriseGroupResponseMergedMembersType",
    "ScimEnterpriseGroupResponseType",
)
