"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import TypedDict

from .group_0003 import SimpleUserType


class MilestoneType(TypedDict):
    """Milestone

    A collection of related issues and pull requests.
    """

    url: str
    html_url: str
    labels_url: str
    id: int
    node_id: str
    number: int
    state: Literal["open", "closed"]
    title: str
    description: Union[str, None]
    creator: Union[None, SimpleUserType]
    open_issues: int
    closed_issues: int
    created_at: datetime
    updated_at: datetime
    closed_at: Union[datetime, None]
    due_on: Union[datetime, None]


__all__ = ("MilestoneType",)
