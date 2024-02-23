"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0389 import EnterpriseWebhooksType
from .group_0390 import SimpleInstallationType
from .group_0391 import OrganizationSimpleWebhooksType
from .group_0392 import RepositoryWebhooksType
from .group_0393 import SimpleUserWebhooksType


class WebhookSponsorshipPendingTierChangeType(TypedDict):
    """sponsorship pending_tier_change event"""

    action: Literal["pending_tier_change"]
    changes: WebhookSponsorshipPendingTierChangePropChangesType
    effective_date: NotRequired[str]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType
    sponsorship: WebhookSponsorshipPendingTierChangePropSponsorshipType


class WebhookSponsorshipPendingTierChangePropSponsorshipType(TypedDict):
    """WebhookSponsorshipPendingTierChangePropSponsorship"""

    created_at: str
    maintainer: NotRequired[
        WebhookSponsorshipPendingTierChangePropSponsorshipPropMaintainerType
    ]
    node_id: str
    privacy_level: str
    sponsor: Union[
        WebhookSponsorshipPendingTierChangePropSponsorshipPropSponsorType, None
    ]
    sponsorable: Union[
        WebhookSponsorshipPendingTierChangePropSponsorshipPropSponsorableType, None
    ]
    tier: WebhookSponsorshipPendingTierChangePropSponsorshipPropTierType


class WebhookSponsorshipPendingTierChangePropSponsorshipPropMaintainerType(TypedDict):
    """WebhookSponsorshipPendingTierChangePropSponsorshipPropMaintainer"""

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


class WebhookSponsorshipPendingTierChangePropSponsorshipPropSponsorType(TypedDict):
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


class WebhookSponsorshipPendingTierChangePropSponsorshipPropSponsorableType(TypedDict):
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


class WebhookSponsorshipPendingTierChangePropSponsorshipPropTierType(TypedDict):
    """Sponsorship Tier

    The `tier_changed` and `pending_tier_change` will include the original tier
    before the change or pending change. For more information, see the pending tier
    change payload.
    """

    created_at: str
    description: str
    is_custom_ammount: NotRequired[bool]
    is_custom_amount: NotRequired[bool]
    is_one_time: bool
    monthly_price_in_cents: int
    monthly_price_in_dollars: int
    name: str
    node_id: str


class WebhookSponsorshipPendingTierChangePropChangesType(TypedDict):
    """WebhookSponsorshipPendingTierChangePropChanges"""

    tier: WebhookSponsorshipPendingTierChangePropChangesPropTierType


class WebhookSponsorshipPendingTierChangePropChangesPropTierType(TypedDict):
    """WebhookSponsorshipPendingTierChangePropChangesPropTier"""

    from_: WebhookSponsorshipPendingTierChangePropChangesPropTierPropFromType


class WebhookSponsorshipPendingTierChangePropChangesPropTierPropFromType(TypedDict):
    """Sponsorship Tier

    The `tier_changed` and `pending_tier_change` will include the original tier
    before the change or pending change. For more information, see the pending tier
    change payload.
    """

    created_at: str
    description: str
    is_custom_ammount: NotRequired[bool]
    is_custom_amount: NotRequired[bool]
    is_one_time: bool
    monthly_price_in_cents: int
    monthly_price_in_dollars: int
    name: str
    node_id: str


__all__ = (
    "WebhookSponsorshipPendingTierChangeType",
    "WebhookSponsorshipPendingTierChangePropSponsorshipType",
    "WebhookSponsorshipPendingTierChangePropSponsorshipPropMaintainerType",
    "WebhookSponsorshipPendingTierChangePropSponsorshipPropSponsorType",
    "WebhookSponsorshipPendingTierChangePropSponsorshipPropSponsorableType",
    "WebhookSponsorshipPendingTierChangePropSponsorshipPropTierType",
    "WebhookSponsorshipPendingTierChangePropChangesType",
    "WebhookSponsorshipPendingTierChangePropChangesPropTierType",
    "WebhookSponsorshipPendingTierChangePropChangesPropTierPropFromType",
)
