"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from typing import Dict, Type, Union
from typing_extensions import Annotated, TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import (
    WebhookDiscussionCommentEdited,
    WebhookDiscussionCommentCreated,
    WebhookDiscussionCommentDeleted,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookDiscussionCommentCreated,
        WebhookDiscussionCommentDeleted,
        WebhookDiscussionCommentEdited,
    ],
    Field(discriminator="action"),
]

DiscussionCommentEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "created": WebhookDiscussionCommentCreated,
    "deleted": WebhookDiscussionCommentDeleted,
    "edited": WebhookDiscussionCommentEdited,
}

discussion_comment_action_types = action_types

__all__ = (
    "Event",
    "DiscussionCommentEvent",
    "action_types",
    "discussion_comment_action_types",
)
