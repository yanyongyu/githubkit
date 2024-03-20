"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0015 import InstallationType
from .group_0357 import EnterpriseWebhooksType
from .group_0360 import RepositoryWebhooksType
from .group_0361 import SimpleUserWebhooksType
from .group_0359 import OrganizationSimpleWebhooksType


class WebhookInstallationUnsuspendType(TypedDict):
    """installation unsuspend event"""

    action: Literal["unsuspend"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: InstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repositories: NotRequired[
        List[WebhookInstallationUnsuspendPropRepositoriesItemsType]
    ]
    repository: NotRequired[RepositoryWebhooksType]
    requester: NotRequired[None]
    sender: SimpleUserWebhooksType


class WebhookInstallationUnsuspendPropRepositoriesItemsType(TypedDict):
    """WebhookInstallationUnsuspendPropRepositoriesItems"""

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


__all__ = (
    "WebhookInstallationUnsuspendType",
    "WebhookInstallationUnsuspendPropRepositoriesItemsType",
)
