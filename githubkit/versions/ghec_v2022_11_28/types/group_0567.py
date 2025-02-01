"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0454 import RepositoryWebhooksType
from .group_0466 import DiscussionType


class WebhookDiscussionTransferredPropChangesType(TypedDict):
    """WebhookDiscussionTransferredPropChanges"""

    new_discussion: DiscussionType
    new_repository: RepositoryWebhooksType


__all__ = ("WebhookDiscussionTransferredPropChangesType",)
