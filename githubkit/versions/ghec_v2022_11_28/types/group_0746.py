"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0402 import EnterpriseWebhooksType
from .group_0403 import SimpleInstallationType
from .group_0405 import RepositoryWebhooksType
from .group_0406 import SimpleUserWebhooksType
from .group_0451 import WebhooksSecurityAdvisoryType
from .group_0404 import OrganizationSimpleWebhooksType


class WebhookSecurityAdvisoryPublishedType(TypedDict):
    """security_advisory published event"""

    action: Literal["published"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    security_advisory: WebhooksSecurityAdvisoryType
    sender: NotRequired[SimpleUserWebhooksType]


__all__ = ("WebhookSecurityAdvisoryPublishedType",)
