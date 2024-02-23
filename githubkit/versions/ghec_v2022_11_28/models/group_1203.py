"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class UserReposPostBody(GitHubModel):
    """UserReposPostBody"""

    name: str = Field(description="The name of the repository.")
    description: Missing[str] = Field(
        default=UNSET, description="A short description of the repository."
    )
    homepage: Missing[str] = Field(
        default=UNSET, description="A URL with more information about the repository."
    )
    private: Missing[bool] = Field(
        default=UNSET, description="Whether the repository is private."
    )
    has_issues: Missing[bool] = Field(
        default=UNSET, description="Whether issues are enabled."
    )
    has_projects: Missing[bool] = Field(
        default=UNSET, description="Whether projects are enabled."
    )
    has_wiki: Missing[bool] = Field(
        default=UNSET, description="Whether the wiki is enabled."
    )
    has_discussions: Missing[bool] = Field(
        default=UNSET, description="Whether discussions are enabled."
    )
    team_id: Missing[int] = Field(
        default=UNSET,
        description="The id of the team that will be granted access to this repository. This is only valid when creating a repository in an organization.",
    )
    auto_init: Missing[bool] = Field(
        default=UNSET,
        description="Whether the repository is initialized with a minimal README.",
    )
    gitignore_template: Missing[str] = Field(
        default=UNSET,
        description="The desired language or platform to apply to the .gitignore.",
    )
    license_template: Missing[str] = Field(
        default=UNSET,
        description="The license keyword of the open source license for this repository.",
    )
    allow_squash_merge: Missing[bool] = Field(
        default=UNSET, description="Whether to allow squash merges for pull requests."
    )
    allow_merge_commit: Missing[bool] = Field(
        default=UNSET, description="Whether to allow merge commits for pull requests."
    )
    allow_rebase_merge: Missing[bool] = Field(
        default=UNSET, description="Whether to allow rebase merges for pull requests."
    )
    allow_auto_merge: Missing[bool] = Field(
        default=UNSET,
        description="Whether to allow Auto-merge to be used on pull requests.",
    )
    delete_branch_on_merge: Missing[bool] = Field(
        default=UNSET,
        description="Whether to delete head branches when pull requests are merged",
    )
    squash_merge_commit_title: Missing[
        Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]
    ] = Field(
        default=UNSET,
        description="The default value for a squash merge commit title:\n\n- `PR_TITLE` - default to the pull request's title.\n- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit).",
    )
    squash_merge_commit_message: Missing[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ] = Field(
        default=UNSET,
        description="The default value for a squash merge commit message:\n\n- `PR_BODY` - default to the pull request's body.\n- `COMMIT_MESSAGES` - default to the branch's commit messages.\n- `BLANK` - default to a blank commit message.",
    )
    merge_commit_title: Missing[Literal["PR_TITLE", "MERGE_MESSAGE"]] = Field(
        default=UNSET,
        description="The default value for a merge commit title.\n\n- `PR_TITLE` - default to the pull request's title.\n- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).",
    )
    merge_commit_message: Missing[Literal["PR_BODY", "PR_TITLE", "BLANK"]] = Field(
        default=UNSET,
        description="The default value for a merge commit message.\n\n- `PR_TITLE` - default to the pull request's title.\n- `PR_BODY` - default to the pull request's body.\n- `BLANK` - default to a blank commit message.",
    )
    has_downloads: Missing[bool] = Field(
        default=UNSET, description="Whether downloads are enabled."
    )
    is_template: Missing[bool] = Field(
        default=UNSET,
        description="Whether this repository acts as a template that can be used to generate new repositories.",
    )


model_rebuild(UserReposPostBody)

__all__ = ("UserReposPostBody",)
