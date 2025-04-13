"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0418 import EnterpriseWebhooks
from .group_0419 import SimpleInstallation
from .group_0420 import OrganizationSimpleWebhooks
from .group_0421 import RepositoryWebhooks


class WebhookReleasePrereleased(GitHubModel):
    """release prereleased event"""

    action: Literal["prereleased"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    release: WebhookReleasePrereleasedPropRelease = Field(
        title="Release",
        description="The [release](https://docs.github.com/rest/releases/releases/#get-a-release) object.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )


class WebhookReleasePrereleasedPropRelease(GitHubModel):
    """Release

    The [release](https://docs.github.com/rest/releases/releases/#get-a-release)
    object.
    """

    assets: list[Union[WebhookReleasePrereleasedPropReleasePropAssetsItems, None]] = (
        Field()
    )
    assets_url: str = Field()
    author: Union[WebhookReleasePrereleasedPropReleasePropAuthor, None] = Field(
        title="User"
    )
    body: Union[str, None] = Field()
    created_at: Union[datetime, None] = Field()
    discussion_url: Missing[str] = Field(default=UNSET)
    draft: bool = Field(description="Whether the release is a draft or published")
    html_url: str = Field()
    id: int = Field()
    name: Union[str, None] = Field()
    node_id: str = Field()
    prerelease: Literal[True] = Field(
        description="Whether the release is identified as a prerelease or a full release."
    )
    published_at: Union[datetime, None] = Field()
    reactions: Missing[WebhookReleasePrereleasedPropReleasePropReactions] = Field(
        default=UNSET, title="Reactions"
    )
    tag_name: str = Field(description="The name of the tag.")
    tarball_url: Union[str, None] = Field()
    target_commitish: str = Field(
        description="Specifies the commitish value that determines where the Git tag is created from."
    )
    upload_url: str = Field()
    url: str = Field()
    zipball_url: Union[str, None] = Field()


class WebhookReleasePrereleasedPropReleasePropAssetsItems(GitHubModel):
    """Release Asset

    Data related to a release.
    """

    browser_download_url: str = Field()
    content_type: str = Field()
    created_at: datetime = Field()
    download_count: int = Field()
    id: int = Field()
    label: Union[str, None] = Field()
    name: str = Field(description="The file name of the asset.")
    node_id: str = Field()
    size: int = Field()
    state: Literal["uploaded"] = Field(description="State of the release asset.")
    updated_at: datetime = Field()
    uploader: Missing[
        Union[WebhookReleasePrereleasedPropReleasePropAssetsItemsPropUploader, None]
    ] = Field(default=UNSET, title="User")
    url: str = Field()


class WebhookReleasePrereleasedPropReleasePropAssetsItemsPropUploader(GitHubModel):
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


class WebhookReleasePrereleasedPropReleasePropAuthor(GitHubModel):
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


class WebhookReleasePrereleasedPropReleasePropReactions(GitHubModel):
    """Reactions"""

    plus_one: int = Field(alias="+1")
    minus_one: int = Field(alias="-1")
    confused: int = Field()
    eyes: int = Field()
    heart: int = Field()
    hooray: int = Field()
    laugh: int = Field()
    rocket: int = Field()
    total_count: int = Field()
    url: str = Field()


model_rebuild(WebhookReleasePrereleased)
model_rebuild(WebhookReleasePrereleasedPropRelease)
model_rebuild(WebhookReleasePrereleasedPropReleasePropAssetsItems)
model_rebuild(WebhookReleasePrereleasedPropReleasePropAssetsItemsPropUploader)
model_rebuild(WebhookReleasePrereleasedPropReleasePropAuthor)
model_rebuild(WebhookReleasePrereleasedPropReleasePropReactions)

__all__ = (
    "WebhookReleasePrereleased",
    "WebhookReleasePrereleasedPropRelease",
    "WebhookReleasePrereleasedPropReleasePropAssetsItems",
    "WebhookReleasePrereleasedPropReleasePropAssetsItemsPropUploader",
    "WebhookReleasePrereleasedPropReleasePropAuthor",
    "WebhookReleasePrereleasedPropReleasePropReactions",
)
