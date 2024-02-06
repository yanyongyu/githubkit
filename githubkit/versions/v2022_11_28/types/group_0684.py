"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict

from .group_0685 import (
    WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionType,
)


class WebhookRegistryPackageUpdatedPropRegistryPackageType(TypedDict):
    """WebhookRegistryPackageUpdatedPropRegistryPackage"""

    created_at: str
    description: None
    ecosystem: str
    html_url: str
    id: int
    name: str
    namespace: str
    owner: WebhookRegistryPackageUpdatedPropRegistryPackagePropOwnerType
    package_type: str
    package_version: (
        WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionType
    )
    registry: Union[
        WebhookRegistryPackageUpdatedPropRegistryPackagePropRegistryType, None
    ]
    updated_at: str


class WebhookRegistryPackageUpdatedPropRegistryPackagePropOwnerType(TypedDict):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropOwner"""

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


class WebhookRegistryPackageUpdatedPropRegistryPackagePropRegistryType(TypedDict):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropRegistry"""


__all__ = (
    "WebhookRegistryPackageUpdatedPropRegistryPackageType",
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropOwnerType",
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropRegistryType",
)
