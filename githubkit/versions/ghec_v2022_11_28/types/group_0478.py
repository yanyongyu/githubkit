"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0015 import InstallationType
from .group_0390 import EnterpriseWebhooksType
from .group_0392 import OrganizationSimpleWebhooksType
from .group_0393 import RepositoryWebhooksType
from .group_0394 import SimpleUserWebhooksType


class WebhookInstallationRepositoriesAddedType(TypedDict):
    """installation_repositories added event"""

    action: Literal["added"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: InstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repositories_added: List[
        WebhookInstallationRepositoriesAddedPropRepositoriesAddedItemsType
    ]
    repositories_removed: List[
        WebhookInstallationRepositoriesAddedPropRepositoriesRemovedItemsType
    ]
    repository: NotRequired[RepositoryWebhooksType]
    repository_selection: Literal["all", "selected"]
    requester: Union[WebhookInstallationRepositoriesAddedPropRequesterType, None]
    sender: SimpleUserWebhooksType


class WebhookInstallationRepositoriesAddedPropRepositoriesAddedItemsType(TypedDict):
    """WebhookInstallationRepositoriesAddedPropRepositoriesAddedItems"""

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


class WebhookInstallationRepositoriesAddedPropRepositoriesRemovedItemsType(TypedDict):
    """WebhookInstallationRepositoriesAddedPropRepositoriesRemovedItems"""

    full_name: NotRequired[str]
    id: NotRequired[int]
    name: NotRequired[str]
    node_id: NotRequired[str]
    private: NotRequired[bool]


class WebhookInstallationRepositoriesAddedPropRequesterType(TypedDict):
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
    "WebhookInstallationRepositoriesAddedType",
    "WebhookInstallationRepositoriesAddedPropRepositoriesAddedItemsType",
    "WebhookInstallationRepositoriesAddedPropRepositoriesRemovedItemsType",
    "WebhookInstallationRepositoriesAddedPropRequesterType",
)
