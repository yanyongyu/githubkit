"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from datetime import datetime
from typing_extensions import TypedDict, NotRequired


class ActionsCacheListType(TypedDict):
    """Repository actions caches

    Repository actions caches
    """

    total_count: int
    actions_caches: List[ActionsCacheListPropActionsCachesItemsType]


class ActionsCacheListPropActionsCachesItemsType(TypedDict):
    """ActionsCacheListPropActionsCachesItems"""

    id: NotRequired[int]
    ref: NotRequired[str]
    key: NotRequired[str]
    version: NotRequired[str]
    last_accessed_at: NotRequired[datetime]
    created_at: NotRequired[datetime]
    size_in_bytes: NotRequired[int]


__all__ = (
    "ActionsCacheListType",
    "ActionsCacheListPropActionsCachesItemsType",
)
