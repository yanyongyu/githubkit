"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0005 import IntegrationType


class RenamedIssueEventType(TypedDict):
    """Renamed Issue Event

    Renamed Issue Event
    """

    id: int
    node_id: str
    url: str
    actor: SimpleUserType
    event: Literal["renamed"]
    commit_id: Union[str, None]
    commit_url: Union[str, None]
    created_at: str
    performed_via_github_app: Union[None, IntegrationType]
    rename: RenamedIssueEventPropRenameType


class RenamedIssueEventPropRenameType(TypedDict):
    """RenamedIssueEventPropRename"""

    from_: str
    to: str


__all__ = (
    "RenamedIssueEventType",
    "RenamedIssueEventPropRenameType",
)
