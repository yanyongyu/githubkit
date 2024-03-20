"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict, NotRequired


class SearchResultTextMatchesItemsType(TypedDict):
    """SearchResultTextMatchesItems"""

    object_url: NotRequired[str]
    object_type: NotRequired[Union[str, None]]
    property_: NotRequired[str]
    fragment: NotRequired[str]
    matches: NotRequired[List[SearchResultTextMatchesItemsPropMatchesItemsType]]


class SearchResultTextMatchesItemsPropMatchesItemsType(TypedDict):
    """SearchResultTextMatchesItemsPropMatchesItems"""

    text: NotRequired[str]
    indices: NotRequired[List[int]]


__all__ = (
    "SearchResultTextMatchesItemsType",
    "SearchResultTextMatchesItemsPropMatchesItemsType",
)
