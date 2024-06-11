"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0453 import WebhooksChanges8Type
from .group_0402 import EnterpriseWebhooksType
from .group_0403 import SimpleInstallationType
from .group_0405 import RepositoryWebhooksType
from .group_0406 import SimpleUserWebhooksType
from .group_0452 import WebhooksSponsorshipType
from .group_0404 import OrganizationSimpleWebhooksType


class WebhookSponsorshipTierChangedType(TypedDict):
    """sponsorship tier_changed event"""

    action: Literal["tier_changed"]
    changes: WebhooksChanges8Type
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType
    sponsorship: WebhooksSponsorshipType


__all__ = ("WebhookSponsorshipTierChangedType",)
