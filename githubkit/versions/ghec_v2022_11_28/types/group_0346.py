"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0010 import IntegrationType
from .group_0138 import ReactionRollupType


class TimelineCommentEventType(TypedDict):
    """Timeline Comment Event

    Timeline Comment Event
    """

    event: Literal["commented"]
    actor: SimpleUserType
    id: int
    node_id: str
    url: str
    body: NotRequired[str]
    body_text: NotRequired[str]
    body_html: NotRequired[str]
    html_url: str
    user: SimpleUserType
    created_at: datetime
    updated_at: datetime
    issue_url: str
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]
    performed_via_github_app: NotRequired[Union[None, IntegrationType, None]]
    reactions: NotRequired[ReactionRollupType]


__all__ = ("TimelineCommentEventType",)
