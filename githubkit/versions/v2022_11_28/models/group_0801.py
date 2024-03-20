"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0802 import (
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItems,
)
from .group_0804 import (
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropReferencedWorkflowsItems,
)


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0(GitHubModel):
    """Workflow Run"""

    actor: Union[
        WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropActor, None
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
    head_commit: WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadCommit = Field(
        title="SimpleCommit"
    )
    head_repository: WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadRepository = Field(
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
        WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItems
    ] = Field()
    referenced_workflows: Missing[
        Union[
            List[
                WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropReferencedWorkflowsItems
            ],
            None,
        ]
    ] = Field(default=UNSET)
    repository: WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropRepository = Field(
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
        WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropTriggeringActor, None
    ] = Field(title="User")
    updated_at: datetime = Field()
    url: str = Field()
    workflow_id: int = Field()
    workflow_url: str = Field()


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropActor(GitHubModel):
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


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropTriggeringActor(GitHubModel):
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


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadCommit(GitHubModel):
    """SimpleCommit"""

    author: WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadCommitPropAuthor = (
        Field(
            title="Committer",
            description="Metaproperties for Git author/committer information.",
        )
    )
    committer: WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadCommitPropCommitter = Field(
        title="Committer",
        description="Metaproperties for Git author/committer information.",
    )
    id: str = Field()
    message: str = Field()
    timestamp: str = Field()
    tree_id: str = Field()


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadCommitPropAuthor(
    GitHubModel
):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: Missing[datetime] = Field(default=UNSET)
    email: Union[str, None] = Field()
    name: str = Field(description="The git author's name.")
    username: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadCommitPropCommitter(
    GitHubModel
):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: Missing[datetime] = Field(default=UNSET)
    email: Union[str, None] = Field()
    name: str = Field(description="The git author's name.")
    username: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadRepository(GitHubModel):
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
        WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadRepositoryPropOwner,
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


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadRepositoryPropOwner(
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


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropRepository(GitHubModel):
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
        WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropRepositoryPropOwner, None
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


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropRepositoryPropOwner(
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


model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof0)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropActor)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropTriggeringActor)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadCommit)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadCommitPropAuthor)
model_rebuild(
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadCommitPropCommitter
)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadRepository)
model_rebuild(
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadRepositoryPropOwner
)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropRepository)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropRepositoryPropOwner)

__all__ = (
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropActor",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropTriggeringActor",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadCommit",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadCommitPropAuthor",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadCommitPropCommitter",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadRepository",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropHeadRepositoryPropOwner",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropRepository",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropRepositoryPropOwner",
)
