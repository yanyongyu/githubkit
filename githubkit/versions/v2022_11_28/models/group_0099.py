"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0028 import TeamSimple


class UserRoleAssignment(GitHubModel):
    """A Role Assignment for a User

    The Relationship a User has with a role.
    """

    assignment: Missing[Literal["direct", "indirect", "mixed"]] = Field(
        default=UNSET,
        description="Determines if the user has a direct, indirect, or mixed relationship to a role",
    )
    inherited_from: Missing[list[TeamSimple]] = Field(
        default=UNSET, description="Team the user has gotten the role through"
    )
    name: Missing[Union[str, None]] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    login: str = Field()
    id: int = Field()
    node_id: str = Field()
    avatar_url: str = Field()
    gravatar_id: Union[str, None] = Field()
    url: str = Field()
    html_url: str = Field()
    followers_url: str = Field()
    following_url: str = Field()
    gists_url: str = Field()
    starred_url: str = Field()
    subscriptions_url: str = Field()
    organizations_url: str = Field()
    repos_url: str = Field()
    events_url: str = Field()
    received_events_url: str = Field()
    type: str = Field()
    site_admin: bool = Field()
    starred_at: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


model_rebuild(UserRoleAssignment)

__all__ = ("UserRoleAssignment",)
