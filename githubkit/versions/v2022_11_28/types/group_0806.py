"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0417 import EnterpriseWebhooksType
from .group_0418 import SimpleInstallationType
from .group_0419 import OrganizationSimpleWebhooksType
from .group_0420 import RepositoryWebhooksType


class WebhookWatchStartedType(TypedDict):
    """watch started event"""

    action: Literal["started"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookWatchStartedType",)
