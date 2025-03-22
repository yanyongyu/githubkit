"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0221 import RepositoryAdvisoryType
from .group_0472 import EnterpriseWebhooksType
from .group_0473 import SimpleInstallationType
from .group_0474 import OrganizationSimpleWebhooksType
from .group_0475 import RepositoryWebhooksType


class WebhookRepositoryAdvisoryPublishedType(TypedDict):
    """Repository advisory published event"""

    action: Literal["published"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    repository_advisory: RepositoryAdvisoryType
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookRepositoryAdvisoryPublishedType",)
