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
from githubkit.compat import GitHubModel, model_rebuild

from .group_0803 import (
    WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItems,
)
from .group_0805 import (
    WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropReferencedWorkflowsItems,
)


class WebhookWorkflowRunInProgressPropWorkflowRunAllof0(GitHubModel):
    """Workflow Run"""

    actor: Union[
        WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropActor, None
    ] = Field(title="User")
    artifacts_url: str = Field()
    cancel_url: str = Field()
    check_suite_id: int = Field()
    check_suite_node_id: str = Field()
    check_suite_url: str = Field()
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
    ] = Field()
    created_at: datetime = Field()
    event: str = Field()
    head_branch: Union[str, None] = Field()
    head_commit: WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadCommit = (
        Field(title="SimpleCommit")
    )
    head_repository: WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadRepository = Field(
        title="Repository Lite"
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
    pull_requests: List[
        WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropPullRequestsItems
    ] = Field()
    referenced_workflows: Missing[
        Union[
            List[
                WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropReferencedWorkflowsItems
            ],
            None,
        ]
    ] = Field(default=UNSET)
    repository: WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropRepository = Field(
        title="Repository Lite"
    )
    rerun_url: str = Field()
    run_attempt: int = Field()
    run_number: int = Field()
    run_started_at: datetime = Field()
    status: Literal[
        "requested", "in_progress", "completed", "queued", "pending"
    ] = Field()
    triggering_actor: Union[
        WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropTriggeringActor, None
    ] = Field(title="User")
    updated_at: datetime = Field()
    url: str = Field()
    workflow_id: int = Field()
    workflow_url: str = Field()


class WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropActor(GitHubModel):
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


class WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropTriggeringActor(GitHubModel):
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


class WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadCommit(GitHubModel):
    """SimpleCommit"""

    author: WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadCommitPropAuthor = Field(
        title="Committer",
        description="Metaproperties for Git author/committer information.",
    )
    committer: WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadCommitPropCommitter = Field(
        title="Committer",
        description="Metaproperties for Git author/committer information.",
    )
    id: str = Field()
    message: str = Field()
    timestamp: str = Field()
    tree_id: str = Field()


class WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadCommitPropAuthor(
    GitHubModel
):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: Missing[datetime] = Field(default=UNSET)
    email: Union[str, None] = Field()
    name: str = Field(description="The git author's name.")
    username: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadCommitPropCommitter(
    GitHubModel
):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: Missing[datetime] = Field(default=UNSET)
    email: Union[str, None] = Field()
    name: str = Field(description="The git author's name.")
    username: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadRepository(GitHubModel):
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
        WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadRepositoryPropOwner,
        None,
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


class WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadRepositoryPropOwner(
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


class WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropRepository(GitHubModel):
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
        WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropRepositoryPropOwner, None
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


class WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropRepositoryPropOwner(
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


model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunAllof0)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropActor)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropTriggeringActor)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadCommit)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadCommitPropAuthor)
model_rebuild(
    WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadCommitPropCommitter
)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadRepository)
model_rebuild(
    WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadRepositoryPropOwner
)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropRepository)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropRepositoryPropOwner)

__all__ = (
    "WebhookWorkflowRunInProgressPropWorkflowRunAllof0",
    "WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropActor",
    "WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropTriggeringActor",
    "WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadCommit",
    "WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadCommitPropAuthor",
    "WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadCommitPropCommitter",
    "WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadRepository",
    "WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropHeadRepositoryPropOwner",
    "WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropRepository",
    "WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropRepositoryPropOwner",
)
