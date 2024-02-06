"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0015 import InstallationType
from .group_0355 import EnterpriseWebhooksType
from .group_0358 import RepositoryWebhooksType
from .group_0359 import SimpleUserWebhooksType
from .group_0357 import OrganizationSimpleWebhooksType


class WebhookInstallationRepositoriesRemovedType(TypedDict):
    """installation_repositories removed event"""

    action: Literal["removed"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: InstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repositories_added: List[
        WebhookInstallationRepositoriesRemovedPropRepositoriesAddedItemsType
    ]
    repositories_removed: List[
        WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItemsType
    ]
    repository: NotRequired[RepositoryWebhooksType]
    repository_selection: Literal["all", "selected"]
    requester: Union[WebhookInstallationRepositoriesRemovedPropRequesterType, None]
    sender: SimpleUserWebhooksType


class WebhookInstallationRepositoriesRemovedPropRepositoriesAddedItemsType(TypedDict):
    """WebhookInstallationRepositoriesRemovedPropRepositoriesAddedItems"""

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


class WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItemsType(TypedDict):
    """WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItems"""

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


class WebhookInstallationRepositoriesRemovedPropRequesterType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


__all__ = (
    "WebhookInstallationRepositoriesRemovedType",
    "WebhookInstallationRepositoriesRemovedPropRepositoriesAddedItemsType",
    "WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItemsType",
    "WebhookInstallationRepositoriesRemovedPropRequesterType",
)
