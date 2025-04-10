"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class WebhooksRule(GitHubModel):
    """branch protection rule

    The branch protection rule. Includes a `name` and all the [branch protection
    settings](https://docs.github.com/github/administering-a-repository/defining-
    the-mergeability-of-pull-requests/about-protected-branches#about-branch-
    protection-settings) applied to branches that match the name. Binary settings
    are boolean. Multi-level configurations are one of `off`, `non_admins`, or
    `everyone`. Actor and build lists are arrays of strings.
    """

    admin_enforced: bool = Field()
    allow_deletions_enforcement_level: Literal["off", "non_admins", "everyone"] = (
        Field()
    )
    allow_force_pushes_enforcement_level: Literal["off", "non_admins", "everyone"] = (
        Field()
    )
    authorized_actor_names: list[str] = Field()
    authorized_actors_only: bool = Field()
    authorized_dismissal_actors_only: bool = Field()
    create_protected: Missing[bool] = Field(default=UNSET)
    created_at: datetime = Field()
    dismiss_stale_reviews_on_push: bool = Field()
    id: int = Field()
    ignore_approvals_from_contributors: bool = Field()
    linear_history_requirement_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    lock_branch_enforcement_level: Literal["off", "non_admins", "everyone"] = Field(
        description="The enforcement level of the branch lock setting. `off` means the branch is not locked, `non_admins` means the branch is read-only for non_admins, and `everyone` means the branch is read-only for everyone."
    )
    lock_allows_fork_sync: Missing[bool] = Field(
        default=UNSET,
        description="Whether users can pull changes from upstream when the branch is locked. Set to `true` to allow users to pull changes from upstream when the branch is locked. This setting is only applicable for forks.",
    )
    merge_queue_enforcement_level: Literal["off", "non_admins", "everyone"] = Field()
    name: str = Field()
    pull_request_reviews_enforcement_level: Literal["off", "non_admins", "everyone"] = (
        Field()
    )
    repository_id: int = Field()
    require_code_owner_review: bool = Field()
    require_last_push_approval: Missing[bool] = Field(
        default=UNSET,
        description="Whether the most recent push must be approved by someone other than the person who pushed it",
    )
    required_approving_review_count: int = Field()
    required_conversation_resolution_level: Literal["off", "non_admins", "everyone"] = (
        Field()
    )
    required_deployments_enforcement_level: Literal["off", "non_admins", "everyone"] = (
        Field()
    )
    required_status_checks: list[str] = Field()
    required_status_checks_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    signature_requirement_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    strict_required_status_checks_policy: bool = Field()
    updated_at: datetime = Field()


model_rebuild(WebhooksRule)

__all__ = ("WebhooksRule",)
