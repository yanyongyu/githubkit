"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class OrgsOrgInvitationsPostBody(GitHubModel):
    """OrgsOrgInvitationsPostBody"""

    invitee_id: Missing[int] = Field(
        default=UNSET,
        description="**Required unless you provide `email`**. GitHub user ID for the person you are inviting.",
    )
    email: Missing[str] = Field(
        default=UNSET,
        description="**Required unless you provide `invitee_id`**. Email address of the person you are inviting, which can be an existing GitHub user.",
    )
    role: Missing[
        Literal["admin", "direct_member", "billing_manager", "reinstate"]
    ] = Field(
        default=UNSET,
        description="The role for the new member. \n * `admin` - Organization owners with full administrative rights to the organization and complete access to all repositories and teams.  \n * `direct_member` - Non-owner organization members with ability to see other members and join teams by invitation.  \n * `billing_manager` - Non-owner organization members with ability to manage the billing settings of your organization. \n * `reinstate` - The previous role assigned to the invitee before they were removed from your organization. Can be one of the roles listed above. Only works if the invitee was previously part of your organization.",
    )
    team_ids: Missing[List[int]] = Field(
        default=UNSET,
        description="Specify IDs for the teams you want to invite new members to.",
    )


model_rebuild(OrgsOrgInvitationsPostBody)

__all__ = ("OrgsOrgInvitationsPostBody",)
