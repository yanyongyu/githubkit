"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0357 import EnterpriseWebhooksType
from .group_0358 import SimpleInstallationType
from .group_0359 import OrganizationSimpleWebhooksType
from .group_0360 import RepositoryWebhooksType
from .group_0361 import SimpleUserWebhooksType


class WebhookProjectCreatedType(TypedDict):
    """project created event"""

    action: Literal["created"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project: WebhookProjectCreatedPropProjectType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType


class WebhookProjectCreatedPropProjectType(TypedDict):
    """Project"""

    body: Union[str, None]
    columns_url: str
    created_at: datetime
    creator: Union[WebhookProjectCreatedPropProjectPropCreatorType, None]
    html_url: str
    id: int
    name: str
    node_id: str
    number: int
    owner_url: str
    state: Literal["open", "closed"]
    updated_at: datetime
    url: str


class WebhookProjectCreatedPropProjectPropCreatorType(TypedDict):
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
    "WebhookProjectCreatedType",
    "WebhookProjectCreatedPropProjectType",
    "WebhookProjectCreatedPropProjectPropCreatorType",
)
