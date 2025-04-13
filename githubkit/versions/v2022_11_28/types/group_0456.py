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
from .group_0039 import MilestoneType
from .group_0079 import TeamSimpleType
from .group_0263 import AutoMergeType
from .group_0343 import PullRequestPropLabelsItemsType
from .group_0344 import PullRequestPropBaseType, PullRequestPropHeadType
from .group_0345 import PullRequestPropLinksType


class PullRequestWebhookType(TypedDict):
    """PullRequestWebhook"""

    url: str
    id: int
    node_id: str
    html_url: str
    diff_url: str
    patch_url: str
    issue_url: str
    commits_url: str
    review_comments_url: str
    review_comment_url: str
    comments_url: str
    statuses_url: str
    number: int
    state: Literal["open", "closed"]
    locked: bool
    title: str
    user: SimpleUserType
    body: Union[str, None]
    labels: list[PullRequestPropLabelsItemsType]
    milestone: Union[None, MilestoneType]
    active_lock_reason: NotRequired[Union[str, None]]
    created_at: datetime
    updated_at: datetime
    closed_at: Union[datetime, None]
    merged_at: Union[datetime, None]
    merge_commit_sha: Union[str, None]
    assignee: Union[None, SimpleUserType]
    assignees: NotRequired[Union[list[SimpleUserType], None]]
    requested_reviewers: NotRequired[Union[list[SimpleUserType], None]]
    requested_teams: NotRequired[Union[list[TeamSimpleType], None]]
    head: PullRequestPropHeadType
    base: PullRequestPropBaseType
    links: PullRequestPropLinksType
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]
    auto_merge: Union[AutoMergeType, None]
    draft: NotRequired[bool]
    merged: bool
    mergeable: Union[bool, None]
    rebaseable: NotRequired[Union[bool, None]]
    mergeable_state: str
    merged_by: Union[None, SimpleUserType]
    comments: int
    review_comments: int
    maintainer_can_modify: bool
    commits: int
    additions: int
    deletions: int
    changed_files: int
    allow_auto_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    delete_branch_on_merge: NotRequired[bool]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    use_squash_pr_title_as_default: NotRequired[bool]


__all__ = ("PullRequestWebhookType",)
