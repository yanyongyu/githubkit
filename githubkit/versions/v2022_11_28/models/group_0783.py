"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0356 import EnterpriseWebhooks
from .group_0357 import SimpleInstallation
from .group_0360 import SimpleUserWebhooks
from .group_0358 import OrganizationSimpleWebhooks


class WebhookTeamAddedToRepository(GitHubModel):
    """team added_to_repository event"""

    action: Literal["added_to_repository"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: OrganizationSimpleWebhooks = Field(
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: Missing[WebhookTeamAddedToRepositoryPropRepository] = Field(
        default=UNSET, title="Repository", description="A git repository"
    )
    sender: Missing[SimpleUserWebhooks] = Field(
        default=UNSET,
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )
    team: WebhookTeamAddedToRepositoryPropTeam = Field(
        title="Team",
        description="Groups of organization members that gives permissions on specified repositories.",
    )


class WebhookTeamAddedToRepositoryPropRepository(GitHubModel):
    """Repository

    A git repository
    """

    allow_auto_merge: Missing[bool] = Field(
        default=UNSET, description="Whether to allow auto-merge for pull requests."
    )
    allow_forking: Missing[bool] = Field(
        default=UNSET, description="Whether to allow private forks"
    )
    allow_merge_commit: Missing[bool] = Field(
        default=UNSET, description="Whether to allow merge commits for pull requests."
    )
    allow_rebase_merge: Missing[bool] = Field(
        default=UNSET, description="Whether to allow rebase merges for pull requests."
    )
    allow_squash_merge: Missing[bool] = Field(
        default=UNSET, description="Whether to allow squash merges for pull requests."
    )
    allow_update_branch: Missing[bool] = Field(default=UNSET)
    archive_url: str = Field()
    archived: bool = Field(
        default=False, description="Whether the repository is archived."
    )
    assignees_url: str = Field()
    blobs_url: str = Field()
    branches_url: str = Field()
    clone_url: str = Field()
    collaborators_url: str = Field()
    comments_url: str = Field()
    commits_url: str = Field()
    compare_url: str = Field()
    contents_url: str = Field()
    contributors_url: str = Field()
    created_at: Union[int, datetime] = Field()
    custom_properties: Missing[
        WebhookTeamAddedToRepositoryPropRepositoryPropCustomProperties
    ] = Field(
        default=UNSET,
        description="The custom properties that were defined for the repository. The keys are the custom property names, and the values are the corresponding custom property values.",
    )
    default_branch: str = Field(description="The default branch of the repository.")
    delete_branch_on_merge: Missing[bool] = Field(
        default=UNSET,
        description="Whether to delete head branches when pull requests are merged",
    )
    deployments_url: str = Field()
    description: Union[str, None] = Field()
    disabled: Missing[bool] = Field(
        default=UNSET, description="Returns whether or not this repository is disabled."
    )
    downloads_url: str = Field()
    events_url: str = Field()
    fork: bool = Field()
    forks: int = Field()
    forks_count: int = Field()
    forks_url: str = Field()
    full_name: str = Field()
    git_commits_url: str = Field()
    git_refs_url: str = Field()
    git_tags_url: str = Field()
    git_url: str = Field()
    has_downloads: bool = Field(
        default=True, description="Whether downloads are enabled."
    )
    has_issues: bool = Field(default=True, description="Whether issues are enabled.")
    has_pages: bool = Field()
    has_projects: bool = Field(
        default=True, description="Whether projects are enabled."
    )
    has_wiki: bool = Field(default=True, description="Whether the wiki is enabled.")
    homepage: Union[str, None] = Field()
    hooks_url: str = Field()
    html_url: str = Field()
    id: int = Field(description="Unique identifier of the repository")
    is_template: Missing[bool] = Field(default=UNSET)
    issue_comment_url: str = Field()
    issue_events_url: str = Field()
    issues_url: str = Field()
    keys_url: str = Field()
    labels_url: str = Field()
    language: Union[str, None] = Field()
    languages_url: str = Field()
    license_: Union[WebhookTeamAddedToRepositoryPropRepositoryPropLicense, None] = (
        Field(alias="license", title="License")
    )
    master_branch: Missing[str] = Field(default=UNSET)
    merges_url: str = Field()
    milestones_url: str = Field()
    mirror_url: Union[str, None] = Field()
    name: str = Field(description="The name of the repository.")
    node_id: str = Field()
    notifications_url: str = Field()
    open_issues: int = Field()
    open_issues_count: int = Field()
    organization: Missing[str] = Field(default=UNSET)
    owner: Union[WebhookTeamAddedToRepositoryPropRepositoryPropOwner, None] = Field(
        title="User"
    )
    permissions: Missing[WebhookTeamAddedToRepositoryPropRepositoryPropPermissions] = (
        Field(default=UNSET)
    )
    private: bool = Field(description="Whether the repository is private or public.")
    public: Missing[bool] = Field(default=UNSET)
    pulls_url: str = Field()
    pushed_at: Union[int, datetime, None] = Field()
    releases_url: str = Field()
    role_name: Missing[Union[str, None]] = Field(default=UNSET)
    size: int = Field()
    ssh_url: str = Field()
    stargazers: Missing[int] = Field(default=UNSET)
    stargazers_count: int = Field()
    stargazers_url: str = Field()
    statuses_url: str = Field()
    subscribers_url: str = Field()
    subscription_url: str = Field()
    svn_url: str = Field()
    tags_url: str = Field()
    teams_url: str = Field()
    topics: List[str] = Field()
    trees_url: str = Field()
    updated_at: datetime = Field()
    url: str = Field()
    visibility: Literal["public", "private", "internal"] = Field()
    watchers: int = Field()
    watchers_count: int = Field()


class WebhookTeamAddedToRepositoryPropRepositoryPropCustomProperties(ExtraGitHubModel):
    """WebhookTeamAddedToRepositoryPropRepositoryPropCustomProperties

    The custom properties that were defined for the repository. The keys are the
    custom property names, and the values are the corresponding custom property
    values.
    """


class WebhookTeamAddedToRepositoryPropRepositoryPropLicense(GitHubModel):
    """License"""

    key: str = Field()
    name: str = Field()
    node_id: str = Field()
    spdx_id: str = Field()
    url: Union[str, None] = Field()


class WebhookTeamAddedToRepositoryPropRepositoryPropOwner(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookTeamAddedToRepositoryPropRepositoryPropPermissions(GitHubModel):
    """WebhookTeamAddedToRepositoryPropRepositoryPropPermissions"""

    admin: bool = Field()
    maintain: Missing[bool] = Field(default=UNSET)
    pull: bool = Field()
    push: bool = Field()
    triage: Missing[bool] = Field(default=UNSET)


class WebhookTeamAddedToRepositoryPropTeam(GitHubModel):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: Missing[bool] = Field(default=UNSET)
    description: Missing[Union[str, None]] = Field(
        default=UNSET, description="Description of the team"
    )
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field(description="Unique identifier of the team")
    members_url: Missing[str] = Field(default=UNSET)
    name: str = Field(description="Name of the team")
    node_id: Missing[str] = Field(default=UNSET)
    parent: Missing[Union[WebhookTeamAddedToRepositoryPropTeamPropParent, None]] = (
        Field(default=UNSET)
    )
    permission: Missing[str] = Field(
        default=UNSET,
        description="Permission that the team will have for its repositories",
    )
    privacy: Missing[Literal["open", "closed", "secret"]] = Field(default=UNSET)
    notification_setting: Missing[
        Literal["notifications_enabled", "notifications_disabled"]
    ] = Field(
        default=UNSET,
        description="Whether team members will receive notifications when their team is @mentioned",
    )
    repositories_url: Missing[str] = Field(default=UNSET)
    slug: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET, description="URL for the team")


class WebhookTeamAddedToRepositoryPropTeamPropParent(GitHubModel):
    """WebhookTeamAddedToRepositoryPropTeamPropParent"""

    description: Union[str, None] = Field(description="Description of the team")
    html_url: str = Field()
    id: int = Field(description="Unique identifier of the team")
    members_url: str = Field()
    name: str = Field(description="Name of the team")
    node_id: str = Field()
    permission: str = Field(
        description="Permission that the team will have for its repositories"
    )
    privacy: Literal["open", "closed", "secret"] = Field()
    notification_setting: Literal["notifications_enabled", "notifications_disabled"] = (
        Field(
            description="Whether team members will receive notifications when their team is @mentioned"
        )
    )
    repositories_url: str = Field()
    slug: str = Field()
    url: str = Field(description="URL for the team")


model_rebuild(WebhookTeamAddedToRepository)
model_rebuild(WebhookTeamAddedToRepositoryPropRepository)
model_rebuild(WebhookTeamAddedToRepositoryPropRepositoryPropCustomProperties)
model_rebuild(WebhookTeamAddedToRepositoryPropRepositoryPropLicense)
model_rebuild(WebhookTeamAddedToRepositoryPropRepositoryPropOwner)
model_rebuild(WebhookTeamAddedToRepositoryPropRepositoryPropPermissions)
model_rebuild(WebhookTeamAddedToRepositoryPropTeam)
model_rebuild(WebhookTeamAddedToRepositoryPropTeamPropParent)

__all__ = (
    "WebhookTeamAddedToRepository",
    "WebhookTeamAddedToRepositoryPropRepository",
    "WebhookTeamAddedToRepositoryPropRepositoryPropCustomProperties",
    "WebhookTeamAddedToRepositoryPropRepositoryPropLicense",
    "WebhookTeamAddedToRepositoryPropRepositoryPropOwner",
    "WebhookTeamAddedToRepositoryPropRepositoryPropPermissions",
    "WebhookTeamAddedToRepositoryPropTeam",
    "WebhookTeamAddedToRepositoryPropTeamPropParent",
)
