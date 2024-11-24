"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import Annotated, Union
from typing_extensions import TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import (
    WebhookDiscussionAnswered,
    WebhookDiscussionCategoryChanged,
    WebhookDiscussionClosed,
    WebhookDiscussionCreated,
    WebhookDiscussionDeleted,
    WebhookDiscussionEdited,
    WebhookDiscussionLabeled,
    WebhookDiscussionLocked,
    WebhookDiscussionPinned,
    WebhookDiscussionReopened,
    WebhookDiscussionTransferred,
    WebhookDiscussionUnanswered,
    WebhookDiscussionUnlabeled,
    WebhookDiscussionUnlocked,
    WebhookDiscussionUnpinned,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookDiscussionAnswered,
        WebhookDiscussionCategoryChanged,
        WebhookDiscussionClosed,
        WebhookDiscussionCreated,
        WebhookDiscussionDeleted,
        WebhookDiscussionEdited,
        WebhookDiscussionLabeled,
        WebhookDiscussionLocked,
        WebhookDiscussionPinned,
        WebhookDiscussionReopened,
        WebhookDiscussionTransferred,
        WebhookDiscussionUnanswered,
        WebhookDiscussionUnlabeled,
        WebhookDiscussionUnlocked,
        WebhookDiscussionUnpinned,
    ],
    Field(discriminator="action"),
]

DiscussionEvent: TypeAlias = Event

action_types: dict[str, type[GitHubModel]] = {
    "answered": WebhookDiscussionAnswered,
    "category_changed": WebhookDiscussionCategoryChanged,
    "closed": WebhookDiscussionClosed,
    "created": WebhookDiscussionCreated,
    "deleted": WebhookDiscussionDeleted,
    "edited": WebhookDiscussionEdited,
    "labeled": WebhookDiscussionLabeled,
    "locked": WebhookDiscussionLocked,
    "pinned": WebhookDiscussionPinned,
    "reopened": WebhookDiscussionReopened,
    "transferred": WebhookDiscussionTransferred,
    "unanswered": WebhookDiscussionUnanswered,
    "unlabeled": WebhookDiscussionUnlabeled,
    "unlocked": WebhookDiscussionUnlocked,
    "unpinned": WebhookDiscussionUnpinned,
}

discussion_action_types = action_types

__all__ = ("DiscussionEvent", "Event", "action_types", "discussion_action_types")
