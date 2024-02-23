"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0838 import (
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropReferencedWorkflowsItemsType,
)
from .group_0840 import WebhookWorkflowRunCompletedPropWorkflowRunMergedPullRequestsType


class WebhookWorkflowRunCompletedPropWorkflowRunType(TypedDict):
    """WebhookWorkflowRunCompletedPropWorkflowRun"""

    actor: WebhookWorkflowRunCompletedPropWorkflowRunMergedActorType
    artifacts_url: str
    cancel_url: str
    check_suite_id: int
    check_suite_node_id: str
    check_suite_url: str
    conclusion: Literal[
        "success",
        "failure",
        "neutral",
        "cancelled",
        "timed_out",
        "action_required",
        "stale",
        "skipped",
    ]
    created_at: datetime
    event: str
    head_branch: Union[Union[str, None], None]
    head_commit: WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadCommitType
    head_repository: WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadRepositoryType
    head_sha: str
    html_url: str
    id: int
    jobs_url: str
    logs_url: str
    name: Union[Union[str, None], None]
    node_id: str
    path: str
    previous_attempt_url: Union[Union[str, None], None]
    pull_requests: List[
        WebhookWorkflowRunCompletedPropWorkflowRunMergedPullRequestsType
    ]
    referenced_workflows: NotRequired[
        Union[
            Union[
                List[
                    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropReferencedWorkflowsItemsType
                ],
                None,
            ],
            None,
        ]
    ]
    repository: WebhookWorkflowRunCompletedPropWorkflowRunMergedRepositoryType
    rerun_url: str
    run_attempt: int
    run_number: int
    run_started_at: datetime
    status: Literal[
        "requested", "in_progress", "completed", "queued", "pending", "waiting"
    ]
    triggering_actor: Union[
        WebhookWorkflowRunCompletedPropWorkflowRunMergedTriggeringActorType, None
    ]
    updated_at: datetime
    url: str
    workflow_id: int
    workflow_url: str


class WebhookWorkflowRunCompletedPropWorkflowRunMergedActorType(TypedDict):
    """WebhookWorkflowRunCompletedPropWorkflowRunMergedActor"""

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


class WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadCommitType(TypedDict):
    """WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadCommit"""

    author: WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadCommitPropAuthorType
    committer: WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadCommitPropCommitterType
    id: str
    message: str
    timestamp: str
    tree_id: str


class WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadCommitPropAuthorType(
    TypedDict
):
    """WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadCommitPropAuthor"""

    date: NotRequired[datetime]
    email: str
    name: str
    username: NotRequired[str]


class WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadCommitPropCommitterType(
    TypedDict
):
    """WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadCommitPropCommitter"""

    date: NotRequired[datetime]
    email: str
    name: str
    username: NotRequired[str]


class WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadRepositoryType(TypedDict):
    """WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadRepository"""

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
    description: Union[Union[str, None], None]
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
    owner: WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadRepositoryPropOwnerType
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


class WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadRepositoryPropOwnerType(
    TypedDict
):
    """WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadRepositoryPropOwner"""

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


class WebhookWorkflowRunCompletedPropWorkflowRunMergedRepositoryType(TypedDict):
    """WebhookWorkflowRunCompletedPropWorkflowRunMergedRepository"""

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
    description: Union[Union[str, None], None]
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
    owner: WebhookWorkflowRunCompletedPropWorkflowRunMergedRepositoryPropOwnerType
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


class WebhookWorkflowRunCompletedPropWorkflowRunMergedRepositoryPropOwnerType(
    TypedDict
):
    """WebhookWorkflowRunCompletedPropWorkflowRunMergedRepositoryPropOwner"""

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


class WebhookWorkflowRunCompletedPropWorkflowRunMergedTriggeringActorType(TypedDict):
    """WebhookWorkflowRunCompletedPropWorkflowRunMergedTriggeringActor"""

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


__all__ = (
    "WebhookWorkflowRunCompletedPropWorkflowRunType",
    "WebhookWorkflowRunCompletedPropWorkflowRunMergedActorType",
    "WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadCommitType",
    "WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadCommitPropAuthorType",
    "WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadCommitPropCommitterType",
    "WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadRepositoryType",
    "WebhookWorkflowRunCompletedPropWorkflowRunMergedHeadRepositoryPropOwnerType",
    "WebhookWorkflowRunCompletedPropWorkflowRunMergedRepositoryType",
    "WebhookWorkflowRunCompletedPropWorkflowRunMergedRepositoryPropOwnerType",
    "WebhookWorkflowRunCompletedPropWorkflowRunMergedTriggeringActorType",
)
