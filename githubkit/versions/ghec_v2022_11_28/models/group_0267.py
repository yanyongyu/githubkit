"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0007 import WebhookConfig
from .group_0266 import HookResponse


class Hook(GitHubModel):
    """Webhook

    Webhooks for repositories.
    """

    type: str = Field()
    id: int = Field(description="Unique identifier of the webhook.")
    name: str = Field(
        description="The name of a valid service, use 'web' for a webhook."
    )
    active: bool = Field(
        description="Determines whether the hook is actually triggered on pushes."
    )
    events: List[str] = Field(
        description="Determines what events the hook is triggered for. Default: ['push']."
    )
    config: WebhookConfig = Field(
        title="Webhook Configuration", description="Configuration object of the webhook"
    )
    updated_at: datetime = Field()
    created_at: datetime = Field()
    url: str = Field()
    test_url: str = Field()
    ping_url: str = Field()
    deliveries_url: Missing[str] = Field(default=UNSET)
    last_response: HookResponse = Field(title="Hook Response")


model_rebuild(Hook)

__all__ = ("Hook",)
