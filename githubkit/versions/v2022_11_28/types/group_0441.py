"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0015 import InstallationType
from .group_0351 import EnterpriseWebhooksType
from .group_0354 import RepositoryWebhooksType
from .group_0355 import SimpleUserWebhooksType
from .group_0353 import OrganizationSimpleWebhooksType


class WebhookInstallationSuspendType(TypedDict):
    """installation suspend event"""

    action: Literal["suspend"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: InstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repositories: NotRequired[List[WebhookInstallationSuspendPropRepositoriesItemsType]]
    repository: NotRequired[RepositoryWebhooksType]
    requester: NotRequired[None]
    sender: SimpleUserWebhooksType


class WebhookInstallationSuspendPropRepositoriesItemsType(TypedDict):
    """WebhookInstallationSuspendPropRepositoriesItems"""

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


__all__ = (
    "WebhookInstallationSuspendType",
    "WebhookInstallationSuspendPropRepositoriesItemsType",
)
