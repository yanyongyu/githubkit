"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0060 import OrganizationSimpleType


class OrgMembershipType(TypedDict):
    """Org Membership

    Org Membership
    """

    url: str
    state: Literal["active", "pending"]
    role: Literal["admin", "member", "billing_manager"]
    organization_url: str
    organization: OrganizationSimpleType
    user: Union[None, SimpleUserType]
    permissions: NotRequired[OrgMembershipPropPermissionsType]


class OrgMembershipPropPermissionsType(TypedDict):
    """OrgMembershipPropPermissions"""

    can_create_repository: bool


__all__ = (
    "OrgMembershipPropPermissionsType",
    "OrgMembershipType",
)
