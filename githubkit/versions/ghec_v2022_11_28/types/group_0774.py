"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0467 import WebhooksChanges8Type
from .group_0415 import EnterpriseWebhooksType
from .group_0416 import SimpleInstallationType
from .group_0418 import RepositoryWebhooksType
from .group_0419 import SimpleUserWebhooksType
from .group_0466 import WebhooksSponsorshipType
from .group_0417 import OrganizationSimpleWebhooksType


class WebhookSponsorshipPendingTierChangeType(TypedDict):
    """sponsorship pending_tier_change event"""

    action: Literal["pending_tier_change"]
    changes: WebhooksChanges8Type
    effective_date: NotRequired[str]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType
    sponsorship: WebhooksSponsorshipType


__all__ = ("WebhookSponsorshipPendingTierChangeType",)
