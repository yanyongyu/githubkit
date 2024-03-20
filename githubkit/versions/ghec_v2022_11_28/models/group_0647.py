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


class WebhookProjectCardMovedPropProjectCardAllof0(GitHubModel):
    """Project Card"""

    after_id: Missing[Union[int, None]] = Field(default=UNSET)
    archived: bool = Field(description="Whether or not the card is archived")
    column_id: int = Field()
    column_url: str = Field()
    content_url: Missing[str] = Field(default=UNSET)
    created_at: datetime = Field()
    creator: Union[
        WebhookProjectCardMovedPropProjectCardAllof0PropCreator, None
    ] = Field(title="User")
    id: int = Field(description="The project card's ID")
    node_id: str = Field()
    note: Union[str, None] = Field()
    project_url: str = Field()
    updated_at: datetime = Field()
    url: str = Field()


class WebhookProjectCardMovedPropProjectCardAllof0PropCreator(GitHubModel):
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
    type: Missing[Literal["Bot", "User", "Organization", "Mannequin"]] = Field(
        default=UNSET
    )
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookProjectCardMovedPropProjectCardAllof0)
model_rebuild(WebhookProjectCardMovedPropProjectCardAllof0PropCreator)

__all__ = (
    "WebhookProjectCardMovedPropProjectCardAllof0",
    "WebhookProjectCardMovedPropProjectCardAllof0PropCreator",
)
