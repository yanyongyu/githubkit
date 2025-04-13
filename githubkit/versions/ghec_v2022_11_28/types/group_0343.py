"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing_extensions import NotRequired, TypedDict

from .group_0011 import WebhookConfigType
from .group_0342 import HookResponseType


class HookType(TypedDict):
    """Webhook

    Webhooks for repositories.
    """

    type: str
    id: int
    name: str
    active: bool
    events: list[str]
    config: WebhookConfigType
    updated_at: datetime
    created_at: datetime
    url: str
    test_url: str
    ping_url: str
    deliveries_url: NotRequired[str]
    last_response: HookResponseType


__all__ = ("HookType",)
