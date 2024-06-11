"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0092 import TeamSimple


class TeamFull(GitHubModel):
    """Full Team

    Groups of organization members that gives permissions on specified repositories.
    """

    id: int = Field(description="Unique identifier of the team")
    node_id: str = Field()
    url: str = Field(description="URL for the team")
    html_url: str = Field()
    name: str = Field(description="Name of the team")
    slug: str = Field()
    description: Union[str, None] = Field()
    privacy: Missing[Literal["closed", "secret"]] = Field(
        default=UNSET, description="The level of privacy this team should have"
    )
    notification_setting: Missing[
        Literal["notifications_enabled", "notifications_disabled"]
    ] = Field(default=UNSET, description="The notification setting the team has set")
    permission: str = Field(
        description="Permission that the team will have for its repositories"
    )
    members_url: str = Field()
    repositories_url: str = Field()
    parent: Missing[Union[None, TeamSimple]] = Field(default=UNSET)
    members_count: int = Field()
    repos_count: int = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    organization: TeamOrganization = Field(
        title="Team Organization", description="Team Organization"
    )
    ldap_dn: Missing[str] = Field(
        default=UNSET,
        description="Distinguished Name (DN) that team maps to within LDAP environment",
    )


class TeamOrganization(GitHubModel):
    """Team Organization

    Team Organization
    """

    login: str = Field()
    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    repos_url: str = Field()
    events_url: str = Field()
    hooks_url: str = Field()
    issues_url: str = Field()
    members_url: str = Field()
    public_members_url: str = Field()
    avatar_url: str = Field()
    description: Union[str, None] = Field()
    name: Missing[Union[str, None]] = Field(default=UNSET)
    company: Missing[Union[str, None]] = Field(default=UNSET)
    blog: Missing[Union[str, None]] = Field(default=UNSET)
    location: Missing[Union[str, None]] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    twitter_username: Missing[Union[str, None]] = Field(default=UNSET)
    is_verified: Missing[bool] = Field(default=UNSET)
    has_organization_projects: bool = Field()
    has_repository_projects: bool = Field()
    public_repos: int = Field()
    public_gists: int = Field()
    followers: int = Field()
    following: int = Field()
    html_url: str = Field()
    created_at: datetime = Field()
    type: str = Field()
    total_private_repos: Missing[int] = Field(default=UNSET)
    owned_private_repos: Missing[int] = Field(default=UNSET)
    private_gists: Missing[Union[int, None]] = Field(default=UNSET)
    disk_usage: Missing[Union[int, None]] = Field(default=UNSET)
    collaborators: Missing[Union[int, None]] = Field(default=UNSET)
    billing_email: Missing[Union[str, None]] = Field(default=UNSET)
    plan: Missing[TeamOrganizationPropPlan] = Field(default=UNSET)
    default_repository_permission: Missing[Union[str, None]] = Field(default=UNSET)
    members_can_create_repositories: Missing[Union[bool, None]] = Field(default=UNSET)
    two_factor_requirement_enabled: Missing[Union[bool, None]] = Field(default=UNSET)
    members_allowed_repository_creation_type: Missing[str] = Field(default=UNSET)
    members_can_create_public_repositories: Missing[bool] = Field(default=UNSET)
    members_can_create_private_repositories: Missing[bool] = Field(default=UNSET)
    members_can_create_internal_repositories: Missing[bool] = Field(default=UNSET)
    members_can_create_pages: Missing[bool] = Field(default=UNSET)
    members_can_create_public_pages: Missing[bool] = Field(default=UNSET)
    members_can_create_private_pages: Missing[bool] = Field(default=UNSET)
    members_can_fork_private_repositories: Missing[Union[bool, None]] = Field(
        default=UNSET
    )
    web_commit_signoff_required: Missing[bool] = Field(default=UNSET)
    updated_at: datetime = Field()
    archived_at: Union[datetime, None] = Field()


class TeamOrganizationPropPlan(GitHubModel):
    """TeamOrganizationPropPlan"""

    name: str = Field()
    space: int = Field()
    private_repos: int = Field()
    filled_seats: Missing[int] = Field(default=UNSET)
    seats: Missing[int] = Field(default=UNSET)


model_rebuild(TeamFull)
model_rebuild(TeamOrganization)
model_rebuild(TeamOrganizationPropPlan)

__all__ = (
    "TeamFull",
    "TeamOrganization",
    "TeamOrganizationPropPlan",
)
