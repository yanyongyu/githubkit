"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0697 import WebhookReleasePrereleasedPropReleaseMergedAssetsType
from .group_0695 import WebhookReleasePrereleasedPropReleaseAllof0PropReactionsType


class WebhookReleasePrereleasedPropReleaseType(TypedDict):
    """WebhookReleasePrereleasedPropRelease"""

    assets: List[WebhookReleasePrereleasedPropReleaseMergedAssetsType]
    assets_url: str
    author: WebhookReleasePrereleasedPropReleaseMergedAuthorType
    body: Union[Union[str, None], None]
    created_at: datetime
    discussion_url: NotRequired[str]
    draft: bool
    html_url: str
    id: int
    name: Union[Union[str, None], None]
    node_id: str
    prerelease: Literal[True]
    published_at: Union[datetime, None]
    reactions: NotRequired[WebhookReleasePrereleasedPropReleaseAllof0PropReactionsType]
    tag_name: str
    tarball_url: Union[Union[str, None], None]
    target_commitish: str
    upload_url: str
    url: str
    zipball_url: Union[Union[str, None], None]


class WebhookReleasePrereleasedPropReleaseMergedAuthorType(TypedDict):
    """WebhookReleasePrereleasedPropReleaseMergedAuthor"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


__all__ = (
    "WebhookReleasePrereleasedPropReleaseType",
    "WebhookReleasePrereleasedPropReleaseMergedAuthorType",
)
