"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0001 import SimpleUser
from .group_0033 import ReactionRollup


class TeamDiscussionComment(GitHubModel):
    """Team Discussion Comment

    A reply to a discussion within a team.
    """

    author: Union[None, SimpleUser] = Field()
    body: str = Field(description="The main text of the comment.")
    body_html: str = Field()
    body_version: str = Field(
        description="The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server."
    )
    created_at: datetime = Field()
    last_edited_at: Union[datetime, None] = Field()
    discussion_url: str = Field()
    html_url: str = Field()
    node_id: str = Field()
    number: int = Field(
        description="The unique sequence number of a team discussion comment."
    )
    updated_at: datetime = Field()
    url: str = Field()
    reactions: Missing[ReactionRollup] = Field(default=UNSET, title="Reaction Rollup")


model_rebuild(TeamDiscussionComment)

__all__ = ("TeamDiscussionComment",)
