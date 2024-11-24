"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0091 import MinimalRepositoryType
from .group_0405 import SearchResultTextMatchesItemsType


class CodeSearchResultItemType(TypedDict):
    """Code Search Result Item

    Code Search Result Item
    """

    name: str
    path: str
    sha: str
    url: str
    git_url: str
    html_url: str
    repository: MinimalRepositoryType
    score: float
    file_size: NotRequired[int]
    language: NotRequired[Union[str, None]]
    last_modified_at: NotRequired[datetime]
    line_numbers: NotRequired[list[str]]
    text_matches: NotRequired[list[SearchResultTextMatchesItemsType]]


class SearchCodeGetResponse200Type(TypedDict):
    """SearchCodeGetResponse200"""

    total_count: int
    incomplete_results: bool
    items: list[CodeSearchResultItemType]


__all__ = (
    "CodeSearchResultItemType",
    "SearchCodeGetResponse200Type",
)
