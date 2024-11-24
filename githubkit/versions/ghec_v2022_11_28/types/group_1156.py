"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired


class ScimV2OrganizationsOrgUsersPostBodyType(TypedDict):
    """ScimV2OrganizationsOrgUsersPostBody"""

    user_name: str
    display_name: NotRequired[str]
    name: ScimV2OrganizationsOrgUsersPostBodyPropNameType
    emails: list[ScimV2OrganizationsOrgUsersPostBodyPropEmailsItemsType]
    schemas: NotRequired[list[str]]
    external_id: NotRequired[str]
    groups: NotRequired[list[str]]
    active: NotRequired[bool]


class ScimV2OrganizationsOrgUsersPostBodyPropNameType(TypedDict):
    """ScimV2OrganizationsOrgUsersPostBodyPropName

    Examples:
        {'givenName': 'Jane', 'familyName': 'User'}
    """

    given_name: str
    family_name: str
    formatted: NotRequired[str]


class ScimV2OrganizationsOrgUsersPostBodyPropEmailsItemsType(TypedDict):
    """ScimV2OrganizationsOrgUsersPostBodyPropEmailsItems"""

    value: str
    primary: NotRequired[bool]
    type: NotRequired[str]


__all__ = (
    "ScimV2OrganizationsOrgUsersPostBodyPropEmailsItemsType",
    "ScimV2OrganizationsOrgUsersPostBodyPropNameType",
    "ScimV2OrganizationsOrgUsersPostBodyType",
)
