"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0018 import InstallationType
from .group_0472 import EnterpriseWebhooksType
from .group_0474 import OrganizationSimpleWebhooksType
from .group_0475 import RepositoryWebhooksType
from .group_0490 import WebhooksRepositoriesItemsType


class WebhookInstallationDeletedType(TypedDict):
    """installation deleted event"""

    action: Literal["deleted"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: InstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repositories: NotRequired[list[WebhooksRepositoriesItemsType]]
    repository: NotRequired[RepositoryWebhooksType]
    requester: NotRequired[None]
    sender: SimpleUserType


__all__ = ("WebhookInstallationDeletedType",)
