"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal, Union
from typing_extensions import NotRequired, TypeAlias, TypedDict

from .group_0003 import SimpleUserType
from .group_0473 import EnterpriseWebhooksType
from .group_0474 import SimpleInstallationType
from .group_0475 import OrganizationSimpleWebhooksType
from .group_0476 import RepositoryWebhooksType
from .group_0672 import WebhookIssuesOpenedPropIssueType


class WebhookIssuesOpenedType(TypedDict):
    """issues opened event"""

    action: Literal["opened"]
    changes: NotRequired[WebhookIssuesOpenedPropChangesType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    issue: WebhookIssuesOpenedPropIssueType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookIssuesOpenedPropChangesType(TypedDict):
    """WebhookIssuesOpenedPropChanges"""

    old_issue: Union[WebhookIssuesOpenedPropChangesPropOldIssueType, None]
    old_repository: WebhookIssuesOpenedPropChangesPropOldRepositoryType


class WebhookIssuesOpenedPropChangesPropOldIssueType(TypedDict):
    """Issue

    The [issue](https://docs.github.com/enterprise-
    cloud@latest//rest/issues/issues#get-an-issue) itself.
    """

    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ]
    assignee: NotRequired[
        Union[WebhookIssuesOpenedPropChangesPropOldIssuePropAssigneeType, None]
    ]
    assignees: list[
        Union[WebhookIssuesOpenedPropChangesPropOldIssuePropAssigneesItemsType, None]
    ]
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]
    body: Union[str, None]
    closed_at: Union[datetime, None]
    comments: int
    comments_url: str
    created_at: datetime
    draft: NotRequired[bool]
    events_url: str
    html_url: str
    id: int
    labels: NotRequired[
        list[WebhookIssuesOpenedPropChangesPropOldIssuePropLabelsItemsType]
    ]
    labels_url: str
    locked: NotRequired[bool]
    milestone: Union[WebhookIssuesOpenedPropChangesPropOldIssuePropMilestoneType, None]
    node_id: str
    number: int
    performed_via_github_app: NotRequired[
        Union[
            WebhookIssuesOpenedPropChangesPropOldIssuePropPerformedViaGithubAppType,
            None,
        ]
    ]
    pull_request: NotRequired[
        WebhookIssuesOpenedPropChangesPropOldIssuePropPullRequestType
    ]
    reactions: WebhookIssuesOpenedPropChangesPropOldIssuePropReactionsType
    repository_url: str
    sub_issues_summary: NotRequired[
        WebhookIssuesOpenedPropChangesPropOldIssuePropSubIssuesSummaryType
    ]
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[Union[str, None]]
    timeline_url: NotRequired[str]
    title: str
    updated_at: datetime
    url: str
    user: Union[WebhookIssuesOpenedPropChangesPropOldIssuePropUserType, None]


