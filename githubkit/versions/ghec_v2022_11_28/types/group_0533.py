"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0015 import InstallationType
from .group_0416 import WebhooksUserType
from .group_0402 import EnterpriseWebhooksType
from .group_0405 import RepositoryWebhooksType
from .group_0406 import SimpleUserWebhooksType
from .group_0404 import OrganizationSimpleWebhooksType
from .group_0422 import WebhooksRepositoriesAddedItemsType


class WebhookInstallationRepositoriesAddedType(TypedDict):
    """installation_repositories added event"""

    action: Literal["added"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: InstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repositories_added: List[WebhooksRepositoriesAddedItemsType]
    repositories_removed: List[
        WebhookInstallationRepositoriesAddedPropRepositoriesRemovedItemsType
    ]
    repository: NotRequired[RepositoryWebhooksType]
    repository_selection: Literal["all", "selected"]
    requester: Union[WebhooksUserType, None]
    sender: SimpleUserWebhooksType


class WebhookInstallationRepositoriesAddedPropRepositoriesRemovedItemsType(TypedDict):
    """WebhookInstallationRepositoriesAddedPropRepositoriesRemovedItems"""

    full_name: NotRequired[str]
    id: NotRequired[int]
    name: NotRequired[str]
    node_id: NotRequired[str]
    private: NotRequired[bool]


__all__ = (
    "WebhookInstallationRepositoriesAddedType",
    "WebhookInstallationRepositoriesAddedPropRepositoriesRemovedItemsType",
)
