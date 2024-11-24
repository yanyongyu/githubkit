"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict


class TimelineCommittedEventType(TypedDict):
    """Timeline Committed Event

    Timeline Committed Event
    """

    event: NotRequired[Literal["committed"]]
    sha: str
    node_id: str
    url: str
    author: TimelineCommittedEventPropAuthorType
    committer: TimelineCommittedEventPropCommitterType
    message: str
    tree: TimelineCommittedEventPropTreeType
    parents: list[TimelineCommittedEventPropParentsItemsType]
    verification: TimelineCommittedEventPropVerificationType
    html_url: str


class TimelineCommittedEventPropAuthorType(TypedDict):
    """TimelineCommittedEventPropAuthor

    Identifying information for the git-user
    """

    date: datetime
    email: str
    name: str


class TimelineCommittedEventPropCommitterType(TypedDict):
    """TimelineCommittedEventPropCommitter

    Identifying information for the git-user
    """

    date: datetime
    email: str
    name: str


class TimelineCommittedEventPropTreeType(TypedDict):
    """TimelineCommittedEventPropTree"""

    sha: str
    url: str


class TimelineCommittedEventPropParentsItemsType(TypedDict):
    """TimelineCommittedEventPropParentsItems"""

    sha: str
    url: str
    html_url: str


class TimelineCommittedEventPropVerificationType(TypedDict):
    """TimelineCommittedEventPropVerification"""

    verified: bool
    reason: str
    signature: Union[str, None]
    payload: Union[str, None]


__all__ = (
    "TimelineCommittedEventPropAuthorType",
    "TimelineCommittedEventPropCommitterType",
    "TimelineCommittedEventPropParentsItemsType",
    "TimelineCommittedEventPropTreeType",
    "TimelineCommittedEventPropVerificationType",
    "TimelineCommittedEventType",
)
