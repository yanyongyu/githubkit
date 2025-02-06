"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0010 import Integration
from .group_0138 import ReactionRollup


class TimelineCommentEvent(GitHubModel):
    """Timeline Comment Event

    Timeline Comment Event
    """

    event: Literal["commented"] = Field()
    actor: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    id: int = Field(description="Unique identifier of the issue comment")
    node_id: str = Field()
    url: str = Field(description="URL for the issue comment")
    body: Missing[str] = Field(
        default=UNSET, description="Contents of the issue comment"
    )
    body_text: Missing[str] = Field(default=UNSET)
    body_html: Missing[str] = Field(default=UNSET)
    html_url: str = Field()
    user: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    created_at: datetime = Field()
    updated_at: datetime = Field()
    issue_url: str = Field()
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ] = Field(
        title="author_association",
        description="How the author is associated with the repository.",
    )
    performed_via_github_app: Missing[Union[None, Integration, None]] = Field(
        default=UNSET
    )
    reactions: Missing[ReactionRollup] = Field(default=UNSET, title="Reaction Rollup")


model_rebuild(TimelineCommentEvent)

__all__ = ("TimelineCommentEvent",)
