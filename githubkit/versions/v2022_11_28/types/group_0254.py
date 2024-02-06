"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict

from .group_0001 import SimpleUserType
from .group_0005 import IntegrationType


class AssignedIssueEventType(TypedDict):
    """Assigned Issue Event

    Assigned Issue Event
    """

    id: int
    node_id: str
    url: str
    actor: SimpleUserType
    event: str
    commit_id: Union[str, None]
    commit_url: Union[str, None]
    created_at: str
    performed_via_github_app: IntegrationType
    assignee: SimpleUserType
    assigner: SimpleUserType


__all__ = ("AssignedIssueEventType",)
