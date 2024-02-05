"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0007 import WebhookConfig


class ReposOwnerRepoHooksHookIdPatchBody(GitHubModel):
    """ReposOwnerRepoHooksHookIdPatchBody"""

    config: Missing[WebhookConfig] = Field(
        default=UNSET,
        title="Webhook Configuration",
        description="Configuration object of the webhook",
    )
    events: Missing[List[str]] = Field(
        default=UNSET,
        description="Determines what [events](https://docs.github.com/webhooks/event-payloads) the hook is triggered for. This replaces the entire array of events.",
    )
    add_events: Missing[List[str]] = Field(
        default=UNSET,
        description="Determines a list of events to be added to the list of events that the Hook triggers for.",
    )
    remove_events: Missing[List[str]] = Field(
        default=UNSET,
        description="Determines a list of events to be removed from the list of events that the Hook triggers for.",
    )
    active: Missing[bool] = Field(
        default=UNSET,
        description="Determines if notifications are sent when the webhook is triggered. Set to `true` to send notifications.",
    )


model_rebuild(ReposOwnerRepoHooksHookIdPatchBody)

__all__ = ("ReposOwnerRepoHooksHookIdPatchBody",)
