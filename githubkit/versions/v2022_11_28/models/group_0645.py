"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0032 import Milestone
from .group_0210 import AutoMerge
from .group_0001 import SimpleUser
from .group_0074 import TeamSimple
from .group_0291 import PullRequestPropBase
from .group_0293 import PullRequestPropLinks
from .group_0290 import PullRequestPropHead, PullRequestPropLabelsItems


class WebhookPullRequestConvertedToDraftPropPullRequest(GitHubModel):
    """WebhookPullRequestConvertedToDraftPropPullRequest"""

    url: str = Field()
    id: int = Field()
    node_id: str = Field()
    html_url: str = Field()
    diff_url: str = Field()
    patch_url: str = Field()
    issue_url: str = Field()
    commits_url: str = Field()
    review_comments_url: str = Field()
    review_comment_url: str = Field()
    comments_url: str = Field()
    statuses_url: str = Field()
    number: int = Field(
        description="Number uniquely identifying the pull request within its repository."
    )
    state: Literal["open", "closed"] = Field(
        description="State of this Pull Request. Either `open` or `closed`."
    )
    locked: bool = Field()
    title: str = Field(description="The title of the pull request.")
    user: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    body: Union[str, None] = Field()
    labels: List[PullRequestPropLabelsItems] = Field()
    milestone: Union[None, Milestone] = Field()
    active_lock_reason: Missing[Union[str, None]] = Field(default=UNSET)
    created_at: datetime = Field()
    updated_at: datetime = Field()
    closed_at: Union[datetime, None] = Field()
    merged_at: Union[datetime, None] = Field()
    merge_commit_sha: Union[str, None] = Field()
    assignee: Union[None, SimpleUser] = Field()
    assignees: Missing[Union[List[SimpleUser], None]] = Field(default=UNSET)
    requested_reviewers: Missing[Union[List[SimpleUser], None]] = Field(default=UNSET)
    requested_teams: Missing[Union[List[TeamSimple], None]] = Field(default=UNSET)
    head: PullRequestPropHead = Field()
    base: PullRequestPropBase = Field()
    links: PullRequestPropLinks = Field(alias="_links")
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ] = Field(
        title="author_association",
        description="How the author is associated with the repository.",
    )
    auto_merge: Union[AutoMerge, None] = Field(
        title="Auto merge", description="The status of auto merging a pull request."
    )
    draft: Missing[bool] = Field(
        default=UNSET,
        description="Indicates whether or not the pull request is a draft.",
    )
    merged: bool = Field()
    mergeable: Union[bool, None] = Field()
    rebaseable: Missing[Union[bool, None]] = Field(default=UNSET)
    mergeable_state: str = Field()
    merged_by: Union[None, SimpleUser] = Field()
    comments: int = Field()
    review_comments: int = Field()
    maintainer_can_modify: bool = Field(
        description="Indicates whether maintainers can modify the pull request."
    )
    commits: int = Field()
    additions: int = Field()
    deletions: int = Field()
    changed_files: int = Field()
    allow_auto_merge: Missing[bool] = Field(
        default=UNSET, description="Whether to allow auto-merge for pull requests."
    )
    allow_update_branch: Missing[bool] = Field(
        default=UNSET,
        description="Whether to allow updating the pull request's branch.",
    )
    delete_branch_on_merge: Missing[bool] = Field(
        default=UNSET,
        description="Whether to delete head branches when pull requests are merged.",
    )
    merge_commit_message: Missing[Literal["PR_BODY", "PR_TITLE", "BLANK"]] = Field(
        default=UNSET,
        description="The default value for a merge commit message.\n- `PR_TITLE` - default to the pull request's title.\n- `PR_BODY` - default to the pull request's body.\n- `BLANK` - default to a blank commit message.",
    )
    merge_commit_title: Missing[Literal["PR_TITLE", "MERGE_MESSAGE"]] = Field(
        default=UNSET,
        description='The default value for a merge commit title.\n- `PR_TITLE` - default to the pull request\'s title.\n- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., "Merge pull request #123 from branch-name").',
    )
    squash_merge_commit_message: Missing[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ] = Field(
        default=UNSET,
        description="The default value for a squash merge commit message:\n- `PR_BODY` - default to the pull request's body.\n- `COMMIT_MESSAGES` - default to the branch's commit messages.\n- `BLANK` - default to a blank commit message.",
    )
    squash_merge_commit_title: Missing[
        Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]
    ] = Field(
        default=UNSET,
        description="The default value for a squash merge commit title:\n- `PR_TITLE` - default to the pull request's title.\n- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit).",
    )
    use_squash_pr_title_as_default: Missing[bool] = Field(
        default=UNSET,
        description="Whether a squash merge commit can use the pull request title as default. **This property has been deprecated. Please use `squash_merge_commit_title` instead.**",
    )


model_rebuild(WebhookPullRequestConvertedToDraftPropPullRequest)

__all__ = ("WebhookPullRequestConvertedToDraftPropPullRequest",)
