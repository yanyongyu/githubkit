"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0357 import EnterpriseWebhooksType
from .group_0358 import SimpleInstallationType
from .group_0359 import OrganizationSimpleWebhooksType
from .group_0360 import RepositoryWebhooksType
from .group_0361 import SimpleUserWebhooksType
from .group_0369 import SecretScanningAlertWebhookType


class WebhookSecretScanningAlertReopenedType(TypedDict):
    """secret_scanning_alert reopened event"""

    action: Literal["reopened"]
    alert: SecretScanningAlertWebhookType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: NotRequired[SimpleUserWebhooksType]


__all__ = ("WebhookSecretScanningAlertReopenedType",)
