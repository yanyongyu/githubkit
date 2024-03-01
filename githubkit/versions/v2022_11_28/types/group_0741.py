"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0356 import EnterpriseWebhooksType
from .group_0357 import SimpleInstallationType
from .group_0359 import RepositoryWebhooksType
from .group_0360 import SimpleUserWebhooksType
from .group_0358 import OrganizationSimpleWebhooksType
from .group_0742 import WebhookRepositoryVulnerabilityAlertDismissPropAlertType


class WebhookRepositoryVulnerabilityAlertDismissType(TypedDict):
    """repository_vulnerability_alert dismiss event"""

    action: Literal["dismiss"]
    alert: WebhookRepositoryVulnerabilityAlertDismissPropAlertType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookRepositoryVulnerabilityAlertDismissType",)
