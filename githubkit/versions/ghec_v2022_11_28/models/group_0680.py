"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0681 import WebhookPackagePublishedPropPackagePropPackageVersion


class WebhookPackagePublishedPropPackage(GitHubModel):
    """WebhookPackagePublishedPropPackage

    Information about the package.
    """

    created_at: Union[str, None] = Field()
    description: Union[str, None] = Field()
    ecosystem: str = Field()
    html_url: str = Field()
    id: int = Field()
    name: str = Field()
    namespace: str = Field()
    owner: Union[WebhookPackagePublishedPropPackagePropOwner, None] = Field(
        title="User"
    )
    package_type: str = Field()
    package_version: Union[
        WebhookPackagePublishedPropPackagePropPackageVersion, None
    ] = Field()
    registry: Union[WebhookPackagePublishedPropPackagePropRegistry, None] = Field()
    updated_at: Union[str, None] = Field()


class WebhookPackagePublishedPropPackagePropOwner(GitHubModel):
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
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookPackagePublishedPropPackagePropRegistry(GitHubModel):
    """WebhookPackagePublishedPropPackagePropRegistry"""

    about_url: str = Field()
    name: str = Field()
    type: str = Field()
    url: str = Field()
    vendor: str = Field()


model_rebuild(WebhookPackagePublishedPropPackage)
model_rebuild(WebhookPackagePublishedPropPackagePropOwner)
model_rebuild(WebhookPackagePublishedPropPackagePropRegistry)

__all__ = (
    "WebhookPackagePublishedPropPackage",
    "WebhookPackagePublishedPropPackagePropOwner",
    "WebhookPackagePublishedPropPackagePropRegistry",
)
