"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0280 import DependabotAlertType
from .group_0427 import EnterpriseWebhooksType
from .group_0428 import SimpleInstallationType
from .group_0429 import OrganizationSimpleWebhooksType
from .group_0430 import RepositoryWebhooksType


class WebhookDependabotAlertDismissedType(TypedDict):
    """Dependabot alert dismissed event"""

    action: Literal["dismissed"]
    alert: DependabotAlertType
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookDependabotAlertDismissedType",)
