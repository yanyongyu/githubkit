"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0418 import EnterpriseWebhooks
from .group_0419 import SimpleInstallation
from .group_0420 import OrganizationSimpleWebhooks
from .group_0421 import RepositoryWebhooks
from .group_0426 import WebhooksWorkflow


class WebhookWorkflowRunCompleted(GitHubModel):
    """workflow_run completed event"""

    action: Literal["completed"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    workflow: Union[WebhooksWorkflow, None] = Field(title="Workflow")
    workflow_run: WebhookWorkflowRunCompletedPropWorkflowRun = Field(
        title="Workflow Run"
    )


class WebhookWorkflowRunCompletedPropWorkflowRun(GitHubModel):
    """Workflow Run"""

    actor: Union[WebhookWorkflowRunCompletedPropWorkflowRunPropActor, None] = Field(
        title="User"
    )
    artifacts_url: str = Field()
    cancel_url: str = Field()
    check_suite_id: int = Field()
    check_suite_node_id: str = Field()
    check_suite_url: str = Field()
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
            "startup_failure",
        ],
    ] = Field()
    created_at: datetime = Field()
    event: str = Field()
    head_branch: Union[str, None] = Field()
    head_commit: WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommit = Field(
        title="SimpleCommit"
    )
    head_repository: WebhookWorkflowRunCompletedPropWorkflowRunPropHeadRepository = (
        Field(title="Repository Lite")
    )
    head_sha: str = Field()
    html_url: str = Field()
    id: int = Field()
    jobs_url: str = Field()
    logs_url: str = Field()
    name: Union[str, None] = Field()
    node_id: str = Field()
    path: str = Field()
    previous_attempt_url: Union[str, None] = Field()
    pull_requests: list[
        Union[WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItems, None]
    ] = Field()
    referenced_workflows: Missing[
        Union[
            list[
                WebhookWorkflowRunCompletedPropWorkflowRunPropReferencedWorkflowsItems
            ],
            None,
        ]
    ] = Field(default=UNSET)
    repository: WebhookWorkflowRunCompletedPropWorkflowRunPropRepository = Field(
        title="Repository Lite"
    )
    rerun_url: str = Field()
    run_attempt: int = Field()
    run_number: int = Field()
    run_started_at: datetime = Field()
    status: Literal[
        "requested", "in_progress", "completed", "queued", "pending", "waiting"
    ] = Field()
    triggering_actor: Union[
        WebhookWorkflowRunCompletedPropWorkflowRunPropTriggeringActor, None
    ] = Field(title="User")
    updated_at: datetime = Field()
    url: str = Field()
    workflow_id: int = Field()
    workflow_url: str = Field()
    display_title: Missing[str] = Field(
        default=UNSET,
        description="The event-specific title associated with the run or the run-name if set, or the value of `run-name` if it is set in the workflow.",
    )


class WebhookWorkflowRunCompletedPropWorkflowRunPropActor(GitHubModel):
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
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunPropReferencedWorkflowsItems(
    GitHubModel
):
    """WebhookWorkflowRunCompletedPropWorkflowRunPropReferencedWorkflowsItems"""

    path: str = Field()
    ref: Missing[str] = Field(default=UNSET)
    sha: str = Field()


class WebhookWorkflowRunCompletedPropWorkflowRunPropTriggeringActor(GitHubModel):
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
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommit(GitHubModel):
    """SimpleCommit"""

    author: WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitPropAuthor = Field(
        title="Committer",
        description="Metaproperties for Git author/committer information.",
    )
    committer: WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitPropCommitter = (
        Field(
            title="Committer",
            description="Metaproperties for Git author/committer information.",
        )
    )
    id: str = Field()
    message: str = Field()
    timestamp: str = Field()
    tree_id: str = Field()


class WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitPropAuthor(GitHubModel):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: Missing[datetime] = Field(default=UNSET)
    email: Union[str, None] = Field()
    name: str = Field(description="The git author's name.")
    username: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitPropCommitter(
    GitHubModel
):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: Missing[datetime] = Field(default=UNSET)
    email: Union[str, None] = Field()
    name: str = Field(description="The git author's name.")
    username: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunPropHeadRepository(GitHubModel):
    """Repository Lite"""

    archive_url: str = Field()
    assignees_url: str = Field()
    blobs_url: str = Field()
    branches_url: str = Field()
    collaborators_url: str = Field()
    comments_url: str = Field()
    commits_url: str = Field()
    compare_url: str = Field()
    contents_url: str = Field()
    contributors_url: str = Field()
    deployments_url: str = Field()
    description: Union[str, None] = Field()
    downloads_url: str = Field()
    events_url: str = Field()
    fork: bool = Field()
    forks_url: str = Field()
    full_name: str = Field()
    git_commits_url: str = Field()
    git_refs_url: str = Field()
    git_tags_url: str = Field()
    hooks_url: str = Field()
    html_url: str = Field()
    id: int = Field(description="Unique identifier of the repository")
    issue_comment_url: str = Field()
    issue_events_url: str = Field()
    issues_url: str = Field()
    keys_url: str = Field()
    labels_url: str = Field()
    languages_url: str = Field()
    merges_url: str = Field()
    milestones_url: str = Field()
    name: str = Field(description="The name of the repository.")
    node_id: str = Field()
    notifications_url: str = Field()
    owner: Union[
        WebhookWorkflowRunCompletedPropWorkflowRunPropHeadRepositoryPropOwner, None
    ] = Field(title="User")
    private: bool = Field(description="Whether the repository is private or public.")
    pulls_url: str = Field()
    releases_url: str = Field()
    stargazers_url: str = Field()
    statuses_url: str = Field()
    subscribers_url: str = Field()
    subscription_url: str = Field()
    tags_url: str = Field()
    teams_url: str = Field()
    trees_url: str = Field()
    url: str = Field()


class WebhookWorkflowRunCompletedPropWorkflowRunPropHeadRepositoryPropOwner(
    GitHubModel
):
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
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunPropRepository(GitHubModel):
    """Repository Lite"""

    archive_url: str = Field()
    assignees_url: str = Field()
    blobs_url: str = Field()
    branches_url: str = Field()
    collaborators_url: str = Field()
    comments_url: str = Field()
    commits_url: str = Field()
    compare_url: str = Field()
    contents_url: str = Field()
    contributors_url: str = Field()
    deployments_url: str = Field()
    description: Union[str, None] = Field()
    downloads_url: str = Field()
    events_url: str = Field()
    fork: bool = Field()
    forks_url: str = Field()
    full_name: str = Field()
    git_commits_url: str = Field()
    git_refs_url: str = Field()
    git_tags_url: str = Field()
    hooks_url: str = Field()
    html_url: str = Field()
    id: int = Field(description="Unique identifier of the repository")
    issue_comment_url: str = Field()
    issue_events_url: str = Field()
    issues_url: str = Field()
    keys_url: str = Field()
    labels_url: str = Field()
    languages_url: str = Field()
    merges_url: str = Field()
    milestones_url: str = Field()
    name: str = Field(description="The name of the repository.")
    node_id: str = Field()
    notifications_url: str = Field()
    owner: Union[
        WebhookWorkflowRunCompletedPropWorkflowRunPropRepositoryPropOwner, None
    ] = Field(title="User")
    private: bool = Field(description="Whether the repository is private or public.")
    pulls_url: str = Field()
    releases_url: str = Field()
    stargazers_url: str = Field()
    statuses_url: str = Field()
    subscribers_url: str = Field()
    subscription_url: str = Field()
    tags_url: str = Field()
    teams_url: str = Field()
    trees_url: str = Field()
    url: str = Field()


class WebhookWorkflowRunCompletedPropWorkflowRunPropRepositoryPropOwner(GitHubModel):
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
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItems(GitHubModel):
    """WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItems"""

    base: WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropBase = (
        Field()
    )
    head: WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropHead = (
        Field()
    )
    id: int = Field()
    number: int = Field()
    url: str = Field()


class WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropBase(
    GitHubModel
):
    """WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropBase"""

    ref: str = Field()
    repo: WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropBasePropRepo = Field(
        title="Repo Ref"
    )
    sha: str = Field()


class WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropBasePropRepo(
    GitHubModel
):
    """Repo Ref"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


class WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropHead(
    GitHubModel
):
    """WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropHead"""

    ref: str = Field()
    repo: WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo = Field(
        title="Repo Ref"
    )
    sha: str = Field()


class WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo(
    GitHubModel
):
    """Repo Ref"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


model_rebuild(WebhookWorkflowRunCompleted)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRun)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunPropActor)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunPropReferencedWorkflowsItems)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunPropTriggeringActor)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommit)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitPropAuthor)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitPropCommitter)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunPropHeadRepository)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunPropHeadRepositoryPropOwner)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunPropRepository)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunPropRepositoryPropOwner)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItems)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropBase)
model_rebuild(
    WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropBasePropRepo
)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropHead)
model_rebuild(
    WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo
)

__all__ = (
    "WebhookWorkflowRunCompleted",
    "WebhookWorkflowRunCompletedPropWorkflowRun",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropActor",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommit",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitPropAuthor",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropHeadCommitPropCommitter",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropHeadRepository",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropHeadRepositoryPropOwner",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItems",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropBase",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropBasePropRepo",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropHead",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropReferencedWorkflowsItems",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropRepository",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropRepositoryPropOwner",
    "WebhookWorkflowRunCompletedPropWorkflowRunPropTriggeringActor",
)
