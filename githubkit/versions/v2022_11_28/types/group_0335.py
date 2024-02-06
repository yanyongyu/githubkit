"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0177 import GitUserType
from .group_0001 import SimpleUserType
from .group_0050 import MinimalRepositoryType
from .group_0333 import SearchResultTextMatchesItemsType
from .group_0336 import CommitSearchResultItemPropCommitType


class CommitSearchResultItemType(TypedDict):
    """Commit Search Result Item

    Commit Search Result Item
    """

    url: str
    sha: str
    html_url: str
    comments_url: str
    commit: CommitSearchResultItemPropCommitType
    author: Union[None, SimpleUserType]
    committer: Union[None, GitUserType]
    parents: List[CommitSearchResultItemPropParentsItemsType]
    repository: MinimalRepositoryType
    score: float
    node_id: str
    text_matches: NotRequired[List[SearchResultTextMatchesItemsType]]


class CommitSearchResultItemPropParentsItemsType(TypedDict):
    """CommitSearchResultItemPropParentsItems"""

    url: NotRequired[str]
    html_url: NotRequired[str]
    sha: NotRequired[str]


class SearchCommitsGetResponse200Type(TypedDict):
    """SearchCommitsGetResponse200"""

    total_count: int
    incomplete_results: bool
    items: List[CommitSearchResultItemType]


__all__ = (
    "CommitSearchResultItemType",
    "CommitSearchResultItemPropParentsItemsType",
    "SearchCommitsGetResponse200Type",
)
