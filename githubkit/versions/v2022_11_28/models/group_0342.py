"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0334 import SearchResultTextMatchesItems


class UserSearchResultItem(GitHubModel):
    """User Search Result Item

    User Search Result Item
    """

    login: str = Field()
    id: int = Field()
    node_id: str = Field()
    avatar_url: str = Field()
    gravatar_id: Union[str, None] = Field()
    url: str = Field()
    html_url: str = Field()
    followers_url: str = Field()
    subscriptions_url: str = Field()
    organizations_url: str = Field()
    repos_url: str = Field()
    received_events_url: str = Field()
    type: str = Field()
    score: float = Field()
    following_url: str = Field()
    gists_url: str = Field()
    starred_url: str = Field()
    events_url: str = Field()
    public_repos: Missing[int] = Field(default=UNSET)
    public_gists: Missing[int] = Field(default=UNSET)
    followers: Missing[int] = Field(default=UNSET)
    following: Missing[int] = Field(default=UNSET)
    created_at: Missing[datetime] = Field(default=UNSET)
    updated_at: Missing[datetime] = Field(default=UNSET)
    name: Missing[Union[str, None]] = Field(default=UNSET)
    bio: Missing[Union[str, None]] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    location: Missing[Union[str, None]] = Field(default=UNSET)
    site_admin: bool = Field()
    hireable: Missing[Union[bool, None]] = Field(default=UNSET)
    text_matches: Missing[List[SearchResultTextMatchesItems]] = Field(
        default=UNSET, title="Search Result Text Matches"
    )
    blog: Missing[Union[str, None]] = Field(default=UNSET)
    company: Missing[Union[str, None]] = Field(default=UNSET)
    suspended_at: Missing[Union[datetime, None]] = Field(default=UNSET)


class SearchUsersGetResponse200(GitHubModel):
    """SearchUsersGetResponse200"""

    total_count: int = Field()
    incomplete_results: bool = Field()
    items: List[UserSearchResultItem] = Field()


model_rebuild(UserSearchResultItem)
model_rebuild(SearchUsersGetResponse200)

__all__ = (
    "UserSearchResultItem",
    "SearchUsersGetResponse200",
)
