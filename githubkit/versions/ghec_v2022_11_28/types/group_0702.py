"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0451 import EnterpriseWebhooksType
from .group_0452 import SimpleInstallationType
from .group_0453 import OrganizationSimpleWebhooksType
from .group_0454 import RepositoryWebhooksType
from .group_0486 import WebhooksProjectColumnType


class WebhookProjectColumnDeletedType(TypedDict):
    """project_column deleted event"""

    action: Literal["deleted"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project_column: WebhooksProjectColumnType
    repository: NotRequired[Union[None, RepositoryWebhooksType]]
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookProjectColumnDeletedType",)
