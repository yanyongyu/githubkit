"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0318 import DependabotAlertType
from .group_0471 import EnterpriseWebhooksType
from .group_0472 import SimpleInstallationType
from .group_0473 import OrganizationSimpleWebhooksType
from .group_0474 import RepositoryWebhooksType


class WebhookDependabotAlertFixedType(TypedDict):
    """Dependabot alert fixed event"""

    action: Literal["fixed"]
    alert: DependabotAlertType
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookDependabotAlertFixedType",)
