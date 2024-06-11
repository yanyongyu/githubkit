"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0413 import WebhooksWorkflowType
from .group_0402 import EnterpriseWebhooksType
from .group_0403 import SimpleInstallationType
from .group_0405 import RepositoryWebhooksType
from .group_0406 import SimpleUserWebhooksType
from .group_0404 import OrganizationSimpleWebhooksType


class WebhookDeploymentCreatedType(TypedDict):
    """deployment created event"""

    action: Literal["created"]
    deployment: WebhookDeploymentCreatedPropDeploymentType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType
    workflow: Union[WebhooksWorkflowType, None]
    workflow_run: Union[WebhookDeploymentCreatedPropWorkflowRunType, None]


class WebhookDeploymentCreatedPropDeploymentType(TypedDict):
    """Deployment

    The [deployment](https://docs.github.com/enterprise-
    cloud@latest//rest/deployments/deployments#list-deployments).
    """

    created_at: str
    creator: Union[WebhookDeploymentCreatedPropDeploymentPropCreatorType, None]
    description: Union[str, None]
    environment: str
    id: int
    node_id: str
    original_environment: str
    payload: Union[WebhookDeploymentCreatedPropDeploymentPropPayloadOneof0Type, str]
    performed_via_github_app: NotRequired[
        Union[WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppType, None]
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


class WebhookDeploymentCreatedPropDeploymentPropCreatorType(TypedDict):
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


class WebhookDeploymentCreatedPropDeploymentPropPayloadOneof0Type(TypedDict):
    """WebhookDeploymentCreatedPropDeploymentPropPayloadOneof0"""


class WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppType(TypedDict):
    """App

    GitHub apps are a new way to extend GitHub. They can be installed directly on
    organizations and user accounts and granted access to specific repositories.
    They come with granular permissions and built-in webhooks. GitHub apps are first
    class actors within GitHub.
    """

    created_at: Union[datetime, None]
    description: Union[str, None]
    events: NotRequired[
        List[
            Literal[
                "branch_protection_rule",
                "check_run",
                "check_suite",
                "code_scanning_alert",
                "commit_comment",
                "content_reference",
                "create",
                "delete",
                "deployment",
                "deployment_review",
                "deployment_status",
                "deploy_key",
                "discussion",
                "discussion_comment",
                "fork",
                "gollum",
                "issues",
                "issue_comment",
                "label",
                "member",
                "membership",
                "milestone",
                "organization",
                "org_block",
                "page_build",
                "project",
                "project_card",
                "project_column",
                "public",
                "pull_request",
                "pull_request_review",
                "pull_request_review_comment",
                "push",
                "registry_package",
                "release",
                "repository",
                "repository_dispatch",
                "secret_scanning_alert",
                "star",
                "status",
                "team",
                "team_add",
                "watch",
                "workflow_dispatch",
                "workflow_run",
                "workflow_job",
                "pull_request_review_thread",
                "merge_queue_entry",
                "secret_scanning_alert_location",
                "merge_group",
            ]
        ]
    ]
    external_url: Union[str, None]
    html_url: str
    id: Union[int, None]
    name: str
    node_id: str
    owner: Union[
        WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppPropPermissionsType
    ]
    slug: NotRequired[str]
    updated_at: Union[datetime, None]


class WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppPropOwnerType(
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


class WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppPropPermissionsType(
    TypedDict
):
    """WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppPropPermissions

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


class WebhookDeploymentCreatedPropWorkflowRunType(TypedDict):
    """Deployment Workflow Run"""

    actor: Union[WebhookDeploymentCreatedPropWorkflowRunPropActorType, None]
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
        ],
    ]
    created_at: datetime
    display_title: str
    event: str
    head_branch: str
    head_commit: NotRequired[None]
    head_repository: NotRequired[
        WebhookDeploymentCreatedPropWorkflowRunPropHeadRepositoryType
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
    pull_requests: List[
        WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsType
    ]
    referenced_workflows: NotRequired[
        Union[
            List[
                WebhookDeploymentCreatedPropWorkflowRunPropReferencedWorkflowsItemsType
            ],
            None,
        ]
    ]
    repository: NotRequired[WebhookDeploymentCreatedPropWorkflowRunPropRepositoryType]
    rerun_url: NotRequired[str]
    run_attempt: int
    run_number: int
    run_started_at: datetime
    status: Literal[
        "requested", "in_progress", "completed", "queued", "waiting", "pending"
    ]
    triggering_actor: NotRequired[
        Union[WebhookDeploymentCreatedPropWorkflowRunPropTriggeringActorType, None]
    ]
    updated_at: datetime
    url: str
    workflow_id: int
    workflow_url: NotRequired[str]


class WebhookDeploymentCreatedPropWorkflowRunPropActorType(TypedDict):
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


class WebhookDeploymentCreatedPropWorkflowRunPropReferencedWorkflowsItemsType(
    TypedDict
):
    """WebhookDeploymentCreatedPropWorkflowRunPropReferencedWorkflowsItems"""

    path: str
    ref: NotRequired[str]
    sha: str


class WebhookDeploymentCreatedPropWorkflowRunPropTriggeringActorType(TypedDict):
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


class WebhookDeploymentCreatedPropWorkflowRunPropHeadRepositoryType(TypedDict):
    """WebhookDeploymentCreatedPropWorkflowRunPropHeadRepository"""

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
        WebhookDeploymentCreatedPropWorkflowRunPropHeadRepositoryPropOwnerType
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


class WebhookDeploymentCreatedPropWorkflowRunPropHeadRepositoryPropOwnerType(TypedDict):
    """WebhookDeploymentCreatedPropWorkflowRunPropHeadRepositoryPropOwner"""

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


class WebhookDeploymentCreatedPropWorkflowRunPropRepositoryType(TypedDict):
    """WebhookDeploymentCreatedPropWorkflowRunPropRepository"""

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
        WebhookDeploymentCreatedPropWorkflowRunPropRepositoryPropOwnerType
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


class WebhookDeploymentCreatedPropWorkflowRunPropRepositoryPropOwnerType(TypedDict):
    """WebhookDeploymentCreatedPropWorkflowRunPropRepositoryPropOwner"""

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


class WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsType(TypedDict):
    """Check Run Pull Request"""

    base: WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropBaseType
    head: WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropHeadType
    id: int
    number: int
    url: str


class WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropBaseType(
    TypedDict
):
    """WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropBase"""

    ref: str
    repo: (
        WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType
    )
    sha: str


class WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


class WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropHeadType(
    TypedDict
):
    """WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropHead"""

    ref: str
    repo: (
        WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType
    )
    sha: str


class WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


__all__ = (
    "WebhookDeploymentCreatedType",
    "WebhookDeploymentCreatedPropDeploymentType",
    "WebhookDeploymentCreatedPropDeploymentPropCreatorType",
    "WebhookDeploymentCreatedPropDeploymentPropPayloadOneof0Type",
    "WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppType",
    "WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppPropOwnerType",
    "WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppPropPermissionsType",
    "WebhookDeploymentCreatedPropWorkflowRunType",
    "WebhookDeploymentCreatedPropWorkflowRunPropActorType",
    "WebhookDeploymentCreatedPropWorkflowRunPropReferencedWorkflowsItemsType",
    "WebhookDeploymentCreatedPropWorkflowRunPropTriggeringActorType",
    "WebhookDeploymentCreatedPropWorkflowRunPropHeadRepositoryType",
    "WebhookDeploymentCreatedPropWorkflowRunPropHeadRepositoryPropOwnerType",
    "WebhookDeploymentCreatedPropWorkflowRunPropRepositoryType",
    "WebhookDeploymentCreatedPropWorkflowRunPropRepositoryPropOwnerType",
    "WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsType",
    "WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropBaseType",
    "WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType",
    "WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropHeadType",
    "WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType",
)
