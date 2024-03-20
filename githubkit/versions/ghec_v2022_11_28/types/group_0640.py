"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0267 import HookResponseType


class WebhookPingPropHookType(TypedDict):
    """Webhook

    The webhook that is being pinged
    """

    active: bool
    app_id: NotRequired[int]
    config: WebhookPingPropHookPropConfigType
    created_at: datetime
    deliveries_url: NotRequired[str]
    events: List[str]
    id: int
    last_response: NotRequired[HookResponseType]
    name: Literal["web"]
    ping_url: NotRequired[str]
    test_url: NotRequired[str]
    type: str
    updated_at: datetime
    url: NotRequired[str]


class WebhookPingPropHookPropConfigType(TypedDict):
    """WebhookPingPropHookPropConfig"""

    content_type: NotRequired[str]
    insecure_ssl: NotRequired[Union[str, float]]
    secret: NotRequired[str]
    url: NotRequired[str]


__all__ = (
    "WebhookPingPropHookType",
    "WebhookPingPropHookPropConfigType",
)
