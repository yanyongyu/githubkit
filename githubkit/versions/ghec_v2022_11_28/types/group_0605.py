"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0489 import OrganizationSimpleWebhooksType
from .group_0490 import RepositoryWebhooksType
from .group_0501 import WebhooksAnswerType
from .group_0502 import DiscussionType


class WebhookDiscussionUnansweredType(TypedDict):
    """discussion unanswered event"""

    action: Literal["unanswered"]
    discussion: DiscussionType
    old_answer: WebhooksAnswerType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookDiscussionUnansweredType",)
