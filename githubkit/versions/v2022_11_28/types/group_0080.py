"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from datetime import datetime
from typing_extensions import TypedDict, NotRequired


class OrgHookType(TypedDict):
    """Org Hook

    Org Hook
    """

    id: int
    url: str
    ping_url: str
    deliveries_url: NotRequired[str]
    name: str
    events: List[str]
    active: bool
    config: OrgHookPropConfigType
    updated_at: datetime
    created_at: datetime
    type: str


class OrgHookPropConfigType(TypedDict):
    """OrgHookPropConfig"""

    url: NotRequired[str]
    insecure_ssl: NotRequired[str]
    content_type: NotRequired[str]
    secret: NotRequired[str]


__all__ = (
    "OrgHookType",
    "OrgHookPropConfigType",
)
