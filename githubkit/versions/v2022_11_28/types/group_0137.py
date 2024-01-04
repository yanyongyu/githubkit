"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0033 import ReactionRollupType


class TeamDiscussionCommentType(TypedDict):
    """Team Discussion Comment

    A reply to a discussion within a team.
    """

    author: Union[None, SimpleUserType]
    body: str
    body_html: str
    body_version: str
    created_at: datetime
    last_edited_at: Union[datetime, None]
    discussion_url: str
    html_url: str
    node_id: str
    number: int
    updated_at: datetime
    url: str
    reactions: NotRequired[ReactionRollupType]


__all__ = ("TeamDiscussionCommentType",)
