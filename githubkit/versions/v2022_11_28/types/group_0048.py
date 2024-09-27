"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict

from .group_0002 import SimpleUserType


class GistCommentType(TypedDict):
    """Gist Comment

    A comment made to a gist.
    """

    id: int
    node_id: str
    url: str
    body: str
    user: Union[None, SimpleUserType]
    created_at: datetime
    updated_at: datetime
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


__all__ = ("GistCommentType",)
