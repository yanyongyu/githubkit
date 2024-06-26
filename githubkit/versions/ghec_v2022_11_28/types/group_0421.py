"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict


class WebhooksRepositoriesItemsType(TypedDict):
    """WebhooksRepositoriesItems"""

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


__all__ = ("WebhooksRepositoriesItemsType",)
