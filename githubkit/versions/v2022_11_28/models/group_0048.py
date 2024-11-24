"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union

from pydantic import Field

from githubkit.compat import ExtraGitHubModel, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser
from .group_0047 import GistHistory, GistSimplePropForkOf


class GistSimple(GitHubModel):
    """Gist Simple

    Gist Simple
    """

    forks: Missing[Union[list[GistSimplePropForksItems], None]] = Field(default=UNSET)
    history: Missing[Union[list[GistHistory], None]] = Field(default=UNSET)
    fork_of: Missing[Union[GistSimplePropForkOf, None]] = Field(
        default=UNSET, title="Gist", description="Gist"
    )
    url: Missing[str] = Field(default=UNSET)
    forks_url: Missing[str] = Field(default=UNSET)
    commits_url: Missing[str] = Field(default=UNSET)
    id: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    git_pull_url: Missing[str] = Field(default=UNSET)
    git_push_url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    files: Missing[GistSimplePropFiles] = Field(default=UNSET)
    public: Missing[bool] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)
    description: Missing[Union[str, None]] = Field(default=UNSET)
    comments: Missing[int] = Field(default=UNSET)
    user: Missing[Union[str, None]] = Field(default=UNSET)
    comments_url: Missing[str] = Field(default=UNSET)
    owner: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )
    truncated: Missing[bool] = Field(default=UNSET)


class GistSimplePropFiles(ExtraGitHubModel):
    """GistSimplePropFiles"""


class GistSimplePropForksItems(GitHubModel):
    """GistSimplePropForksItems"""

    id: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user: Missing[PublicUser] = Field(
        default=UNSET, title="Public User", description="Public User"
    )
    created_at: Missing[datetime] = Field(default=UNSET)
    updated_at: Missing[datetime] = Field(default=UNSET)


class PublicUser(GitHubModel):
    """Public User

    Public User
    """

    login: str = Field()
    id: int = Field()
    user_view_type: Missing[str] = Field(default=UNSET)
    node_id: str = Field()
    avatar_url: str = Field()
    gravatar_id: Union[str, None] = Field()
    url: str = Field()
    html_url: str = Field()
    followers_url: str = Field()
    following_url: str = Field()
    gists_url: str = Field()
    starred_url: str = Field()
    subscriptions_url: str = Field()
    organizations_url: str = Field()
    repos_url: str = Field()
    events_url: str = Field()
    received_events_url: str = Field()
    type: str = Field()
    site_admin: bool = Field()
    name: Union[str, None] = Field()
    company: Union[str, None] = Field()
    blog: Union[str, None] = Field()
    location: Union[str, None] = Field()
    email: Union[str, None] = Field()
    notification_email: Missing[Union[str, None]] = Field(default=UNSET)
    hireable: Union[bool, None] = Field()
    bio: Union[str, None] = Field()
    twitter_username: Missing[Union[str, None]] = Field(default=UNSET)
    public_repos: int = Field()
    public_gists: int = Field()
    followers: int = Field()
    following: int = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    plan: Missing[PublicUserPropPlan] = Field(default=UNSET)
    private_gists: Missing[int] = Field(default=UNSET)
    total_private_repos: Missing[int] = Field(default=UNSET)
    owned_private_repos: Missing[int] = Field(default=UNSET)
    disk_usage: Missing[int] = Field(default=UNSET)
    collaborators: Missing[int] = Field(default=UNSET)


class PublicUserPropPlan(GitHubModel):
    """PublicUserPropPlan"""

    collaborators: int = Field()
    name: str = Field()
    space: int = Field()
    private_repos: int = Field()


model_rebuild(GistSimple)
model_rebuild(GistSimplePropFiles)
model_rebuild(GistSimplePropForksItems)
model_rebuild(PublicUser)
model_rebuild(PublicUserPropPlan)

__all__ = (
    "GistSimple",
    "GistSimplePropFiles",
    "GistSimplePropForksItems",
    "PublicUser",
    "PublicUserPropPlan",
)
