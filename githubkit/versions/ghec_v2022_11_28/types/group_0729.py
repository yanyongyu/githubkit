"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0730 import WebhookPackagePublishedPropPackagePropPackageVersionType


class WebhookPackagePublishedPropPackageType(TypedDict):
    """WebhookPackagePublishedPropPackage

    Information about the package.
    """

    created_at: Union[str, None]
    description: Union[str, None]
    ecosystem: str
    html_url: str
    id: int
    name: str
    namespace: str
    owner: Union[WebhookPackagePublishedPropPackagePropOwnerType, None]
    package_type: str
    package_version: Union[
        WebhookPackagePublishedPropPackagePropPackageVersionType, None
    ]
    registry: Union[WebhookPackagePublishedPropPackagePropRegistryType, None]
    updated_at: Union[str, None]


class WebhookPackagePublishedPropPackagePropOwnerType(TypedDict):
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


class WebhookPackagePublishedPropPackagePropRegistryType(TypedDict):
    """WebhookPackagePublishedPropPackagePropRegistry"""

    about_url: str
    name: str
    type: str
    url: str
    vendor: str


__all__ = (
    "WebhookPackagePublishedPropPackagePropOwnerType",
    "WebhookPackagePublishedPropPackagePropRegistryType",
    "WebhookPackagePublishedPropPackageType",
)
