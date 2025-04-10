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


class WebhookProjectCardMovedPropProjectCardAllof1(GitHubModel):
    """WebhookProjectCardMovedPropProjectCardAllof1"""

    after_id: Union[int, None] = Field()
    archived: Missing[bool] = Field(default=UNSET)
    column_id: Missing[int] = Field(default=UNSET)
    column_url: Missing[str] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    creator: Missing[
        Union[WebhookProjectCardMovedPropProjectCardAllof1PropCreator, None]
    ] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    note: Missing[Union[str, None]] = Field(default=UNSET)
    project_url: Missing[str] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookProjectCardMovedPropProjectCardAllof1PropCreator(GitHubModel):
    """WebhookProjectCardMovedPropProjectCardAllof1PropCreator"""

    avatar_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookProjectCardMovedPropProjectCardAllof1)
model_rebuild(WebhookProjectCardMovedPropProjectCardAllof1PropCreator)

__all__ = (
    "WebhookProjectCardMovedPropProjectCardAllof1",
    "WebhookProjectCardMovedPropProjectCardAllof1PropCreator",
)
