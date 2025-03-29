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
from .group_0471 import EnterpriseWebhooksType
from .group_0472 import SimpleInstallationType
from .group_0473 import OrganizationSimpleWebhooksType
from .group_0474 import RepositoryWebhooksType
from .group_0481 import WebhooksWorkflowType


class WebhookDeploymentStatusCreatedType(TypedDict):
    """deployment_status created event"""

    action: Literal["created"]
    check_run: NotRequired[Union[WebhookDeploymentStatusCreatedPropCheckRunType, None]]
    deployment: WebhookDeploymentStatusCreatedPropDeploymentType
    deployment_status: WebhookDeploymentStatusCreatedPropDeploymentStatusType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType
    workflow: NotRequired[Union[WebhooksWorkflowType, None]]
    workflow_run: NotRequired[
        Union[WebhookDeploymentStatusCreatedPropWorkflowRunType, None]
    ]


class WebhookDeploymentStatusCreatedPropCheckRunType(TypedDict):
    """WebhookDeploymentStatusCreatedPropCheckRun"""

    completed_at: Union[datetime, None]
    conclusion: Union[
        None,
        Literal[
            "success",
            "failure",
            "neutral",
            "cancelled",
            "timed_out",
            "action_required",
            "stale",
            "skipped",
        ],
    ]
    details_url: str
    external_id: str
    head_sha: str
    html_url: str
    id: int
    name: str
    node_id: str
    started_at: datetime
    status: Literal["queued", "in_progress", "completed", "waiting", "pending"]
    url: str


class WebhookDeploymentStatusCreatedPropDeploymentType(TypedDict):
    """Deployment

    The [deployment](https://docs.github.com/enterprise-
    cloud@latest//rest/deployments/deployments#list-deployments).
    """

    created_at: str
    creator: Union[WebhookDeploymentStatusCreatedPropDeploymentPropCreatorType, None]
    description: Union[str, None]
    environment: str
    id: int
    node_id: str
    original_environment: str
    payload: Union[
        str, WebhookDeploymentStatusCreatedPropDeploymentPropPayloadOneof1Type, None
    ]
    performed_via_github_app: NotRequired[
        Union[
            WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppType,
            None,
        ]
    ]
    production_environment: NotRequired[bool]
    ref: str
    repository_url: str
    sha: str
    statuses_url: str
    task: str
    transient_environment: NotRequired[bool]
    updated_at: str
    url: str


class WebhookDeploymentStatusCreatedPropDeploymentPropCreatorType(TypedDict):
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


WebhookDeploymentStatusCreatedPropDeploymentPropPayloadOneof1Type: TypeAlias = dict[
    str, Any
]
"""WebhookDeploymentStatusCreatedPropDeploymentPropPayloadOneof1
"""


class WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppType(
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
        WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppPropPermissionsType
    ]
    slug: NotRequired[str]
    updated_at: Union[datetime, None]


class WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppPropOwnerType(
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


class WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppPropPermissionsType(
    TypedDict
):
    """WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppPropPermiss
    ions

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


class WebhookDeploymentStatusCreatedPropDeploymentStatusType(TypedDict):
    """WebhookDeploymentStatusCreatedPropDeploymentStatus

    The [deployment status](https://docs.github.com/enterprise-
    cloud@latest//rest/deployments/statuses#list-deployment-statuses).
    """

    created_at: str
    creator: Union[
        WebhookDeploymentStatusCreatedPropDeploymentStatusPropCreatorType, None
    ]
    deployment_url: str
    description: str
    environment: str
    environment_url: NotRequired[str]
    id: int
    log_url: NotRequired[str]
    node_id: str
    performed_via_github_app: NotRequired[
        Union[
            WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppType,
            None,
        ]
    ]
    repository_url: str
    state: str
    target_url: str
    updated_at: str
    url: str


class WebhookDeploymentStatusCreatedPropDeploymentStatusPropCreatorType(TypedDict):
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


class WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppType(
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
        WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppPropPermissionsType
    ]
    slug: NotRequired[str]
    updated_at: Union[datetime, None]


class WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppPropOwnerType(
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


class WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppPropPermissionsType(
    TypedDict
):
    """WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppPropP
    ermissions

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


class WebhookDeploymentStatusCreatedPropWorkflowRunType(TypedDict):
    """Deployment Workflow Run"""

    actor: Union[WebhookDeploymentStatusCreatedPropWorkflowRunPropActorType, None]
    artifacts_url: NotRequired[str]
    cancel_url: NotRequired[str]
    check_suite_id: int
    check_suite_node_id: str
    check_suite_url: NotRequired[str]
    conclusion: Union[
        None,
        Literal[
            "success",
            "failure",
            "neutral",
            "cancelled",
            "timed_out",
            "action_required",
            "stale",
            "startup_failure",
        ],
    ]
    created_at: datetime
    display_title: str
    event: str
    head_branch: str
    head_commit: NotRequired[None]
    head_repository: NotRequired[
        WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepositoryType
    ]
    head_sha: str
    html_url: str
    id: int
    jobs_url: NotRequired[str]
    logs_url: NotRequired[str]
    name: str
    node_id: str
    path: str
    previous_attempt_url: NotRequired[None]
    pull_requests: list[
        WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsType
    ]
    referenced_workflows: NotRequired[
        Union[
            list[
                WebhookDeploymentStatusCreatedPropWorkflowRunPropReferencedWorkflowsItemsType
            ],
            None,
        ]
    ]
    repository: NotRequired[
        WebhookDeploymentStatusCreatedPropWorkflowRunPropRepositoryType
    ]
    rerun_url: NotRequired[str]
    run_attempt: int
    run_number: int
    run_started_at: datetime
    status: Literal[
        "requested", "in_progress", "completed", "queued", "waiting", "pending"
    ]
    triggering_actor: Union[
        WebhookDeploymentStatusCreatedPropWorkflowRunPropTriggeringActorType, None
    ]
    updated_at: datetime
    url: str
    workflow_id: int
    workflow_url: NotRequired[str]


class WebhookDeploymentStatusCreatedPropWorkflowRunPropActorType(TypedDict):
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


class WebhookDeploymentStatusCreatedPropWorkflowRunPropReferencedWorkflowsItemsType(
    TypedDict
):
    """WebhookDeploymentStatusCreatedPropWorkflowRunPropReferencedWorkflowsItems"""

    path: str
    ref: NotRequired[str]
    sha: str


class WebhookDeploymentStatusCreatedPropWorkflowRunPropTriggeringActorType(TypedDict):
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


class WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepositoryType(TypedDict):
    """WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepository"""

    archive_url: NotRequired[str]
    assignees_url: NotRequired[str]
    blobs_url: NotRequired[str]
    branches_url: NotRequired[str]
    collaborators_url: NotRequired[str]
    comments_url: NotRequired[str]
    commits_url: NotRequired[str]
    compare_url: NotRequired[str]
    contents_url: NotRequired[str]
    contributors_url: NotRequired[str]
    deployments_url: NotRequired[str]
    description: NotRequired[None]
    downloads_url: NotRequired[str]
    events_url: NotRequired[str]
    fork: NotRequired[bool]
    forks_url: NotRequired[str]
    full_name: NotRequired[str]
    git_commits_url: NotRequired[str]
    git_refs_url: NotRequired[str]
    git_tags_url: NotRequired[str]
    hooks_url: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    issue_comment_url: NotRequired[str]
    issue_events_url: NotRequired[str]
    issues_url: NotRequired[str]
    keys_url: NotRequired[str]
    labels_url: NotRequired[str]
    languages_url: NotRequired[str]
    merges_url: NotRequired[str]
    milestones_url: NotRequired[str]
    name: NotRequired[str]
    node_id: NotRequired[str]
    notifications_url: NotRequired[str]
    owner: NotRequired[
        WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepositoryPropOwnerType
    ]
    private: NotRequired[bool]
    pulls_url: NotRequired[str]
    releases_url: NotRequired[str]
    stargazers_url: NotRequired[str]
    statuses_url: NotRequired[str]
    subscribers_url: NotRequired[str]
    subscription_url: NotRequired[str]
    tags_url: NotRequired[str]
    teams_url: NotRequired[str]
    trees_url: NotRequired[str]
    url: NotRequired[str]


class WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepositoryPropOwnerType(
    TypedDict
):
    """WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepositoryPropOwner"""

    avatar_url: NotRequired[str]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]


class WebhookDeploymentStatusCreatedPropWorkflowRunPropRepositoryType(TypedDict):
    """WebhookDeploymentStatusCreatedPropWorkflowRunPropRepository"""

    archive_url: NotRequired[str]
    assignees_url: NotRequired[str]
    blobs_url: NotRequired[str]
    branches_url: NotRequired[str]
    collaborators_url: NotRequired[str]
    comments_url: NotRequired[str]
    commits_url: NotRequired[str]
    compare_url: NotRequired[str]
    contents_url: NotRequired[str]
    contributors_url: NotRequired[str]
    deployments_url: NotRequired[str]
    description: NotRequired[None]
    downloads_url: NotRequired[str]
    events_url: NotRequired[str]
    fork: NotRequired[bool]
    forks_url: NotRequired[str]
    full_name: NotRequired[str]
    git_commits_url: NotRequired[str]
    git_refs_url: NotRequired[str]
    git_tags_url: NotRequired[str]
    hooks_url: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    issue_comment_url: NotRequired[str]
    issue_events_url: NotRequired[str]
    issues_url: NotRequired[str]
    keys_url: NotRequired[str]
    labels_url: NotRequired[str]
    languages_url: NotRequired[str]
    merges_url: NotRequired[str]
    milestones_url: NotRequired[str]
    name: NotRequired[str]
    node_id: NotRequired[str]
    notifications_url: NotRequired[str]
    owner: NotRequired[
        WebhookDeploymentStatusCreatedPropWorkflowRunPropRepositoryPropOwnerType
    ]
    private: NotRequired[bool]
    pulls_url: NotRequired[str]
    releases_url: NotRequired[str]
    stargazers_url: NotRequired[str]
    statuses_url: NotRequired[str]
    subscribers_url: NotRequired[str]
    subscription_url: NotRequired[str]
    tags_url: NotRequired[str]
    teams_url: NotRequired[str]
    trees_url: NotRequired[str]
    url: NotRequired[str]


class WebhookDeploymentStatusCreatedPropWorkflowRunPropRepositoryPropOwnerType(
    TypedDict
):
    """WebhookDeploymentStatusCreatedPropWorkflowRunPropRepositoryPropOwner"""

    avatar_url: NotRequired[str]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]


class WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsType(TypedDict):
    """Check Run Pull Request"""

    base: WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropBaseType
    head: WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropHeadType
    id: int
    number: int
    url: str


class WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropBaseType(
    TypedDict
):
    """WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropBase"""

    ref: str
    repo: WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType
    sha: str


class WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


class WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropHeadType(
    TypedDict
):
    """WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropHead"""

    ref: str
    repo: WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType
    sha: str


class WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


__all__ = (
    "WebhookDeploymentStatusCreatedPropCheckRunType",
    "WebhookDeploymentStatusCreatedPropDeploymentPropCreatorType",
    "WebhookDeploymentStatusCreatedPropDeploymentPropPayloadOneof1Type",
    "WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppPropOwnerType",
    "WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppPropPermissionsType",
    "WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppType",
    "WebhookDeploymentStatusCreatedPropDeploymentStatusPropCreatorType",
    "WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppPropOwnerType",
    "WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppPropPermissionsType",
    "WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppType",
    "WebhookDeploymentStatusCreatedPropDeploymentStatusType",
    "WebhookDeploymentStatusCreatedPropDeploymentType",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropActorType",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepositoryPropOwnerType",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepositoryType",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropBaseType",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropHeadType",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsType",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropReferencedWorkflowsItemsType",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropRepositoryPropOwnerType",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropRepositoryType",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropTriggeringActorType",
    "WebhookDeploymentStatusCreatedPropWorkflowRunType",
    "WebhookDeploymentStatusCreatedType",
)
