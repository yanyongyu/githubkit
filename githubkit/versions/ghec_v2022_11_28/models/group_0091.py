"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union
from datetime import date, datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0001 import SimpleUser
from .group_0090 import Team


class CopilotSeatDetails(GitHubModel):
    """Copilot Business Seat Detail

    Information about a Copilot Business seat assignment for a user, team, or
    organization.
    """

    assignee: Union[SimpleUser, Team, Organization] = Field(
        description="The assignee that has been granted access to GitHub Copilot."
    )
    assigning_team: Missing[Union[Team, None]] = Field(
        default=UNSET,
        description="The team that granted access to GitHub Copilot to the assignee. This will be null if the user was assigned a seat individually.",
    )
    pending_cancellation_date: Missing[Union[date, None]] = Field(
        default=UNSET,
        description="The pending cancellation date for the seat, in `YYYY-MM-DD` format. This will be null unless the assignee's Copilot access has been canceled during the current billing cycle. If the seat has been cancelled, this corresponds to the start of the organization's next billing cycle.",
    )
    last_activity_at: Missing[Union[datetime, None]] = Field(
        default=UNSET,
        description="Timestamp of user's last GitHub Copilot activity, in ISO 8601 format.",
    )
    last_activity_editor: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="Last editor that was used by the user for a GitHub Copilot completion.",
    )
    created_at: datetime = Field(
        description="Timestamp of when the assignee was last granted access to GitHub Copilot, in ISO 8601 format."
    )
    updated_at: Missing[datetime] = Field(
        default=UNSET,
        description="Timestamp of when the assignee's GitHub Copilot access was last updated, in ISO 8601 format.",
    )


class Organization(GitHubModel):
    """Organization

    GitHub account for managing multiple users, teams, and repositories
    """

    login: str = Field(description="Unique login name of the organization")
    url: str = Field(description="URL for the organization")
    id: int = Field()
    node_id: str = Field()
    repos_url: str = Field()
    events_url: str = Field()
    hooks_url: str = Field()
    issues_url: str = Field()
    members_url: str = Field()
    public_members_url: str = Field()
    avatar_url: str = Field()
    description: Union[str, None] = Field()
    blog: Missing[str] = Field(
        default=UNSET, description="Display blog url for the organization"
    )
    html_url: str = Field()
    name: Missing[str] = Field(
        default=UNSET, description="Display name for the organization"
    )
    company: Missing[str] = Field(
        default=UNSET, description="Display company name for the organization"
    )
    location: Missing[str] = Field(
        default=UNSET, description="Display location for the organization"
    )
    email: Missing[str] = Field(
        default=UNSET, description="Display email for the organization"
    )
    has_organization_projects: bool = Field(
        description="Specifies if organization projects are enabled for this org"
    )
    has_repository_projects: bool = Field(
        description="Specifies if repository projects are enabled for repositories that belong to this org"
    )
    is_verified: Missing[bool] = Field(default=UNSET)
    public_repos: int = Field()
    public_gists: int = Field()
    followers: int = Field()
    following: int = Field()
    type: str = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    plan: Missing[OrganizationPropPlan] = Field(default=UNSET)


class OrganizationPropPlan(GitHubModel):
    """OrganizationPropPlan"""

    name: Missing[str] = Field(default=UNSET)
    space: Missing[int] = Field(default=UNSET)
    private_repos: Missing[int] = Field(default=UNSET)
    filled_seats: Missing[int] = Field(default=UNSET)
    seats: Missing[int] = Field(default=UNSET)


class OrgsOrgCopilotBillingSeatsGetResponse200(GitHubModel):
    """OrgsOrgCopilotBillingSeatsGetResponse200"""

    total_seats: Missing[int] = Field(
        default=UNSET,
        description="Total number of Copilot For Business seats for the organization currently being billed.",
    )
    seats: Missing[List[CopilotSeatDetails]] = Field(default=UNSET)


model_rebuild(CopilotSeatDetails)
model_rebuild(Organization)
model_rebuild(OrganizationPropPlan)
model_rebuild(OrgsOrgCopilotBillingSeatsGetResponse200)

__all__ = (
    "CopilotSeatDetails",
    "Organization",
    "OrganizationPropPlan",
    "OrgsOrgCopilotBillingSeatsGetResponse200",
)
