"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0010 import Integration
from .group_0071 import Team


class ReviewRequestedIssueEvent(GitHubModel):
    """Review Requested Issue Event

    Review Requested Issue Event
    """

    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    actor: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    event: Literal["review_requested"] = Field()
    commit_id: Union[str, None] = Field()
    commit_url: Union[str, None] = Field()
    created_at: str = Field()
    performed_via_github_app: Union[None, Integration, None] = Field()
    review_requester: SimpleUser = Field(
        title="Simple User", description="A GitHub user."
    )
    requested_team: Missing[Team] = Field(
        default=UNSET,
        title="Team",
        description="Groups of organization members that gives permissions on specified repositories.",
    )
    requested_reviewer: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )


model_rebuild(ReviewRequestedIssueEvent)

__all__ = ("ReviewRequestedIssueEvent",)
