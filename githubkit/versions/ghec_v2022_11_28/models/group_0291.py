"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class TimelineCommittedEvent(GitHubModel):
    """Timeline Committed Event

    Timeline Committed Event
    """

    event: Missing[Literal["committed"]] = Field(default=UNSET)
    sha: str = Field(description="SHA for the commit")
    node_id: str = Field()
    url: str = Field()
    author: TimelineCommittedEventPropAuthor = Field(
        description="Identifying information for the git-user"
    )
    committer: TimelineCommittedEventPropCommitter = Field(
        description="Identifying information for the git-user"
    )
    message: str = Field(description="Message describing the purpose of the commit")
    tree: TimelineCommittedEventPropTree = Field()
    parents: List[TimelineCommittedEventPropParentsItems] = Field()
    verification: TimelineCommittedEventPropVerification = Field()
    html_url: str = Field()


class TimelineCommittedEventPropAuthor(GitHubModel):
    """TimelineCommittedEventPropAuthor

    Identifying information for the git-user
    """

    date: datetime = Field(description="Timestamp of the commit")
    email: str = Field(description="Git email address of the user")
    name: str = Field(description="Name of the git user")


class TimelineCommittedEventPropCommitter(GitHubModel):
    """TimelineCommittedEventPropCommitter

    Identifying information for the git-user
    """

    date: datetime = Field(description="Timestamp of the commit")
    email: str = Field(description="Git email address of the user")
    name: str = Field(description="Name of the git user")


class TimelineCommittedEventPropTree(GitHubModel):
    """TimelineCommittedEventPropTree"""

    sha: str = Field(description="SHA for the commit")
    url: str = Field()


class TimelineCommittedEventPropParentsItems(GitHubModel):
    """TimelineCommittedEventPropParentsItems"""

    sha: str = Field(description="SHA for the commit")
    url: str = Field()
    html_url: str = Field()


class TimelineCommittedEventPropVerification(GitHubModel):
    """TimelineCommittedEventPropVerification"""

    verified: bool = Field()
    reason: str = Field()
    signature: Union[str, None] = Field()
    payload: Union[str, None] = Field()


model_rebuild(TimelineCommittedEvent)
model_rebuild(TimelineCommittedEventPropAuthor)
model_rebuild(TimelineCommittedEventPropCommitter)
model_rebuild(TimelineCommittedEventPropTree)
model_rebuild(TimelineCommittedEventPropParentsItems)
model_rebuild(TimelineCommittedEventPropVerification)

__all__ = (
    "TimelineCommittedEvent",
    "TimelineCommittedEventPropAuthor",
    "TimelineCommittedEventPropCommitter",
    "TimelineCommittedEventPropTree",
    "TimelineCommittedEventPropParentsItems",
    "TimelineCommittedEventPropVerification",
)
