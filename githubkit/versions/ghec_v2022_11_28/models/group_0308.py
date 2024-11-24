"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0002 import SimpleUser
from .group_0008 import Integration
from .group_0056 import Team
from .group_0075 import Issue


class IssueEvent(GitHubModel):
    """Issue Event

    Issue Event
    """

    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    actor: Union[None, SimpleUser] = Field()
    event: str = Field()
    commit_id: Union[str, None] = Field()
    commit_url: Union[str, None] = Field()
    created_at: datetime = Field()
    issue: Missing[Union[None, Issue]] = Field(default=UNSET)
    label: Missing[IssueEventLabel] = Field(
        default=UNSET, title="Issue Event Label", description="Issue Event Label"
    )
    assignee: Missing[Union[None, SimpleUser]] = Field(default=UNSET)
    assigner: Missing[Union[None, SimpleUser]] = Field(default=UNSET)
    review_requester: Missing[Union[None, SimpleUser]] = Field(default=UNSET)
    requested_reviewer: Missing[Union[None, SimpleUser]] = Field(default=UNSET)
    requested_team: Missing[Team] = Field(
        default=UNSET,
        title="Team",
        description="Groups of organization members that gives permissions on specified repositories.",
    )
    dismissed_review: Missing[IssueEventDismissedReview] = Field(
        default=UNSET, title="Issue Event Dismissed Review"
    )
    milestone: Missing[IssueEventMilestone] = Field(
        default=UNSET,
        title="Issue Event Milestone",
        description="Issue Event Milestone",
    )
    project_card: Missing[IssueEventProjectCard] = Field(
        default=UNSET,
        title="Issue Event Project Card",
        description="Issue Event Project Card",
    )
    rename: Missing[IssueEventRename] = Field(
        default=UNSET, title="Issue Event Rename", description="Issue Event Rename"
    )
    author_association: Missing[
        Literal[
            "COLLABORATOR",
            "CONTRIBUTOR",
            "FIRST_TIMER",
            "FIRST_TIME_CONTRIBUTOR",
            "MANNEQUIN",
            "MEMBER",
            "NONE",
            "OWNER",
        ]
    ] = Field(
        default=UNSET,
        title="author_association",
        description="How the author is associated with the repository.",
    )
    lock_reason: Missing[Union[str, None]] = Field(default=UNSET)
    performed_via_github_app: Missing[Union[None, Integration, None]] = Field(
        default=UNSET
    )


class IssueEventLabel(GitHubModel):
    """Issue Event Label

    Issue Event Label
    """

    name: Union[str, None] = Field()
    color: Union[str, None] = Field()


class IssueEventDismissedReview(GitHubModel):
    """Issue Event Dismissed Review"""

    state: str = Field()
    review_id: int = Field()
    dismissal_message: Union[str, None] = Field()
    dismissal_commit_id: Missing[Union[str, None]] = Field(default=UNSET)


class IssueEventMilestone(GitHubModel):
    """Issue Event Milestone

    Issue Event Milestone
    """

    title: str = Field()


class IssueEventProjectCard(GitHubModel):
    """Issue Event Project Card

    Issue Event Project Card
    """

    url: str = Field()
    id: int = Field()
    project_url: str = Field()
    project_id: int = Field()
    column_name: str = Field()
    previous_column_name: Missing[str] = Field(default=UNSET)


class IssueEventRename(GitHubModel):
    """Issue Event Rename

    Issue Event Rename
    """

    from_: str = Field(alias="from")
    to: str = Field()


model_rebuild(IssueEvent)
model_rebuild(IssueEventLabel)
model_rebuild(IssueEventDismissedReview)
model_rebuild(IssueEventMilestone)
model_rebuild(IssueEventProjectCard)
model_rebuild(IssueEventRename)

__all__ = (
    "IssueEvent",
    "IssueEventDismissedReview",
    "IssueEventLabel",
    "IssueEventMilestone",
    "IssueEventProjectCard",
    "IssueEventRename",
)
