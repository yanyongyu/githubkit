"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhookWorkflowRunCompletedPropWorkflowRunAllof1(GitHubModel):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof1"""

    actor: Missing[WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropActor] = Field(
        default=UNSET
    )
    artifacts_url: Missing[str] = Field(default=UNSET)
    cancel_url: Missing[str] = Field(default=UNSET)
    check_suite_id: Missing[int] = Field(default=UNSET)
    check_suite_node_id: Missing[str] = Field(default=UNSET)
    check_suite_url: Missing[str] = Field(default=UNSET)
    conclusion: Literal[
        "success",
        "failure",
        "neutral",
        "cancelled",
        "timed_out",
        "action_required",
        "stale",
        "skipped",
    ] = Field()
    created_at: Missing[str] = Field(default=UNSET)
    event: Missing[str] = Field(default=UNSET)
    head_branch: Missing[Union[str, None]] = Field(default=UNSET)
    head_commit: Missing[
        WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadCommit
    ] = Field(default=UNSET)
    head_repository: Missing[
        WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadRepository
    ] = Field(default=UNSET)
    head_sha: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    jobs_url: Missing[str] = Field(default=UNSET)
    logs_url: Missing[str] = Field(default=UNSET)
    name: Missing[Union[str, None]] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    path: Missing[str] = Field(default=UNSET)
    previous_attempt_url: Missing[Union[str, None]] = Field(default=UNSET)
    pull_requests: Missing[
        List[
            Union[
                WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropPullRequestsItems,
                None,
            ]
        ]
    ] = Field(default=UNSET)
    referenced_workflows: Missing[
        Union[
            List[
                WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropReferencedWorkflowsItems
            ],
            None,
        ]
    ] = Field(default=UNSET)
    repository: Missing[
        WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropRepository
    ] = Field(default=UNSET)
    rerun_url: Missing[str] = Field(default=UNSET)
    run_attempt: Missing[int] = Field(default=UNSET)
    run_number: Missing[int] = Field(default=UNSET)
    run_started_at: Missing[str] = Field(default=UNSET)
    status: Missing[str] = Field(default=UNSET)
    triggering_actor: Missing[
        Union[WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropTriggeringActor, None]
    ] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    workflow_id: Missing[int] = Field(default=UNSET)
    workflow_url: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropActor(GitHubModel):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropActor"""

    avatar_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropPullRequestsItems(
    GitHubModel
):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropPullRequestsItems"""


class WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropReferencedWorkflowsItems(
    GitHubModel
):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropReferencedWorkflowsItems"""

    path: str = Field()
    ref: Missing[str] = Field(default=UNSET)
    sha: str = Field()


class WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropTriggeringActor(GitHubModel):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropTriggeringActor"""

    avatar_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadCommit(GitHubModel):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadCommit"""

    author: Missing[
        WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadCommitPropAuthor
    ] = Field(default=UNSET)
    committer: Missing[
        WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadCommitPropCommitter
    ] = Field(default=UNSET)
    id: Missing[str] = Field(default=UNSET)
    message: Missing[str] = Field(default=UNSET)
    timestamp: Missing[str] = Field(default=UNSET)
    tree_id: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadCommitPropAuthor(
    GitHubModel
):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadCommitPropAuthor"""

    email: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadCommitPropCommitter(
    GitHubModel
):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadCommitPropCommitter"""

    email: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadRepository(GitHubModel):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadRepository"""

    archive_url: Missing[str] = Field(default=UNSET)
    assignees_url: Missing[str] = Field(default=UNSET)
    blobs_url: Missing[str] = Field(default=UNSET)
    branches_url: Missing[str] = Field(default=UNSET)
    collaborators_url: Missing[str] = Field(default=UNSET)
    comments_url: Missing[str] = Field(default=UNSET)
    commits_url: Missing[str] = Field(default=UNSET)
    compare_url: Missing[str] = Field(default=UNSET)
    contents_url: Missing[str] = Field(default=UNSET)
    contributors_url: Missing[str] = Field(default=UNSET)
    deployments_url: Missing[str] = Field(default=UNSET)
    description: Missing[Union[str, None]] = Field(default=UNSET)
    downloads_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    fork: Missing[bool] = Field(default=UNSET)
    forks_url: Missing[str] = Field(default=UNSET)
    full_name: Missing[str] = Field(default=UNSET)
    git_commits_url: Missing[str] = Field(default=UNSET)
    git_refs_url: Missing[str] = Field(default=UNSET)
    git_tags_url: Missing[str] = Field(default=UNSET)
    hooks_url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    issue_comment_url: Missing[str] = Field(default=UNSET)
    issue_events_url: Missing[str] = Field(default=UNSET)
    issues_url: Missing[str] = Field(default=UNSET)
    keys_url: Missing[str] = Field(default=UNSET)
    labels_url: Missing[str] = Field(default=UNSET)
    languages_url: Missing[str] = Field(default=UNSET)
    merges_url: Missing[str] = Field(default=UNSET)
    milestones_url: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    notifications_url: Missing[str] = Field(default=UNSET)
    owner: Missing[
        WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadRepositoryPropOwner
    ] = Field(default=UNSET)
    private: Missing[bool] = Field(default=UNSET)
    pulls_url: Missing[str] = Field(default=UNSET)
    releases_url: Missing[str] = Field(default=UNSET)
    stargazers_url: Missing[str] = Field(default=UNSET)
    statuses_url: Missing[str] = Field(default=UNSET)
    subscribers_url: Missing[str] = Field(default=UNSET)
    subscription_url: Missing[str] = Field(default=UNSET)
    tags_url: Missing[str] = Field(default=UNSET)
    teams_url: Missing[str] = Field(default=UNSET)
    trees_url: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadRepositoryPropOwner(
    GitHubModel
):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadRepositoryPropOwner"""

    avatar_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropRepository(GitHubModel):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropRepository"""

    archive_url: Missing[str] = Field(default=UNSET)
    assignees_url: Missing[str] = Field(default=UNSET)
    blobs_url: Missing[str] = Field(default=UNSET)
    branches_url: Missing[str] = Field(default=UNSET)
    collaborators_url: Missing[str] = Field(default=UNSET)
    comments_url: Missing[str] = Field(default=UNSET)
    commits_url: Missing[str] = Field(default=UNSET)
    compare_url: Missing[str] = Field(default=UNSET)
    contents_url: Missing[str] = Field(default=UNSET)
    contributors_url: Missing[str] = Field(default=UNSET)
    deployments_url: Missing[str] = Field(default=UNSET)
    description: Missing[Union[str, None]] = Field(default=UNSET)
    downloads_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    fork: Missing[bool] = Field(default=UNSET)
    forks_url: Missing[str] = Field(default=UNSET)
    full_name: Missing[str] = Field(default=UNSET)
    git_commits_url: Missing[str] = Field(default=UNSET)
    git_refs_url: Missing[str] = Field(default=UNSET)
    git_tags_url: Missing[str] = Field(default=UNSET)
    hooks_url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    issue_comment_url: Missing[str] = Field(default=UNSET)
    issue_events_url: Missing[str] = Field(default=UNSET)
    issues_url: Missing[str] = Field(default=UNSET)
    keys_url: Missing[str] = Field(default=UNSET)
    labels_url: Missing[str] = Field(default=UNSET)
    languages_url: Missing[str] = Field(default=UNSET)
    merges_url: Missing[str] = Field(default=UNSET)
    milestones_url: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    notifications_url: Missing[str] = Field(default=UNSET)
    owner: Missing[
        WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropRepositoryPropOwner
    ] = Field(default=UNSET)
    private: Missing[bool] = Field(default=UNSET)
    pulls_url: Missing[str] = Field(default=UNSET)
    releases_url: Missing[str] = Field(default=UNSET)
    stargazers_url: Missing[str] = Field(default=UNSET)
    statuses_url: Missing[str] = Field(default=UNSET)
    subscribers_url: Missing[str] = Field(default=UNSET)
    subscription_url: Missing[str] = Field(default=UNSET)
    tags_url: Missing[str] = Field(default=UNSET)
    teams_url: Missing[str] = Field(default=UNSET)
    trees_url: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropRepositoryPropOwner(
    GitHubModel
):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropRepositoryPropOwner"""

    avatar_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof1)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropActor)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropPullRequestsItems)
model_rebuild(
    WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropReferencedWorkflowsItems
)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropTriggeringActor)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadCommit)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadCommitPropAuthor)
model_rebuild(
    WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadCommitPropCommitter
)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadRepository)
model_rebuild(
    WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadRepositoryPropOwner
)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropRepository)
model_rebuild(WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropRepositoryPropOwner)

__all__ = (
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof1",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropActor",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropPullRequestsItems",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropReferencedWorkflowsItems",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropTriggeringActor",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadCommit",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadCommitPropAuthor",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadCommitPropCommitter",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadRepository",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropHeadRepositoryPropOwner",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropRepository",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof1PropRepositoryPropOwner",
)
