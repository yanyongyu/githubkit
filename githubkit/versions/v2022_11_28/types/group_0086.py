"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType


class OrganizationRoleType(TypedDict):
    """Organization Role

    Organization roles
    """

    id: int
    name: str
    description: NotRequired[Union[str, None]]
    permissions: List[str]
    organization: Union[None, SimpleUserType]
    created_at: datetime
    updated_at: datetime


class OrgsOrgOrganizationRolesGetResponse200Type(TypedDict):
    """OrgsOrgOrganizationRolesGetResponse200"""

    total_count: NotRequired[int]
    roles: NotRequired[List[OrganizationRoleType]]


__all__ = (
    "OrganizationRoleType",
    "OrgsOrgOrganizationRolesGetResponse200Type",
)
