"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import PYDANTIC_V2, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class ScimV2OrganizationsOrgUsersScimUserIdPutBody(GitHubModel):
    """ScimV2OrganizationsOrgUsersScimUserIdPutBody"""

    schemas: Missing[list[str]] = Field(default=UNSET)
    display_name: Missing[str] = Field(
        default=UNSET,
        alias="displayName",
        description="The name of the user, suitable for display to end-users",
    )
    external_id: Missing[str] = Field(default=UNSET, alias="externalId")
    groups: Missing[list[str]] = Field(default=UNSET)
    active: Missing[bool] = Field(default=UNSET)
    user_name: str = Field(
        alias="userName",
        description="Configured by the admin. Could be an email, login, or username",
    )
    name: ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropName = Field()
    emails: list[ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItems] = Field(
        min_length=1 if PYDANTIC_V2 else None, description="user emails"
    )


class ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropName(GitHubModel):
    """ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropName

    Examples:
        {'givenName': 'Jane', 'familyName': 'User'}
    """

    given_name: str = Field(alias="givenName")
    family_name: str = Field(alias="familyName")
    formatted: Missing[str] = Field(default=UNSET)


class ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItems(GitHubModel):
    """ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItems"""

    type: Missing[str] = Field(default=UNSET)
    value: str = Field()
    primary: Missing[bool] = Field(default=UNSET)


model_rebuild(ScimV2OrganizationsOrgUsersScimUserIdPutBody)
model_rebuild(ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropName)
model_rebuild(ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItems)

__all__ = (
    "ScimV2OrganizationsOrgUsersScimUserIdPutBody",
    "ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItems",
    "ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropName",
)
