"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0351 import EnterpriseWebhooksType
from .group_0352 import SimpleInstallationType
from .group_0354 import RepositoryWebhooksType
from .group_0355 import SimpleUserWebhooksType
from .group_0353 import OrganizationSimpleWebhooksType


class WebhookSponsorshipCancelledType(TypedDict):
    """sponsorship cancelled event"""

    action: Literal["cancelled"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType
    sponsorship: WebhookSponsorshipCancelledPropSponsorshipType


class WebhookSponsorshipCancelledPropSponsorshipType(TypedDict):
    """WebhookSponsorshipCancelledPropSponsorship"""

    created_at: str
    maintainer: NotRequired[
        WebhookSponsorshipCancelledPropSponsorshipPropMaintainerType
    ]
    node_id: str
    privacy_level: str
    sponsor: Union[WebhookSponsorshipCancelledPropSponsorshipPropSponsorType, None]
    sponsorable: Union[
        WebhookSponsorshipCancelledPropSponsorshipPropSponsorableType, None
    ]
    tier: WebhookSponsorshipCancelledPropSponsorshipPropTierType


class WebhookSponsorshipCancelledPropSponsorshipPropMaintainerType(TypedDict):
    """WebhookSponsorshipCancelledPropSponsorshipPropMaintainer"""

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


class WebhookSponsorshipCancelledPropSponsorshipPropSponsorType(TypedDict):
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


class WebhookSponsorshipCancelledPropSponsorshipPropSponsorableType(TypedDict):
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


class WebhookSponsorshipCancelledPropSponsorshipPropTierType(TypedDict):
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
    "WebhookSponsorshipCancelledType",
    "WebhookSponsorshipCancelledPropSponsorshipType",
    "WebhookSponsorshipCancelledPropSponsorshipPropMaintainerType",
    "WebhookSponsorshipCancelledPropSponsorshipPropSponsorType",
    "WebhookSponsorshipCancelledPropSponsorshipPropSponsorableType",
    "WebhookSponsorshipCancelledPropSponsorshipPropTierType",
)
