"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict, NotRequired


class OrganizationFullType(TypedDict):
    """Organization Full

    Prevents users in the organization from using insecure methods of two-factor
    authentication to fulfill a two-factor requirement.
    Removes non-compliant outside collaborators from the organization and its
    repositories.

    GitHub currently defines SMS as an insecure method of two-factor authentication.

    If your users are managed by the enterprise this policy will not affect them.
    The first admin account of the enterprise will still be affected.
    """

    login: str
    id: int
    node_id: str
    url: str
    repos_url: str
    events_url: str
    hooks_url: str
    issues_url: str
    members_url: str
    public_members_url: str
    avatar_url: str
    description: Union[str, None]
    name: NotRequired[Union[str, None]]
    company: NotRequired[Union[str, None]]
    blog: NotRequired[Union[str, None]]
    location: NotRequired[Union[str, None]]
    email: NotRequired[Union[str, None]]
    twitter_username: NotRequired[Union[str, None]]
    is_verified: NotRequired[bool]
    has_organization_projects: bool
    has_repository_projects: bool
    public_repos: int
    public_gists: int
    followers: int
    following: int
    html_url: str
    type: str
    total_private_repos: NotRequired[int]
    owned_private_repos: NotRequired[int]
    private_gists: NotRequired[Union[int, None]]
    disk_usage: NotRequired[Union[int, None]]
    collaborators: NotRequired[Union[int, None]]
    billing_email: NotRequired[Union[str, None]]
    plan: NotRequired[OrganizationFullPropPlanType]
    default_repository_permission: NotRequired[Union[str, None]]
    members_can_create_repositories: NotRequired[Union[bool, None]]
    two_factor_requirement_enabled: NotRequired[Union[bool, None]]
    members_allowed_repository_creation_type: NotRequired[str]
    members_can_create_public_repositories: NotRequired[bool]
    members_can_create_private_repositories: NotRequired[bool]
    members_can_create_internal_repositories: NotRequired[bool]
    members_can_create_pages: NotRequired[bool]
    members_can_create_public_pages: NotRequired[bool]
    members_can_create_private_pages: NotRequired[bool]
    members_can_fork_private_repositories: NotRequired[Union[bool, None]]
    web_commit_signoff_required: NotRequired[bool]
    advanced_security_enabled_for_new_repositories: NotRequired[bool]
    dependabot_alerts_enabled_for_new_repositories: NotRequired[bool]
    dependabot_security_updates_enabled_for_new_repositories: NotRequired[bool]
    dependency_graph_enabled_for_new_repositories: NotRequired[bool]
    secret_scanning_enabled_for_new_repositories: NotRequired[bool]
    secret_scanning_push_protection_enabled_for_new_repositories: NotRequired[bool]
    secret_scanning_push_protection_custom_link_enabled: NotRequired[bool]
    secret_scanning_push_protection_custom_link: NotRequired[Union[str, None]]
    secret_scanning_validity_checks_enabled: NotRequired[bool]
    created_at: datetime
    updated_at: datetime
    archived_at: Union[datetime, None]
    deploy_keys_enabled_for_repositories: NotRequired[bool]


class OrganizationFullPropPlanType(TypedDict):
    """OrganizationFullPropPlan"""

    name: str
    space: int
    private_repos: int
    filled_seats: NotRequired[int]
    seats: NotRequired[int]


__all__ = (
    "OrganizationFullType",
    "OrganizationFullPropPlanType",
)
