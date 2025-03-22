"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0791 import (
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionType,
)


class WebhookRegistryPackagePublishedPropRegistryPackageType(TypedDict):
    """WebhookRegistryPackagePublishedPropRegistryPackage"""

    created_at: Union[str, None]
    description: Union[str, None]
    ecosystem: str
    html_url: str
    id: int
    name: str
    namespace: str
    owner: WebhookRegistryPackagePublishedPropRegistryPackagePropOwnerType
    package_type: str
    package_version: Union[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionType, None
    ]
    registry: Union[
        WebhookRegistryPackagePublishedPropRegistryPackagePropRegistryType, None
    ]
    updated_at: Union[str, None]


class WebhookRegistryPackagePublishedPropRegistryPackagePropOwnerType(TypedDict):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropOwner"""

    avatar_url: str
    events_url: str
    followers_url: str
    following_url: str
    gists_url: str
    gravatar_id: str
    html_url: str
    id: int
    login: str
    node_id: str
    organizations_url: str
    received_events_url: str
    repos_url: str
    site_admin: bool
    starred_url: str
    subscriptions_url: str
    type: str
    url: str
    user_view_type: NotRequired[str]


class WebhookRegistryPackagePublishedPropRegistryPackagePropRegistryType(TypedDict):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropRegistry"""

    about_url: NotRequired[str]
    name: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]
    vendor: NotRequired[str]


__all__ = (
    "WebhookRegistryPackagePublishedPropRegistryPackagePropOwnerType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropRegistryType",
    "WebhookRegistryPackagePublishedPropRegistryPackageType",
)
