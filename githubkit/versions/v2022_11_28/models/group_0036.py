"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0034 import Issue
from .group_0035 import IssueComment


class EventPropPayload(GitHubModel):
    """EventPropPayload"""

    action: Missing[str] = Field(default=UNSET)
    issue: Missing[Issue] = Field(
        default=UNSET,
        title="Issue",
        description="Issues are a great way to keep track of tasks, enhancements, and bugs for your projects.",
    )
    comment: Missing[IssueComment] = Field(
        default=UNSET,
        title="Issue Comment",
        description="Comments provide a way for people to collaborate on an issue.",
    )
    pages: Missing[List[EventPropPayloadPropPagesItems]] = Field(default=UNSET)


class EventPropPayloadPropPagesItems(GitHubModel):
    """EventPropPayloadPropPagesItems"""

    page_name: Missing[str] = Field(default=UNSET)
    title: Missing[str] = Field(default=UNSET)
    summary: Missing[Union[str, None]] = Field(default=UNSET)
    action: Missing[str] = Field(default=UNSET)
    sha: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)


class Event(GitHubModel):
    """Event

    Event
    """

    id: str = Field()
    type: Union[str, None] = Field()
    actor: Actor = Field(title="Actor", description="Actor")
    repo: EventPropRepo = Field()
    org: Missing[Actor] = Field(default=UNSET, title="Actor", description="Actor")
    payload: EventPropPayload = Field()
    public: bool = Field()
    created_at: Union[datetime, None] = Field()


class Actor(GitHubModel):
    """Actor

    Actor
    """

    id: int = Field()
    login: str = Field()
    display_login: Missing[str] = Field(default=UNSET)
    gravatar_id: Union[str, None] = Field()
    url: str = Field()
    avatar_url: str = Field()


class EventPropRepo(GitHubModel):
    """EventPropRepo"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


model_rebuild(EventPropPayload)
model_rebuild(EventPropPayloadPropPagesItems)
model_rebuild(Event)
model_rebuild(Actor)
model_rebuild(EventPropRepo)

__all__ = (
    "EventPropPayload",
    "EventPropPayloadPropPagesItems",
    "Event",
    "Actor",
    "EventPropRepo",
)