class WebhookIssuesOpenedPropChangesPropOldIssuePropAssigneeType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhookIssuesOpenedPropChangesPropOldIssuePropAssigneesItemsType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhookIssuesOpenedPropChangesPropOldIssuePropLabelsItemsType(TypedDict):
    """Label"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookIssuesOpenedPropChangesPropOldIssuePropMilestoneType(TypedDict):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None]
    closed_issues: int
    created_at: datetime
    creator: Union[
        WebhookIssuesOpenedPropChangesPropOldIssuePropMilestonePropCreatorType, None
    ]
    description: Union[str, None]
    due_on: Union[datetime, None]
    html_url: str
    id: int
    labels_url: str
    node_id: str
    number: int
    open_issues: int
    state: Literal["open", "closed"]
    title: str
    updated_at: datetime
    url: str


class WebhookIssuesOpenedPropChangesPropOldIssuePropMilestonePropCreatorType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhookIssuesOpenedPropChangesPropOldIssuePropPerformedViaGithubAppType(
    TypedDict
):
    """App

    GitHub apps are a new way to extend GitHub. They can be installed directly on
    organizations and user accounts and granted access to specific repositories.
    They come with granular permissions and built-in webhooks. GitHub apps are first
    class actors within GitHub.
    """

    created_at: Union[datetime, None]
    description: Union[str, None]
    events: NotRequired[list[str]]
    external_url: Union[str, None]
    html_url: str
    id: Union[int, None]
    name: str
    node_id: str
    owner: Union[
        WebhookIssuesOpenedPropChangesPropOldIssuePropPerformedViaGithubAppPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookIssuesOpenedPropChangesPropOldIssuePropPerformedViaGithubAppPropPermissionsType
    ]
    slug: NotRequired[str]
    updated_at: Union[datetime, None]


class WebhookIssuesOpenedPropChangesPropOldIssuePropPerformedViaGithubAppPropOwnerType(
    TypedDict
):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhookIssuesOpenedPropChangesPropOldIssuePropPerformedViaGithubAppPropPermissionsType(
    TypedDict
):
    """WebhookIssuesOpenedPropChangesPropOldIssuePropPerformedViaGithubAppPropPermissio
    ns

    The set of permissions for the GitHub app
    """

    actions: NotRequired[Literal["read", "write"]]
    administration: NotRequired[Literal["read", "write"]]
    checks: NotRequired[Literal["read", "write"]]
    content_references: NotRequired[Literal["read", "write"]]
    contents: NotRequired[Literal["read", "write"]]
    deployments: NotRequired[Literal["read", "write"]]
    discussions: NotRequired[Literal["read", "write"]]
    emails: NotRequired[Literal["read", "write"]]
    environments: NotRequired[Literal["read", "write"]]
    issues: NotRequired[Literal["read", "write"]]
    keys: NotRequired[Literal["read", "write"]]
    members: NotRequired[Literal["read", "write"]]
    metadata: NotRequired[Literal["read", "write"]]
    organization_administration: NotRequired[Literal["read", "write"]]
    organization_hooks: NotRequired[Literal["read", "write"]]
    organization_packages: NotRequired[Literal["read", "write"]]
    organization_plan: NotRequired[Literal["read", "write"]]
    organization_projects: NotRequired[Literal["read", "write"]]
    organization_secrets: NotRequired[Literal["read", "write"]]
    organization_self_hosted_runners: NotRequired[Literal["read", "write"]]
    organization_user_blocking: NotRequired[Literal["read", "write"]]
    packages: NotRequired[Literal["read", "write"]]
    pages: NotRequired[Literal["read", "write"]]
    pull_requests: NotRequired[Literal["read", "write"]]
    repository_hooks: NotRequired[Literal["read", "write"]]
    repository_projects: NotRequired[Literal["read", "write"]]
    secret_scanning_alerts: NotRequired[Literal["read", "write"]]
    secrets: NotRequired[Literal["read", "write"]]
    security_events: NotRequired[Literal["read", "write"]]
    security_scanning_alert: NotRequired[Literal["read", "write"]]
    single_file: NotRequired[Literal["read", "write"]]
    statuses: NotRequired[Literal["read", "write"]]
    team_discussions: NotRequired[Literal["read", "write"]]
    vulnerability_alerts: NotRequired[Literal["read", "write"]]
    workflows: NotRequired[Literal["read", "write"]]


class WebhookIssuesOpenedPropChangesPropOldIssuePropPullRequestType(TypedDict):
    """WebhookIssuesOpenedPropChangesPropOldIssuePropPullRequest"""

    diff_url: NotRequired[str]
    html_url: NotRequired[str]
    merged_at: NotRequired[Union[datetime, None]]
    patch_url: NotRequired[str]
    url: NotRequired[str]


class WebhookIssuesOpenedPropChangesPropOldIssuePropReactionsType(TypedDict):
    """Reactions"""

    plus_one: int
    minus_one: int
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhookIssuesOpenedPropChangesPropOldIssuePropSubIssuesSummaryType(TypedDict):
    """Sub-issues Summary"""

    total: int
    completed: int
    percent_completed: int


class WebhookIssuesOpenedPropChangesPropOldIssuePropUserType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhookIssuesOpenedPropChangesPropOldRepositoryType(TypedDict):
    """Repository

    A git repository
    """

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: Union[int, datetime]
    custom_properties: NotRequired[
        WebhookIssuesOpenedPropChangesPropOldRepositoryPropCustomPropertiesType
    ]
    default_branch: str
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: str
    description: Union[str, None]
    disabled: NotRequired[bool]
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_discussions: NotRequired[bool]
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    homepage: Union[str, None]
    hooks_url: str
    html_url: str
    id: int
    is_template: NotRequired[bool]
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: Union[str, None]
    languages_url: str
    license_: Union[
        WebhookIssuesOpenedPropChangesPropOldRepositoryPropLicenseType, None
    ]
    master_branch: NotRequired[str]
    merges_url: str
    milestones_url: str
    mirror_url: Union[str, None]
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: NotRequired[str]
    owner: Union[WebhookIssuesOpenedPropChangesPropOldRepositoryPropOwnerType, None]
    permissions: NotRequired[
        WebhookIssuesOpenedPropChangesPropOldRepositoryPropPermissionsType
    ]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
    ssh_url: str
    stargazers: NotRequired[int]
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: datetime
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: NotRequired[bool]


WebhookIssuesOpenedPropChangesPropOldRepositoryPropCustomPropertiesType: TypeAlias = (
    dict[str, Any]
)
"""WebhookIssuesOpenedPropChangesPropOldRepositoryPropCustomProperties

