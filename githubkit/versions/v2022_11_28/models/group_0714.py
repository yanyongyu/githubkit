"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhookReleaseUnpublishedPropReleaseAllof1(GitHubModel):
    """WebhookReleaseUnpublishedPropReleaseAllof1"""

    assets: Missing[
        List[Union[WebhookReleaseUnpublishedPropReleaseAllof1PropAssetsItems, None]]
    ] = Field(default=UNSET)
    assets_url: Missing[str] = Field(default=UNSET)
    author: Missing[WebhookReleaseUnpublishedPropReleaseAllof1PropAuthor] = Field(
        default=UNSET
    )
    body: Missing[Union[str, None]] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    draft: Missing[bool] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    name: Missing[Union[str, None]] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    prerelease: Missing[bool] = Field(default=UNSET)
    published_at: Union[str, None] = Field()
    tag_name: Missing[str] = Field(default=UNSET)
    tarball_url: Missing[Union[str, None]] = Field(default=UNSET)
    target_commitish: Missing[str] = Field(default=UNSET)
    upload_url: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    zipball_url: Missing[Union[str, None]] = Field(default=UNSET)


class WebhookReleaseUnpublishedPropReleaseAllof1PropAssetsItems(GitHubModel):
    """WebhookReleaseUnpublishedPropReleaseAllof1PropAssetsItems"""


class WebhookReleaseUnpublishedPropReleaseAllof1PropAuthor(GitHubModel):
    """WebhookReleaseUnpublishedPropReleaseAllof1PropAuthor"""

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


model_rebuild(WebhookReleaseUnpublishedPropReleaseAllof1)
model_rebuild(WebhookReleaseUnpublishedPropReleaseAllof1PropAssetsItems)
model_rebuild(WebhookReleaseUnpublishedPropReleaseAllof1PropAuthor)

__all__ = (
    "WebhookReleaseUnpublishedPropReleaseAllof1",
    "WebhookReleaseUnpublishedPropReleaseAllof1PropAssetsItems",
    "WebhookReleaseUnpublishedPropReleaseAllof1PropAuthor",
)
