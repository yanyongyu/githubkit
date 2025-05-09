"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class RepositoryCollaboratorPermission(GitHubModel):
    """Repository Collaborator Permission

    Repository Collaborator Permission
    """

    permission: str = Field()
    role_name: str = Field()
    user: Union[None, Collaborator] = Field()


class Collaborator(GitHubModel):
    """Collaborator

    Collaborator
    """

    login: str = Field()
    id: int = Field()
    email: Missing[Union[str, None]] = Field(default=UNSET)
    name: Missing[Union[str, None]] = Field(default=UNSET)
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
    permissions: Missing[CollaboratorPropPermissions] = Field(default=UNSET)
    role_name: str = Field()
    user_view_type: Missing[str] = Field(default=UNSET)


class CollaboratorPropPermissions(GitHubModel):
    """CollaboratorPropPermissions"""

    pull: bool = Field()
    triage: Missing[bool] = Field(default=UNSET)
    push: bool = Field()
    maintain: Missing[bool] = Field(default=UNSET)
    admin: bool = Field()


model_rebuild(RepositoryCollaboratorPermission)
model_rebuild(Collaborator)
model_rebuild(CollaboratorPropPermissions)

__all__ = (
    "Collaborator",
    "CollaboratorPropPermissions",
    "RepositoryCollaboratorPermission",
)
