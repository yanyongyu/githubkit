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


class SearchResultTextMatchesItems(GitHubModel):
    """SearchResultTextMatchesItems"""

    object_url: Missing[str] = Field(default=UNSET)
    object_type: Missing[Union[str, None]] = Field(default=UNSET)
    property_: Missing[str] = Field(default=UNSET, alias="property")
    fragment: Missing[str] = Field(default=UNSET)
    matches: Missing[list[SearchResultTextMatchesItemsPropMatchesItems]] = Field(
        default=UNSET
    )


class SearchResultTextMatchesItemsPropMatchesItems(GitHubModel):
    """SearchResultTextMatchesItemsPropMatchesItems"""

    text: Missing[str] = Field(default=UNSET)
    indices: Missing[list[int]] = Field(default=UNSET)


model_rebuild(SearchResultTextMatchesItems)
model_rebuild(SearchResultTextMatchesItemsPropMatchesItems)

__all__ = (
    "SearchResultTextMatchesItems",
    "SearchResultTextMatchesItemsPropMatchesItems",
)
