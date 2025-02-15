"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0160 import MinimalRepository
from .group_0250 import GitUser
from .group_0434 import SearchResultTextMatchesItems
from .group_0437 import CommitSearchResultItemPropCommit


class CommitSearchResultItem(GitHubModel):
    """Commit Search Result Item

    Commit Search Result Item
    """

    url: str = Field()
    sha: str = Field()
    html_url: str = Field()
    comments_url: str = Field()
    commit: CommitSearchResultItemPropCommit = Field()
    author: Union[None, SimpleUser] = Field()
    committer: Union[None, GitUser] = Field()
    parents: list[CommitSearchResultItemPropParentsItems] = Field()
    repository: MinimalRepository = Field(
        title="Minimal Repository", description="Minimal Repository"
    )
    score: float = Field()
    node_id: str = Field()
    text_matches: Missing[list[SearchResultTextMatchesItems]] = Field(
        default=UNSET, title="Search Result Text Matches"
    )


class CommitSearchResultItemPropParentsItems(GitHubModel):
    """CommitSearchResultItemPropParentsItems"""

    url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    sha: Missing[str] = Field(default=UNSET)


class SearchCommitsGetResponse200(GitHubModel):
    """SearchCommitsGetResponse200"""

    total_count: int = Field()
    incomplete_results: bool = Field()
    items: list[CommitSearchResultItem] = Field()


model_rebuild(CommitSearchResultItem)
model_rebuild(CommitSearchResultItemPropParentsItems)
model_rebuild(SearchCommitsGetResponse200)

__all__ = (
    "CommitSearchResultItem",
    "CommitSearchResultItemPropParentsItems",
    "SearchCommitsGetResponse200",
)
