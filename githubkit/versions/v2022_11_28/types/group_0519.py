"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0426 import EnterpriseWebhooksType
from .group_0427 import SimpleInstallationType
from .group_0428 import OrganizationSimpleWebhooksType
from .group_0429 import RepositoryWebhooksType
from .group_0435 import WebhooksApproverType, WebhooksReviewersItemsType
from .group_0436 import WebhooksWorkflowJobRunType


class WebhookDeploymentReviewRejectedType(TypedDict):
    """WebhookDeploymentReviewRejected"""

    action: Literal["rejected"]
    approver: NotRequired[WebhooksApproverType]
    comment: NotRequired[str]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    repository: RepositoryWebhooksType
    reviewers: NotRequired[list[WebhooksReviewersItemsType]]
    sender: SimpleUserType
    since: str
    workflow_job_run: NotRequired[WebhooksWorkflowJobRunType]
    workflow_job_runs: NotRequired[
        list[WebhookDeploymentReviewRejectedPropWorkflowJobRunsItemsType]
    ]
    workflow_run: Union[WebhookDeploymentReviewRejectedPropWorkflowRunType, None]


class WebhookDeploymentReviewRejectedPropWorkflowJobRunsItemsType(TypedDict):
    """WebhookDeploymentReviewRejectedPropWorkflowJobRunsItems"""

    conclusion: NotRequired[Union[str, None]]
    created_at: NotRequired[str]
    environment: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    name: NotRequired[Union[str, None]]
    status: NotRequired[str]
    updated_at: NotRequired[str]


class WebhookDeploymentReviewRejectedPropWorkflowRunType(TypedDict):
    """Deployment Workflow Run"""

    actor: Union[WebhookDeploymentReviewRejectedPropWorkflowRunPropActorType, None]
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
    event: str
    head_branch: str
    head_commit: NotRequired[
        Union[WebhookDeploymentReviewRejectedPropWorkflowRunPropHeadCommitType, None]
    ]
    head_repository: NotRequired[
        WebhookDeploymentReviewRejectedPropWorkflowRunPropHeadRepositoryType
    ]
    head_sha: str
    html_url: str
    id: int
    jobs_url: NotRequired[str]
    logs_url: NotRequired[str]
    name: str
    node_id: str
    path: str
    previous_attempt_url: NotRequired[Union[str, None]]
    pull_requests: list[
        WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsType
    ]
    referenced_workflows: NotRequired[
        Union[
            list[
                WebhookDeploymentReviewRejectedPropWorkflowRunPropReferencedWorkflowsItemsType
            ],
            None,
        ]
    ]
    repository: NotRequired[
        WebhookDeploymentReviewRejectedPropWorkflowRunPropRepositoryType
    ]
    rerun_url: NotRequired[str]
    run_attempt: int
    run_number: int
    run_started_at: datetime
    status: Literal["requested", "in_progress", "completed", "queued", "waiting"]
    triggering_actor: Union[
        WebhookDeploymentReviewRejectedPropWorkflowRunPropTriggeringActorType, None
    ]
    updated_at: datetime
    url: str
    workflow_id: int
    workflow_url: NotRequired[str]
    display_title: str


class WebhookDeploymentReviewRejectedPropWorkflowRunPropActorType(TypedDict):
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


class WebhookDeploymentReviewRejectedPropWorkflowRunPropHeadCommitType(TypedDict):
    """WebhookDeploymentReviewRejectedPropWorkflowRunPropHeadCommit"""


class WebhookDeploymentReviewRejectedPropWorkflowRunPropReferencedWorkflowsItemsType(
    TypedDict
):
    """WebhookDeploymentReviewRejectedPropWorkflowRunPropReferencedWorkflowsItems"""

    path: str
    ref: NotRequired[str]
    sha: str


class WebhookDeploymentReviewRejectedPropWorkflowRunPropTriggeringActorType(TypedDict):
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


class WebhookDeploymentReviewRejectedPropWorkflowRunPropHeadRepositoryType(TypedDict):
    """WebhookDeploymentReviewRejectedPropWorkflowRunPropHeadRepository"""

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
    description: NotRequired[Union[str, None]]
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
        WebhookDeploymentReviewRejectedPropWorkflowRunPropHeadRepositoryPropOwnerType
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


class WebhookDeploymentReviewRejectedPropWorkflowRunPropHeadRepositoryPropOwnerType(
    TypedDict
):
    """WebhookDeploymentReviewRejectedPropWorkflowRunPropHeadRepositoryPropOwner"""

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
    user_view_type: NotRequired[str]


class WebhookDeploymentReviewRejectedPropWorkflowRunPropRepositoryType(TypedDict):
    """WebhookDeploymentReviewRejectedPropWorkflowRunPropRepository"""

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
    description: NotRequired[Union[str, None]]
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
        WebhookDeploymentReviewRejectedPropWorkflowRunPropRepositoryPropOwnerType
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


class WebhookDeploymentReviewRejectedPropWorkflowRunPropRepositoryPropOwnerType(
    TypedDict
):
    """WebhookDeploymentReviewRejectedPropWorkflowRunPropRepositoryPropOwner"""

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
    user_view_type: NotRequired[str]


class WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsType(
    TypedDict
):
    """Check Run Pull Request"""

    base: (
        WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsPropBaseType
    )
    head: (
        WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsPropHeadType
    )
    id: int
    number: int
    url: str


class WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsPropBaseType(
    TypedDict
):
    """WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsPropBase"""

    ref: str
    repo: WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType
    sha: str


class WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


class WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsPropHeadType(
    TypedDict
):
    """WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsPropHead"""

    ref: str
    repo: WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType
    sha: str


class WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


__all__ = (
    "WebhookDeploymentReviewRejectedPropWorkflowJobRunsItemsType",
    "WebhookDeploymentReviewRejectedPropWorkflowRunPropActorType",
    "WebhookDeploymentReviewRejectedPropWorkflowRunPropHeadCommitType",
    "WebhookDeploymentReviewRejectedPropWorkflowRunPropHeadRepositoryPropOwnerType",
    "WebhookDeploymentReviewRejectedPropWorkflowRunPropHeadRepositoryType",
    "WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType",
    "WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsPropBaseType",
    "WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType",
    "WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsPropHeadType",
    "WebhookDeploymentReviewRejectedPropWorkflowRunPropPullRequestsItemsType",
    "WebhookDeploymentReviewRejectedPropWorkflowRunPropReferencedWorkflowsItemsType",
    "WebhookDeploymentReviewRejectedPropWorkflowRunPropRepositoryPropOwnerType",
    "WebhookDeploymentReviewRejectedPropWorkflowRunPropRepositoryType",
    "WebhookDeploymentReviewRejectedPropWorkflowRunPropTriggeringActorType",
    "WebhookDeploymentReviewRejectedPropWorkflowRunType",
    "WebhookDeploymentReviewRejectedType",
)