The custom properties that were defined for the repository. The keys are the
custom property names, and the values are the corresponding custom property
values.
"""


class WebhookIssuesOpenedPropChangesPropOldRepositoryPropLicenseType(TypedDict):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookIssuesOpenedPropChangesPropOldRepositoryPropOwnerType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhookIssuesOpenedPropChangesPropOldRepositoryPropPermissionsType(TypedDict):
    """WebhookIssuesOpenedPropChangesPropOldRepositoryPropPermissions"""

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


__all__ = (
    "WebhookIssuesOpenedPropChangesPropOldIssuePropAssigneeType",
    "WebhookIssuesOpenedPropChangesPropOldIssuePropAssigneesItemsType",
    "WebhookIssuesOpenedPropChangesPropOldIssuePropLabelsItemsType",
    "WebhookIssuesOpenedPropChangesPropOldIssuePropMilestonePropCreatorType",
    "WebhookIssuesOpenedPropChangesPropOldIssuePropMilestoneType",
    "WebhookIssuesOpenedPropChangesPropOldIssuePropPerformedViaGithubAppPropOwnerType",
    "WebhookIssuesOpenedPropChangesPropOldIssuePropPerformedViaGithubAppPropPermissionsType",
    "WebhookIssuesOpenedPropChangesPropOldIssuePropPerformedViaGithubAppType",
    "WebhookIssuesOpenedPropChangesPropOldIssuePropPullRequestType",
    "WebhookIssuesOpenedPropChangesPropOldIssuePropReactionsType",
    "WebhookIssuesOpenedPropChangesPropOldIssuePropSubIssuesSummaryType",
    "WebhookIssuesOpenedPropChangesPropOldIssuePropUserType",
    "WebhookIssuesOpenedPropChangesPropOldIssueType",
    "WebhookIssuesOpenedPropChangesPropOldRepositoryPropCustomPropertiesType",
    "WebhookIssuesOpenedPropChangesPropOldRepositoryPropLicenseType",
    "WebhookIssuesOpenedPropChangesPropOldRepositoryPropOwnerType",
    "WebhookIssuesOpenedPropChangesPropOldRepositoryPropPermissionsType",
    "WebhookIssuesOpenedPropChangesPropOldRepositoryType",
    "WebhookIssuesOpenedPropChangesType",
    "WebhookIssuesOpenedType",
)
