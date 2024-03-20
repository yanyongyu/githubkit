"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0739 import WebhookReleasePublishedPropReleaseMergedAssets
from .group_0737 import WebhookReleasePublishedPropReleaseAllof0PropReactions


class WebhookReleasePublishedPropRelease(GitHubModel):
    """WebhookReleasePublishedPropRelease"""

    assets: List[WebhookReleasePublishedPropReleaseMergedAssets] = Field()
    assets_url: str = Field()
    author: WebhookReleasePublishedPropReleaseMergedAuthor = Field()
    body: Union[Union[str, None], None] = Field()
    created_at: datetime = Field()
    discussion_url: Missing[str] = Field(default=UNSET)
    draft: bool = Field(description="Whether the release is a draft or published")
    html_url: str = Field()
    id: int = Field()
    name: Union[Union[str, None], None] = Field()
    node_id: str = Field()
    prerelease: bool = Field(
        description="Whether the release is identified as a prerelease or a full release."
    )
    published_at: Union[Union[datetime, None], None] = Field()
    reactions: Missing[WebhookReleasePublishedPropReleaseAllof0PropReactions] = Field(
        default=UNSET, title="Reactions"
    )
    tag_name: str = Field(description="The name of the tag.")
    tarball_url: Union[Union[str, None], None] = Field()
    target_commitish: str = Field(
        description="Specifies the commitish value that determines where the Git tag is created from."
    )
    upload_url: str = Field()
    url: str = Field()
    zipball_url: Union[Union[str, None], None] = Field()


class WebhookReleasePublishedPropReleaseMergedAuthor(GitHubModel):
    """WebhookReleasePublishedPropReleaseMergedAuthor"""

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


model_rebuild(WebhookReleasePublishedPropRelease)
model_rebuild(WebhookReleasePublishedPropReleaseMergedAuthor)

__all__ = (
    "WebhookReleasePublishedPropRelease",
    "WebhookReleasePublishedPropReleaseMergedAuthor",
)