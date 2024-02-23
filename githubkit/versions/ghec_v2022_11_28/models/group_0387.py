"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class Hovercard(GitHubModel):
    """Hovercard

    Hovercard
    """

    contexts: List[HovercardPropContextsItems] = Field()


class HovercardPropContextsItems(GitHubModel):
    """HovercardPropContextsItems"""

    message: str = Field()
    octicon: str = Field()


model_rebuild(Hovercard)
model_rebuild(HovercardPropContextsItems)

__all__ = (
    "Hovercard",
    "HovercardPropContextsItems",
)
