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


class WebhooksTeam1(GitHubModel):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: Missing[bool] = Field(default=UNSET)
    description: Missing[Union[str, None]] = Field(
        default=UNSET, description="Description of the team"
    )
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field(description="Unique identifier of the team")
    members_url: Missing[str] = Field(default=UNSET)
    name: str = Field(description="Name of the team")
    node_id: Missing[str] = Field(default=UNSET)
    parent: Missing[Union[WebhooksTeam1PropParent, None]] = Field(default=UNSET)
    permission: Missing[str] = Field(
        default=UNSET,
        description="Permission that the team will have for its repositories",
    )
    privacy: Missing[Literal["open", "closed", "secret"]] = Field(default=UNSET)
    notification_setting: Missing[
        Literal["notifications_enabled", "notifications_disabled"]
    ] = Field(
        default=UNSET,
        description="Whether team members will receive notifications when their team is @mentioned",
    )
    repositories_url: Missing[str] = Field(default=UNSET)
    slug: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET, description="URL for the team")


class WebhooksTeam1PropParent(GitHubModel):
    """WebhooksTeam1PropParent"""

    description: Union[str, None] = Field(description="Description of the team")
    html_url: str = Field()
    id: int = Field(description="Unique identifier of the team")
    members_url: str = Field()
    name: str = Field(description="Name of the team")
    node_id: str = Field()
    permission: str = Field(
        description="Permission that the team will have for its repositories"
    )
    privacy: Literal["open", "closed", "secret"] = Field()
    notification_setting: Literal["notifications_enabled", "notifications_disabled"] = (
        Field(
            description="Whether team members will receive notifications when their team is @mentioned"
        )
    )
    repositories_url: str = Field()
    slug: str = Field()
    url: str = Field(description="URL for the team")


model_rebuild(WebhooksTeam1)
model_rebuild(WebhooksTeam1PropParent)

__all__ = (
    "WebhooksTeam1",
    "WebhooksTeam1PropParent",
)
