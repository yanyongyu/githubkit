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

from .group_0471 import (
    WebhookForkPropForkeeAllof0PropPermissions,
    WebhookForkPropForkeeAllof0PropCustomProperties,
)


class WebhookForkPropForkee(GitHubModel):
    """WebhookForkPropForkee

    The created [`repository`](https://docs.github.com/enterprise-
    cloud@latest//rest/repos/repos#get-a-repository) resource.
    """

    allow_auto_merge: Missing[bool] = Field(
        default=UNSET, description="Whether to allow auto-merge for pull requests."
    )
    allow_forking: Missing[bool] = Field(
        default=UNSET, description="Whether to allow private forks"
    )
    allow_merge_commit: Missing[bool] = Field(
        default=UNSET, description="Whether to allow merge commits for pull requests."
    )
    allow_rebase_merge: Missing[bool] = Field(
        default=UNSET, description="Whether to allow rebase merges for pull requests."
    )
    allow_squash_merge: Missing[bool] = Field(
        default=UNSET, description="Whether to allow squash merges for pull requests."
    )
    allow_update_branch: Missing[bool] = Field(default=UNSET)
    archive_url: str = Field()
    archived: bool = Field(
        default=False, description="Whether the repository is archived."
    )
    assignees_url: str = Field()
    blobs_url: str = Field()
    branches_url: str = Field()
    clone_url: str = Field()
    collaborators_url: str = Field()
    comments_url: str = Field()
    commits_url: str = Field()
    compare_url: str = Field()
    contents_url: str = Field()
    contributors_url: str = Field()
    created_at: datetime = Field()
    custom_properties: Missing[WebhookForkPropForkeeAllof0PropCustomProperties] = Field(
        default=UNSET,
        description="The custom properties that were defined for the repository. The keys are the custom property names, and the values are the corresponding custom property values.",
    )
    default_branch: str = Field(description="The default branch of the repository.")
    delete_branch_on_merge: Missing[bool] = Field(
        default=UNSET,
        description="Whether to delete head branches when pull requests are merged",
    )
    deployments_url: str = Field()
    description: Union[Union[str, None], None] = Field()
    disabled: Missing[bool] = Field(
        default=UNSET, description="Returns whether or not this repository is disabled."
    )
    downloads_url: str = Field()
    events_url: str = Field()
    fork: Literal[True] = Field()
    forks: int = Field()
    forks_count: int = Field()
    forks_url: str = Field()
    full_name: str = Field()
    git_commits_url: str = Field()
    git_refs_url: str = Field()
    git_tags_url: str = Field()
    git_url: str = Field()
    has_downloads: bool = Field(
        default=True, description="Whether downloads are enabled."
    )
    has_issues: bool = Field(default=True, description="Whether issues are enabled.")
    has_pages: bool = Field()
    has_projects: bool = Field(
        default=True, description="Whether projects are enabled."
    )
    has_wiki: bool = Field(default=True, description="Whether the wiki is enabled.")
    homepage: Union[Union[str, None], None] = Field()
    hooks_url: str = Field()
    html_url: str = Field()
    id: int = Field(description="Unique identifier of the repository")
    is_template: Missing[bool] = Field(default=UNSET)
    issue_comment_url: str = Field()
    issue_events_url: str = Field()
    issues_url: str = Field()
    keys_url: str = Field()
    labels_url: str = Field()
    language: Union[None, None] = Field()
    languages_url: str = Field()
    license_: Union[WebhookForkPropForkeeMergedLicense, None] = Field(alias="license")
    master_branch: Missing[str] = Field(default=UNSET)
    merges_url: str = Field()
    milestones_url: str = Field()
    mirror_url: Union[None, None] = Field()
    name: str = Field(description="The name of the repository.")
    node_id: str = Field()
    notifications_url: str = Field()
    open_issues: int = Field()
    open_issues_count: int = Field()
    organization: Missing[str] = Field(default=UNSET)
    owner: WebhookForkPropForkeeMergedOwner = Field()
    permissions: Missing[WebhookForkPropForkeeAllof0PropPermissions] = Field(
        default=UNSET
    )
    private: bool = Field(description="Whether the repository is private or public.")
    public: Missing[bool] = Field(default=UNSET)
    pulls_url: str = Field()
    pushed_at: datetime = Field()
    releases_url: str = Field()
    role_name: Missing[Union[str, None]] = Field(default=UNSET)
    size: int = Field()
    ssh_url: str = Field()
    stargazers: Missing[int] = Field(default=UNSET)
    stargazers_count: int = Field()
    stargazers_url: str = Field()
    statuses_url: str = Field()
    subscribers_url: str = Field()
    subscription_url: str = Field()
    svn_url: str = Field()
    tags_url: str = Field()
    teams_url: str = Field()
    topics: List[str] = Field()
    trees_url: str = Field()
    updated_at: datetime = Field()
    url: str = Field()
    visibility: Literal["public", "private", "internal"] = Field()
    watchers: int = Field()
    watchers_count: int = Field()
    web_commit_signoff_required: Missing[bool] = Field(
        default=UNSET,
        description="Whether to require contributors to sign off on web-based commits",
    )


class WebhookForkPropForkeeMergedLicense(GitHubModel):
    """WebhookForkPropForkeeMergedLicense"""

    key: str = Field()
    name: str = Field()
    node_id: str = Field()
    spdx_id: str = Field()
    url: Union[str, None] = Field()


class WebhookForkPropForkeeMergedOwner(GitHubModel):
    """WebhookForkPropForkeeMergedOwner"""

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


model_rebuild(WebhookForkPropForkee)
model_rebuild(WebhookForkPropForkeeMergedLicense)
model_rebuild(WebhookForkPropForkeeMergedOwner)

__all__ = (
    "WebhookForkPropForkee",
    "WebhookForkPropForkeeMergedLicense",
    "WebhookForkPropForkeeMergedOwner",
)
