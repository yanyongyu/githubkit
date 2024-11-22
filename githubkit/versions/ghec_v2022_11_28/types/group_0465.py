"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType


class ProjectsV2ItemType(TypedDict):
    """Projects v2 Item

    An item belonging to a project
    """

    id: float
    node_id: NotRequired[str]
    project_node_id: NotRequired[str]
    content_node_id: str
    content_type: Literal["Issue", "PullRequest", "DraftIssue"]
    creator: NotRequired[SimpleUserType]
    created_at: datetime
    updated_at: datetime
    archived_at: Union[datetime, None]


__all__ = ("ProjectsV2ItemType",)
