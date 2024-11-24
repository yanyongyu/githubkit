"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0405 import SearchResultTextMatchesItemsType


class UserSearchResultItemType(TypedDict):
    """User Search Result Item

    User Search Result Item
    """

    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: Union[str, None]
    url: str
    html_url: str
    followers_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    received_events_url: str
    type: str
    score: float
    following_url: str
    gists_url: str
    starred_url: str
    events_url: str
    public_repos: NotRequired[int]
    public_gists: NotRequired[int]
    followers: NotRequired[int]
    following: NotRequired[int]
    created_at: NotRequired[datetime]
    updated_at: NotRequired[datetime]
    name: NotRequired[Union[str, None]]
    bio: NotRequired[Union[str, None]]
    email: NotRequired[Union[str, None]]
    location: NotRequired[Union[str, None]]
    site_admin: bool
    hireable: NotRequired[Union[bool, None]]
    text_matches: NotRequired[list[SearchResultTextMatchesItemsType]]
    blog: NotRequired[Union[str, None]]
    company: NotRequired[Union[str, None]]
    suspended_at: NotRequired[Union[datetime, None]]
    user_view_type: NotRequired[str]


class SearchUsersGetResponse200Type(TypedDict):
    """SearchUsersGetResponse200"""

    total_count: int
    incomplete_results: bool
    items: list[UserSearchResultItemType]


__all__ = (
    "SearchUsersGetResponse200Type",
    "UserSearchResultItemType",
)
