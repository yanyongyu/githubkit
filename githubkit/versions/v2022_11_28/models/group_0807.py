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

from .group_0811 import (
    WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropReferencedWorkflowsItems,
)
from .group_0813 import WebhookWorkflowRunInProgressPropWorkflowRunMergedPullRequests


class WebhookWorkflowRunInProgressPropWorkflowRun(GitHubModel):
    """WebhookWorkflowRunInProgressPropWorkflowRun"""

    actor: WebhookWorkflowRunInProgressPropWorkflowRunMergedActor = Field()
    artifacts_url: str = Field()
    cancel_url: str = Field()
    check_suite_id: int = Field()
    check_suite_node_id: str = Field()
    check_suite_url: str = Field()
    conclusion: Union[
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
        None,
    ] = Field()
    created_at: datetime = Field()
    event: str = Field()
    head_branch: Union[Union[str, None], None] = Field()
    head_commit: WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadCommit = Field()
    head_repository: WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadRepository = (
        Field()
    )
    head_sha: str = Field()
    html_url: str = Field()
    id: int = Field()
    jobs_url: str = Field()
    logs_url: str = Field()
    name: Union[Union[str, None], None] = Field()
    node_id: str = Field()
    path: str = Field()
    previous_attempt_url: Union[Union[str, None], None] = Field()
    pull_requests: List[
        WebhookWorkflowRunInProgressPropWorkflowRunMergedPullRequests
    ] = Field()
    referenced_workflows: Missing[
        Union[
            Union[
                List[
                    WebhookWorkflowRunInProgressPropWorkflowRunAllof0PropReferencedWorkflowsItems
                ],
                None,
            ],
            None,
        ]
    ] = Field(default=UNSET)
    repository: WebhookWorkflowRunInProgressPropWorkflowRunMergedRepository = Field()
    rerun_url: str = Field()
    run_attempt: int = Field()
    run_number: int = Field()
    run_started_at: datetime = Field()
    status: Literal[
        "requested", "in_progress", "completed", "queued", "pending"
    ] = Field()
    triggering_actor: WebhookWorkflowRunInProgressPropWorkflowRunMergedTriggeringActor = Field()
    updated_at: datetime = Field()
    url: str = Field()
    workflow_id: int = Field()
    workflow_url: str = Field()


class WebhookWorkflowRunInProgressPropWorkflowRunMergedActor(GitHubModel):
    """WebhookWorkflowRunInProgressPropWorkflowRunMergedActor"""

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


class WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadCommit(GitHubModel):
    """WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadCommit"""

    author: WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadCommitPropAuthor = (
        Field()
    )
    committer: WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadCommitPropCommitter = Field()
    id: str = Field()
    message: str = Field()
    timestamp: str = Field()
    tree_id: str = Field()


class WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadCommitPropAuthor(
    GitHubModel
):
    """WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadCommitPropAuthor"""

    date: Missing[datetime] = Field(default=UNSET)
    email: str = Field()
    name: str = Field(description="The git author's name.")
    username: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadCommitPropCommitter(
    GitHubModel
):
    """WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadCommitPropCommitter"""

    date: Missing[datetime] = Field(default=UNSET)
    email: str = Field()
    name: str = Field(description="The git author's name.")
    username: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadRepository(GitHubModel):
    """WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadRepository"""

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
    description: Union[Union[str, None], None] = Field()
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
    owner: WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadRepositoryPropOwner = (
        Field()
    )
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


class WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadRepositoryPropOwner(
    GitHubModel
):
    """WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadRepositoryPropOwner"""

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


class WebhookWorkflowRunInProgressPropWorkflowRunMergedRepository(GitHubModel):
    """WebhookWorkflowRunInProgressPropWorkflowRunMergedRepository"""

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
    description: Union[Union[str, None], None] = Field()
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
    owner: WebhookWorkflowRunInProgressPropWorkflowRunMergedRepositoryPropOwner = (
        Field()
    )
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


class WebhookWorkflowRunInProgressPropWorkflowRunMergedRepositoryPropOwner(GitHubModel):
    """WebhookWorkflowRunInProgressPropWorkflowRunMergedRepositoryPropOwner"""

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


class WebhookWorkflowRunInProgressPropWorkflowRunMergedTriggeringActor(GitHubModel):
    """WebhookWorkflowRunInProgressPropWorkflowRunMergedTriggeringActor"""

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


model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRun)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunMergedActor)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadCommit)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadCommitPropAuthor)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadCommitPropCommitter)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadRepository)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadRepositoryPropOwner)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunMergedRepository)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunMergedRepositoryPropOwner)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflowRunMergedTriggeringActor)

__all__ = (
    "WebhookWorkflowRunInProgressPropWorkflowRun",
    "WebhookWorkflowRunInProgressPropWorkflowRunMergedActor",
    "WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadCommit",
    "WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadCommitPropAuthor",
    "WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadCommitPropCommitter",
    "WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadRepository",
    "WebhookWorkflowRunInProgressPropWorkflowRunMergedHeadRepositoryPropOwner",
    "WebhookWorkflowRunInProgressPropWorkflowRunMergedRepository",
    "WebhookWorkflowRunInProgressPropWorkflowRunMergedRepositoryPropOwner",
    "WebhookWorkflowRunInProgressPropWorkflowRunMergedTriggeringActor",
)
