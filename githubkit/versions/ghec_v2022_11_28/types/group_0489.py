"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0255 import DependabotAlertType
from .group_0402 import EnterpriseWebhooksType
from .group_0403 import SimpleInstallationType
from .group_0405 import RepositoryWebhooksType
from .group_0406 import SimpleUserWebhooksType
from .group_0404 import OrganizationSimpleWebhooksType


class WebhookDependabotAlertAutoDismissedType(TypedDict):
    """Dependabot alert auto-dismissed event"""

    action: Literal["auto_dismissed"]
    alert: DependabotAlertType
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookDependabotAlertAutoDismissedType",)
