"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import TypedDict

from .group_0003 import SimpleUserType
from .group_0010 import IntegrationType


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
    performed_via_github_app: Union[None, IntegrationType, None]
    rename: RenamedIssueEventPropRenameType


class RenamedIssueEventPropRenameType(TypedDict):
    """RenamedIssueEventPropRename"""

    from_: str
    to: str


__all__ = (
    "RenamedIssueEventPropRenameType",
    "RenamedIssueEventType",
)
