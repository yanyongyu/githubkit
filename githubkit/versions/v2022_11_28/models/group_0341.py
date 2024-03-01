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


class TopicSearchResultItem(GitHubModel):
    """Topic Search Result Item

    Topic Search Result Item
    """

    name: str = Field()
    display_name: Union[str, None] = Field()
    short_description: Union[str, None] = Field()
    description: Union[str, None] = Field()
    created_by: Union[str, None] = Field()
    released: Union[str, None] = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    featured: bool = Field()
    curated: bool = Field()
    score: float = Field()
    repository_count: Missing[Union[int, None]] = Field(default=UNSET)
    logo_url: Missing[Union[str, None]] = Field(default=UNSET)
    text_matches: Missing[List[SearchResultTextMatchesItems]] = Field(
        default=UNSET, title="Search Result Text Matches"
    )
    related: Missing[Union[List[TopicSearchResultItemPropRelatedItems], None]] = Field(
        default=UNSET
    )
    aliases: Missing[Union[List[TopicSearchResultItemPropAliasesItems], None]] = Field(
        default=UNSET
    )


class TopicSearchResultItemPropRelatedItems(GitHubModel):
    """TopicSearchResultItemPropRelatedItems"""

    topic_relation: Missing[TopicSearchResultItemPropRelatedItemsPropTopicRelation] = (
        Field(default=UNSET)
    )


class TopicSearchResultItemPropRelatedItemsPropTopicRelation(GitHubModel):
    """TopicSearchResultItemPropRelatedItemsPropTopicRelation"""

    id: Missing[int] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    topic_id: Missing[int] = Field(default=UNSET)
    relation_type: Missing[str] = Field(default=UNSET)


class TopicSearchResultItemPropAliasesItems(GitHubModel):
    """TopicSearchResultItemPropAliasesItems"""

    topic_relation: Missing[TopicSearchResultItemPropAliasesItemsPropTopicRelation] = (
        Field(default=UNSET)
    )


class TopicSearchResultItemPropAliasesItemsPropTopicRelation(GitHubModel):
    """TopicSearchResultItemPropAliasesItemsPropTopicRelation"""

    id: Missing[int] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    topic_id: Missing[int] = Field(default=UNSET)
    relation_type: Missing[str] = Field(default=UNSET)


class SearchTopicsGetResponse200(GitHubModel):
    """SearchTopicsGetResponse200"""

    total_count: int = Field()
    incomplete_results: bool = Field()
    items: List[TopicSearchResultItem] = Field()


model_rebuild(TopicSearchResultItem)
model_rebuild(TopicSearchResultItemPropRelatedItems)
model_rebuild(TopicSearchResultItemPropRelatedItemsPropTopicRelation)
model_rebuild(TopicSearchResultItemPropAliasesItems)
model_rebuild(TopicSearchResultItemPropAliasesItemsPropTopicRelation)
model_rebuild(SearchTopicsGetResponse200)

__all__ = (
    "TopicSearchResultItem",
    "TopicSearchResultItemPropRelatedItems",
    "TopicSearchResultItemPropRelatedItemsPropTopicRelation",
    "TopicSearchResultItemPropAliasesItems",
    "TopicSearchResultItemPropAliasesItemsPropTopicRelation",
    "SearchTopicsGetResponse200",
)
