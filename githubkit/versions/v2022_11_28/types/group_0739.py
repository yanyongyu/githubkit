"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0404 import EnterpriseWebhooksType
from .group_0405 import SimpleInstallationType
from .group_0406 import OrganizationSimpleWebhooksType
from .group_0407 import RepositoryWebhooksType
from .group_0449 import WebhooksAlertType


class WebhookRepositoryVulnerabilityAlertReopenType(TypedDict):
    """repository_vulnerability_alert reopen event"""

    action: Literal["reopen"]
    alert: WebhooksAlertType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookRepositoryVulnerabilityAlertReopenType",)
