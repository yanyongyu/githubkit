"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0471 import EnterpriseWebhooksType
from .group_0472 import SimpleInstallationType
from .group_0473 import OrganizationSimpleWebhooksType
from .group_0474 import RepositoryWebhooksType
from .group_0521 import WebhooksSponsorshipType


class WebhookSponsorshipEditedType(TypedDict):
    """sponsorship edited event"""

    action: Literal["edited"]
    changes: WebhookSponsorshipEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserType
    sponsorship: WebhooksSponsorshipType


class WebhookSponsorshipEditedPropChangesType(TypedDict):
    """WebhookSponsorshipEditedPropChanges"""

    privacy_level: NotRequired[WebhookSponsorshipEditedPropChangesPropPrivacyLevelType]


class WebhookSponsorshipEditedPropChangesPropPrivacyLevelType(TypedDict):
    """WebhookSponsorshipEditedPropChangesPropPrivacyLevel"""

    from_: str


__all__ = (
    "WebhookSponsorshipEditedPropChangesPropPrivacyLevelType",
    "WebhookSponsorshipEditedPropChangesType",
    "WebhookSponsorshipEditedType",
)
