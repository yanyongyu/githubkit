"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0456 import EnterpriseWebhooksType
from .group_0457 import SimpleInstallationType
from .group_0458 import OrganizationSimpleWebhooksType
from .group_0459 import RepositoryWebhooksType


class WebhookPublicType(TypedDict):
    """public event"""

    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookPublicType",)
