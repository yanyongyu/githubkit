"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class NotificationsThreadsThreadIdSubscriptionPutBody(GitHubModel):
    """NotificationsThreadsThreadIdSubscriptionPutBody"""

    ignored: Missing[bool] = Field(
        default=UNSET, description="Whether to block all notifications from a thread."
    )


model_rebuild(NotificationsThreadsThreadIdSubscriptionPutBody)

__all__ = ("NotificationsThreadsThreadIdSubscriptionPutBody",)
