"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict, NotRequired


class WebhookReleaseUnpublishedPropReleaseAllof1Type(TypedDict):
    """WebhookReleaseUnpublishedPropReleaseAllof1"""

    assets: NotRequired[
        List[Union[WebhookReleaseUnpublishedPropReleaseAllof1PropAssetsItemsType, None]]
    ]
    assets_url: NotRequired[str]
    author: NotRequired[WebhookReleaseUnpublishedPropReleaseAllof1PropAuthorType]
    body: NotRequired[Union[str, None]]
    created_at: NotRequired[str]
    draft: NotRequired[bool]
    html_url: NotRequired[str]
    id: NotRequired[int]
    name: NotRequired[Union[str, None]]
    node_id: NotRequired[str]
    prerelease: NotRequired[bool]
    published_at: Union[str, None]
    tag_name: NotRequired[str]
    tarball_url: NotRequired[Union[str, None]]
    target_commitish: NotRequired[str]
    upload_url: NotRequired[str]
    url: NotRequired[str]
    zipball_url: NotRequired[Union[str, None]]


class WebhookReleaseUnpublishedPropReleaseAllof1PropAssetsItemsType(TypedDict):
    """WebhookReleaseUnpublishedPropReleaseAllof1PropAssetsItems"""


class WebhookReleaseUnpublishedPropReleaseAllof1PropAuthorType(TypedDict):
    """WebhookReleaseUnpublishedPropReleaseAllof1PropAuthor"""

    avatar_url: NotRequired[str]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]


__all__ = (
    "WebhookReleaseUnpublishedPropReleaseAllof1Type",
    "WebhookReleaseUnpublishedPropReleaseAllof1PropAssetsItemsType",
    "WebhookReleaseUnpublishedPropReleaseAllof1PropAuthorType",
)
