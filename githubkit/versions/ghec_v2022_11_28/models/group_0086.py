"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class OrganizationFull(GitHubModel):
    """Organization Full

    Organization Full
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
    type: str = Field()
    total_private_repos: Missing[int] = Field(default=UNSET)
    owned_private_repos: Missing[int] = Field(default=UNSET)
    private_gists: Missing[Union[int, None]] = Field(default=UNSET)
    disk_usage: Missing[Union[int, None]] = Field(default=UNSET)
    collaborators: Missing[Union[int, None]] = Field(default=UNSET)
    billing_email: Missing[Union[str, None]] = Field(default=UNSET)
    plan: Missing[OrganizationFullPropPlan] = Field(default=UNSET)
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
    advanced_security_enabled_for_new_repositories: Missing[bool] = Field(
        default=UNSET,
        description="**Deprecated.** Please use [code security configurations](https://docs.github.com/enterprise-cloud@latest//rest/code-security/configurations) instead.\n\nWhether GitHub Advanced Security is enabled for new repositories and repositories transferred to this organization.\n\nThis field is only visible to organization owners or members of a team with the security manager role.",
    )
    dependabot_alerts_enabled_for_new_repositories: Missing[bool] = Field(
        default=UNSET,
        description="**Deprecated.** Please use [code security configurations](https://docs.github.com/enterprise-cloud@latest//rest/code-security/configurations) instead.\n\nWhether Dependabot alerts are automatically enabled for new repositories and repositories transferred to this organization.\n\nThis field is only visible to organization owners or members of a team with the security manager role.",
    )
    dependabot_security_updates_enabled_for_new_repositories: Missing[bool] = Field(
        default=UNSET,
        description="**Deprecated.** Please use [code security configurations](https://docs.github.com/enterprise-cloud@latest//rest/code-security/configurations) instead.\n\nWhether Dependabot security updates are automatically enabled for new repositories and repositories transferred to this organization.\n\nThis field is only visible to organization owners or members of a team with the security manager role.",
    )
    dependency_graph_enabled_for_new_repositories: Missing[bool] = Field(
        default=UNSET,
        description="**Deprecated.** Please use [code security configurations](https://docs.github.com/enterprise-cloud@latest//rest/code-security/configurations) instead.\n\nWhether dependency graph is automatically enabled for new repositories and repositories transferred to this organization.\n\nThis field is only visible to organization owners or members of a team with the security manager role.",
    )
    secret_scanning_enabled_for_new_repositories: Missing[bool] = Field(
        default=UNSET,
        description="**Deprecated.** Please use [code security configurations](https://docs.github.com/enterprise-cloud@latest//rest/code-security/configurations) instead.\n\nWhether secret scanning is automatically enabled for new repositories and repositories transferred to this organization.\n\nThis field is only visible to organization owners or members of a team with the security manager role.",
    )
    secret_scanning_push_protection_enabled_for_new_repositories: Missing[bool] = Field(
        default=UNSET,
        description="**Deprecated.** Please use [code security configurations](https://docs.github.com/enterprise-cloud@latest//rest/code-security/configurations) instead.\n\nWhether secret scanning push protection is automatically enabled for new repositories and repositories transferred to this organization.\n\nThis field is only visible to organization owners or members of a team with the security manager role.",
    )
    secret_scanning_push_protection_custom_link_enabled: Missing[bool] = Field(
        default=UNSET,
        description="Whether a custom link is shown to contributors who are blocked from pushing a secret by push protection.",
    )
    secret_scanning_push_protection_custom_link: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="An optional URL string to display to contributors who are blocked from pushing a secret.",
    )
    secret_scanning_validity_checks_enabled: Missing[bool] = Field(
        default=UNSET,
        description="**Deprecated.** Please use [code security configurations](https://docs.github.com/enterprise-cloud@latest//rest/code-security/configurations) instead.\n\nWhether secret scanning automatic validity checks on supported partner tokens is enabled for all repositories under this organization.",
    )
    created_at: datetime = Field()
    updated_at: datetime = Field()
    archived_at: Union[datetime, None] = Field()


class OrganizationFullPropPlan(GitHubModel):
    """OrganizationFullPropPlan"""

    name: str = Field()
    space: int = Field()
    private_repos: int = Field()
    filled_seats: Missing[int] = Field(default=UNSET)
    seats: Missing[int] = Field(default=UNSET)


model_rebuild(OrganizationFull)
model_rebuild(OrganizationFullPropPlan)

__all__ = (
    "OrganizationFull",
    "OrganizationFullPropPlan",
)
