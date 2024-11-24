"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0427 import EnterpriseWebhooksType
from .group_0428 import SimpleInstallationType
from .group_0429 import OrganizationSimpleWebhooksType
from .group_0430 import RepositoryWebhooksType
from .group_0461 import WebhooksProjectType


class WebhookProjectDeletedType(TypedDict):
    """project deleted event"""

    action: Literal["deleted"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project: WebhooksProjectType
    repository: NotRequired[Union[None, RepositoryWebhooksType]]
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookProjectDeletedType",)
