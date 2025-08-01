"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0010 import IntegrationType
from .group_0086 import TeamType


class ReviewRequestRemovedIssueEventType(TypedDict):
    """Review Request Removed Issue Event

    Review Request Removed Issue Event
    """

    id: int
    node_id: str
    url: str
    actor: SimpleUserType
    event: Literal["review_request_removed"]
    commit_id: Union[str, None]
    commit_url: Union[str, None]
    created_at: str
    performed_via_github_app: Union[None, IntegrationType, None]
    review_requester: SimpleUserType
    requested_team: NotRequired[TeamType]
    requested_reviewer: NotRequired[SimpleUserType]


__all__ = ("ReviewRequestRemovedIssueEventType",)
