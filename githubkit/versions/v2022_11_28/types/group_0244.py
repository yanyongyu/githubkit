"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0243 import HookResponseType


class HookType(TypedDict):
    """Webhook

    Webhooks for repositories.
    """

    type: str
    id: int
    name: str
    active: bool
    events: List[str]
    config: HookPropConfigType
    updated_at: datetime
    created_at: datetime
    url: str
    test_url: str
    ping_url: str
    deliveries_url: NotRequired[str]
    last_response: HookResponseType


class HookPropConfigType(TypedDict):
    """HookPropConfig"""

    email: NotRequired[str]
    password: NotRequired[str]
    room: NotRequired[str]
    subdomain: NotRequired[str]
    url: NotRequired[str]
    insecure_ssl: NotRequired[Union[str, float]]
    content_type: NotRequired[str]
    digest: NotRequired[str]
    secret: NotRequired[str]
    token: NotRequired[str]


__all__ = (
    "HookType",
    "HookPropConfigType",
)
