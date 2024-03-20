"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0267 import HookResponse


class WebhookPingPropHook(GitHubModel):
    """Webhook

    The webhook that is being pinged
    """

    active: bool = Field(
        description="Determines whether the hook is actually triggered for the events it subscribes to."
    )
    app_id: Missing[int] = Field(
        default=UNSET,
        description="Only included for GitHub Apps. When you register a new GitHub App, GitHub sends a ping event to the webhook URL you specified during registration. The GitHub App ID sent in this field is required for authenticating an app.",
    )
    config: WebhookPingPropHookPropConfig = Field()
    created_at: datetime = Field()
    deliveries_url: Missing[str] = Field(default=UNSET)
    events: List[str] = Field(
        description="Determines what events the hook is triggered for. Default: ['push']."
    )
    id: int = Field(description="Unique identifier of the webhook.")
    last_response: Missing[HookResponse] = Field(default=UNSET, title="Hook Response")
    name: Literal["web"] = Field(
        description="The type of webhook. The only valid value is 'web'."
    )
    ping_url: Missing[str] = Field(default=UNSET)
    test_url: Missing[str] = Field(default=UNSET)
    type: str = Field()
    updated_at: datetime = Field()
    url: Missing[str] = Field(default=UNSET)


class WebhookPingPropHookPropConfig(GitHubModel):
    """WebhookPingPropHookPropConfig"""

    content_type: Missing[str] = Field(
        default=UNSET,
        description="The media type used to serialize the payloads. Supported values include `json` and `form`. The default is `form`.",
    )
    insecure_ssl: Missing[Union[str, float]] = Field(default=UNSET)
    secret: Missing[str] = Field(
        default=UNSET,
        description="If provided, the `secret` will be used as the `key` to generate the HMAC hex digest value for [delivery signature headers](https://docs.github.com/enterprise-cloud@latest//webhooks/event-payloads/#delivery-headers).",
    )
    url: Missing[str] = Field(
        default=UNSET, description="The URL to which the payloads will be delivered."
    )


model_rebuild(WebhookPingPropHook)
model_rebuild(WebhookPingPropHookPropConfig)

__all__ = (
    "WebhookPingPropHook",
    "WebhookPingPropHookPropConfig",
)
