"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class GetConsumedLicenses(GitHubModel):
    """Enterprise Consumed Licenses

    A breakdown of the licenses consumed by an enterprise.
    """

    total_seats_consumed: Missing[int] = Field(default=UNSET)
    total_seats_purchased: Missing[int] = Field(default=UNSET)
    users: Missing[List[GetConsumedLicensesPropUsersItems]] = Field(default=UNSET)


class GetConsumedLicensesPropUsersItems(GitHubModel):
    """GetConsumedLicensesPropUsersItems"""

    github_com_login: Missing[str] = Field(default=UNSET)
    github_com_name: Missing[Union[str, None]] = Field(default=UNSET)
    enterprise_server_user_ids: Missing[List[str]] = Field(default=UNSET)
    github_com_user: Missing[bool] = Field(default=UNSET)
    enterprise_server_user: Missing[Union[bool, None]] = Field(default=UNSET)
    visual_studio_subscription_user: Missing[bool] = Field(default=UNSET)
    license_type: Missing[str] = Field(default=UNSET)
    github_com_profile: Missing[Union[str, None]] = Field(default=UNSET)
    github_com_member_roles: Missing[List[str]] = Field(default=UNSET)
    github_com_enterprise_roles: Missing[List[str]] = Field(
        default=UNSET, description="All enterprise roles for a user."
    )
    github_com_verified_domain_emails: Missing[List[str]] = Field(default=UNSET)
    github_com_saml_name_id: Missing[Union[str, None]] = Field(default=UNSET)
    github_com_orgs_with_pending_invites: Missing[List[str]] = Field(default=UNSET)
    github_com_two_factor_auth: Missing[Union[bool, None]] = Field(default=UNSET)
    enterprise_server_emails: Missing[List[str]] = Field(default=UNSET)
    visual_studio_license_status: Missing[Union[str, None]] = Field(default=UNSET)
    visual_studio_subscription_email: Missing[Union[str, None]] = Field(default=UNSET)
    total_user_accounts: Missing[int] = Field(default=UNSET)


model_rebuild(GetConsumedLicenses)
model_rebuild(GetConsumedLicensesPropUsersItems)

__all__ = (
    "GetConsumedLicenses",
    "GetConsumedLicensesPropUsersItems",
)
