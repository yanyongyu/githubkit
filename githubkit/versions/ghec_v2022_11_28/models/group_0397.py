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


class Discussion(GitHubModel):
    """Discussion

    A Discussion in a repository.
    """

    active_lock_reason: Union[str, None] = Field()
    answer_chosen_at: Union[str, None] = Field()
    answer_chosen_by: Union[DiscussionPropAnswerChosenBy, None] = Field(title="User")
    answer_html_url: Union[str, None] = Field()
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
        title="AuthorAssociation",
        description="How the author is associated with the repository.",
    )
    body: str = Field()
    category: DiscussionPropCategory = Field()
    comments: int = Field()
    created_at: datetime = Field()
    html_url: str = Field()
    id: int = Field()
    locked: bool = Field()
    node_id: str = Field()
    number: int = Field()
    reactions: Missing[DiscussionPropReactions] = Field(
        default=UNSET, title="Reactions"
    )
    repository_url: str = Field()
    state: Literal["open", "closed", "locked", "converting", "transferring"] = Field(
        description="The current state of the discussion.\n`converting` means that the discussion is being converted from an issue.\n`transferring` means that the discussion is being transferred from another repository."
    )
    state_reason: Union[
        None, Literal["resolved", "outdated", "duplicate", "reopened"]
    ] = Field(description="The reason for the current state")
    timeline_url: Missing[str] = Field(default=UNSET)
    title: str = Field()
    updated_at: datetime = Field()
    user: Union[DiscussionPropUser, None] = Field(title="User")


class DiscussionPropAnswerChosenBy(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class DiscussionPropCategory(GitHubModel):
    """DiscussionPropCategory"""

    created_at: datetime = Field()
    description: str = Field()
    emoji: str = Field()
    id: int = Field()
    is_answerable: bool = Field()
    name: str = Field()
    node_id: Missing[str] = Field(default=UNSET)
    repository_id: int = Field()
    slug: str = Field()
    updated_at: str = Field()


class DiscussionPropReactions(GitHubModel):
    """Reactions"""

    plus_one: int = Field(alias="+1")
    minus_one: int = Field(alias="-1")
    confused: int = Field()
    eyes: int = Field()
    heart: int = Field()
    hooray: int = Field()
    laugh: int = Field()
    rocket: int = Field()
    total_count: int = Field()
    url: str = Field()


class DiscussionPropUser(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


model_rebuild(Discussion)
model_rebuild(DiscussionPropAnswerChosenBy)
model_rebuild(DiscussionPropCategory)
model_rebuild(DiscussionPropReactions)
model_rebuild(DiscussionPropUser)

__all__ = (
    "Discussion",
    "DiscussionPropAnswerChosenBy",
    "DiscussionPropCategory",
    "DiscussionPropReactions",
    "DiscussionPropUser",
)
