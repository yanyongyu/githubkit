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
from .group_0434 import WebhooksWorkflowType


class WebhookWorkflowRunInProgressType(TypedDict):
    """workflow_run in_progress event"""

    action: Literal["in_progress"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType
    workflow: Union[WebhooksWorkflowType, None]
    workflow_run: WebhookWorkflowRunInProgressPropWorkflowRunType


class WebhookWorkflowRunInProgressPropWorkflowRunType(TypedDict):
    """Workflow Run"""

    actor: Union[WebhookWorkflowRunInProgressPropWorkflowRunPropActorType, None]
    artifacts_url: str
    cancel_url: str
    check_suite_id: int
    check_suite_node_id: str
    check_suite_url: str
    conclusion: Union[
        None,
        Literal[
            "action_required",
            "cancelled",
            "failure",
            "neutral",
            "skipped",
            "stale",
            "success",
            "timed_out",
        ],
    ]
    created_at: datetime
    event: str
    head_branch: Union[str, None]
    head_commit: WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitType
    head_repository: WebhookWorkflowRunInProgressPropWorkflowRunPropHeadRepositoryType
    head_sha: str
    html_url: str
    id: int
    jobs_url: str
    logs_url: str
    name: Union[str, None]
    node_id: str
    path: str
    previous_attempt_url: Union[str, None]
    pull_requests: list[
        Union[
            WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsType, None
        ]
    ]
    referenced_workflows: NotRequired[
        Union[
            list[
                WebhookWorkflowRunInProgressPropWorkflowRunPropReferencedWorkflowsItemsType
            ],
            None,
        ]
    ]
    repository: WebhookWorkflowRunInProgressPropWorkflowRunPropRepositoryType
    rerun_url: str
    run_attempt: int
    run_number: int
    run_started_at: datetime
    status: Literal["requested", "in_progress", "completed", "queued", "pending"]
    triggering_actor: Union[
        WebhookWorkflowRunInProgressPropWorkflowRunPropTriggeringActorType, None
    ]
    updated_at: datetime
    url: str
    workflow_id: int
    workflow_url: str


class WebhookWorkflowRunInProgressPropWorkflowRunPropActorType(TypedDict):
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


class WebhookWorkflowRunInProgressPropWorkflowRunPropReferencedWorkflowsItemsType(
    TypedDict
):
    """WebhookWorkflowRunInProgressPropWorkflowRunPropReferencedWorkflowsItems"""

    path: str
    ref: NotRequired[str]
    sha: str


class WebhookWorkflowRunInProgressPropWorkflowRunPropTriggeringActorType(TypedDict):
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


class WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitType(TypedDict):
    """SimpleCommit"""

    author: WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitPropAuthorType
    committer: (
        WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitPropCommitterType
    )
    id: str
    message: str
    timestamp: str
    tree_id: str


class WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitPropAuthorType(
    TypedDict
):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: NotRequired[datetime]
    email: Union[str, None]
    name: str
    username: NotRequired[str]


class WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitPropCommitterType(
    TypedDict
):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: NotRequired[datetime]
    email: Union[str, None]
    name: str
    username: NotRequired[str]


class WebhookWorkflowRunInProgressPropWorkflowRunPropHeadRepositoryType(TypedDict):
    """Repository Lite"""

    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    description: Union[str, None]
    downloads_url: str
    events_url: str
    fork: bool
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    hooks_url: str
    html_url: str
    id: int
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    name: Union[str, None]
    node_id: str
    notifications_url: str
    owner: Union[
        WebhookWorkflowRunInProgressPropWorkflowRunPropHeadRepositoryPropOwnerType, None
    ]
    private: bool
    pulls_url: str
    releases_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    url: str


class WebhookWorkflowRunInProgressPropWorkflowRunPropHeadRepositoryPropOwnerType(
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


class WebhookWorkflowRunInProgressPropWorkflowRunPropRepositoryType(TypedDict):
    """Repository Lite"""

    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    description: Union[str, None]
    downloads_url: str
    events_url: str
    fork: bool
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    hooks_url: str
    html_url: str
    id: int
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    name: str
    node_id: str
    notifications_url: str
    owner: Union[
        WebhookWorkflowRunInProgressPropWorkflowRunPropRepositoryPropOwnerType, None
    ]
    private: bool
    pulls_url: str
    releases_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    url: str


class WebhookWorkflowRunInProgressPropWorkflowRunPropRepositoryPropOwnerType(TypedDict):
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


class WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsType(TypedDict):
    """WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItems"""

    base: WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropBaseType
    head: WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropHeadType
    id: int
    number: int
    url: str


class WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropBaseType(
    TypedDict
):
    """WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropBase"""

    ref: str
    repo: WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType
    sha: str


class WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


class WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropHeadType(
    TypedDict
):
    """WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropHead"""

    ref: str
    repo: WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType
    sha: str


class WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


__all__ = (
    "WebhookWorkflowRunInProgressPropWorkflowRunPropActorType",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitPropAuthorType",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitPropCommitterType",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropHeadCommitType",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropHeadRepositoryPropOwnerType",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropHeadRepositoryType",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropBaseType",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsPropHeadType",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropPullRequestsItemsType",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropReferencedWorkflowsItemsType",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropRepositoryPropOwnerType",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropRepositoryType",
    "WebhookWorkflowRunInProgressPropWorkflowRunPropTriggeringActorType",
    "WebhookWorkflowRunInProgressPropWorkflowRunType",
    "WebhookWorkflowRunInProgressType",
)
