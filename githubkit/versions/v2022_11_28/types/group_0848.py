"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict


class OrgsOrgPatchBodyType(TypedDict):
    """OrgsOrgPatchBody"""

    billing_email: NotRequired[str]
    company: NotRequired[str]
    email: NotRequired[str]
    twitter_username: NotRequired[str]
    location: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    has_organization_projects: NotRequired[bool]
    has_repository_projects: NotRequired[bool]
    default_repository_permission: NotRequired[
        Literal["read", "write", "admin", "none"]
    ]
    members_can_create_repositories: NotRequired[bool]
    members_can_create_internal_repositories: NotRequired[bool]
    members_can_create_private_repositories: NotRequired[bool]
    members_can_create_public_repositories: NotRequired[bool]
    members_allowed_repository_creation_type: NotRequired[
        Literal["all", "private", "none"]
    ]
    members_can_create_pages: NotRequired[bool]
    members_can_create_public_pages: NotRequired[bool]
    members_can_create_private_pages: NotRequired[bool]
    members_can_fork_private_repositories: NotRequired[bool]
    web_commit_signoff_required: NotRequired[bool]
    blog: NotRequired[str]
    advanced_security_enabled_for_new_repositories: NotRequired[bool]
    dependabot_alerts_enabled_for_new_repositories: NotRequired[bool]
    dependabot_security_updates_enabled_for_new_repositories: NotRequired[bool]
    dependency_graph_enabled_for_new_repositories: NotRequired[bool]
    secret_scanning_enabled_for_new_repositories: NotRequired[bool]
    secret_scanning_push_protection_enabled_for_new_repositories: NotRequired[bool]
    secret_scanning_push_protection_custom_link_enabled: NotRequired[bool]
    secret_scanning_push_protection_custom_link: NotRequired[str]
    deploy_keys_enabled_for_repositories: NotRequired[bool]


__all__ = ("OrgsOrgPatchBodyType",)
