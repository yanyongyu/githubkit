"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0389 import EnterpriseWebhooksType
from .group_0390 import SimpleInstallationType
from .group_0391 import OrganizationSimpleWebhooksType
from .group_0392 import RepositoryWebhooksType
from .group_0393 import SimpleUserWebhooksType
from .group_0780 import WebhookRepositoryVulnerabilityAlertReopenPropAlertType


class WebhookRepositoryVulnerabilityAlertReopenType(TypedDict):
    """repository_vulnerability_alert reopen event"""

    action: Literal["reopen"]
    alert: WebhookRepositoryVulnerabilityAlertReopenPropAlertType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookRepositoryVulnerabilityAlertReopenType",)
