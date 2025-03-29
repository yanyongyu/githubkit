"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Any, Literal, Union
from typing_extensions import NotRequired, TypeAlias, TypedDict

from .group_0712 import WebhookRubygemsMetadataType


class WebhookPackageUpdatedPropPackagePropPackageVersionType(TypedDict):
    """WebhookPackageUpdatedPropPackagePropPackageVersion"""

    author: Union[
        WebhookPackageUpdatedPropPackagePropPackageVersionPropAuthorType, None
    ]
    body: str
    body_html: str
    created_at: str
    description: str
    docker_metadata: NotRequired[
        list[
            WebhookPackageUpdatedPropPackagePropPackageVersionPropDockerMetadataItemsType
        ]
    ]
    draft: NotRequired[bool]
    html_url: str
    id: int
    installation_command: str
    manifest: NotRequired[str]
    metadata: list[
        WebhookPackageUpdatedPropPackagePropPackageVersionPropMetadataItemsType
    ]
    name: str
    package_files: list[
        WebhookPackageUpdatedPropPackagePropPackageVersionPropPackageFilesItemsType
    ]
    package_url: NotRequired[str]
    prerelease: NotRequired[bool]
    release: NotRequired[
        WebhookPackageUpdatedPropPackagePropPackageVersionPropReleaseType
    ]
    rubygems_metadata: NotRequired[list[WebhookRubygemsMetadataType]]
    source_url: NotRequired[str]
    summary: str
    tag_name: NotRequired[str]
    target_commitish: str
    target_oid: str
    updated_at: str
    version: str


class WebhookPackageUpdatedPropPackagePropPackageVersionPropAuthorType(TypedDict):
    """User"""

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
    user_view_type: NotRequired[str]


class WebhookPackageUpdatedPropPackagePropPackageVersionPropDockerMetadataItemsType(
    TypedDict
):
    """WebhookPackageUpdatedPropPackagePropPackageVersionPropDockerMetadataItems"""

    tags: NotRequired[list[str]]


WebhookPackageUpdatedPropPackagePropPackageVersionPropMetadataItemsType: TypeAlias = (
    dict[str, Any]
)
"""WebhookPackageUpdatedPropPackagePropPackageVersionPropMetadataItems
"""


class WebhookPackageUpdatedPropPackagePropPackageVersionPropPackageFilesItemsType(
    TypedDict
):
    """WebhookPackageUpdatedPropPackagePropPackageVersionPropPackageFilesItems"""

    content_type: str
    created_at: str
    download_url: str
    id: int
    md5: Union[str, None]
    name: str
    sha1: Union[str, None]
    sha256: str
    size: int
    state: str
    updated_at: str


class WebhookPackageUpdatedPropPackagePropPackageVersionPropReleaseType(TypedDict):
    """WebhookPackageUpdatedPropPackagePropPackageVersionPropRelease"""

    author: Union[
        WebhookPackageUpdatedPropPackagePropPackageVersionPropReleasePropAuthorType,
        None,
    ]
    created_at: str
    draft: bool
    html_url: str
    id: int
    name: str
    prerelease: bool
    published_at: str
    tag_name: str
    target_commitish: str
    url: str


class WebhookPackageUpdatedPropPackagePropPackageVersionPropReleasePropAuthorType(
    TypedDict
):
    """User"""

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
    user_view_type: NotRequired[str]


__all__ = (
    "WebhookPackageUpdatedPropPackagePropPackageVersionPropAuthorType",
    "WebhookPackageUpdatedPropPackagePropPackageVersionPropDockerMetadataItemsType",
    "WebhookPackageUpdatedPropPackagePropPackageVersionPropMetadataItemsType",
    "WebhookPackageUpdatedPropPackagePropPackageVersionPropPackageFilesItemsType",
    "WebhookPackageUpdatedPropPackagePropPackageVersionPropReleasePropAuthorType",
    "WebhookPackageUpdatedPropPackagePropPackageVersionPropReleaseType",
    "WebhookPackageUpdatedPropPackagePropPackageVersionType",
)
