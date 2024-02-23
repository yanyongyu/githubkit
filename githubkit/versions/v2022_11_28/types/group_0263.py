"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict

from .group_0001 import SimpleUserType
from .group_0005 import IntegrationType


class LockedIssueEventType(TypedDict):
    """Locked Issue Event

    Locked Issue Event
    """

    id: int
    node_id: str
    url: str
    actor: SimpleUserType
    event: Literal["locked"]
    commit_id: Union[str, None]
    commit_url: Union[str, None]
    created_at: str
    performed_via_github_app: Union[None, IntegrationType]
    lock_reason: Union[str, None]


__all__ = ("LockedIssueEventType",)
