"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0389 import EnterpriseWebhooksType
from .group_0390 import SimpleInstallationType
from .group_0391 import OrganizationSimpleWebhooksType
from .group_0392 import RepositoryWebhooksType
from .group_0393 import SimpleUserWebhooksType


class WebhookProjectEditedType(TypedDict):
    """project edited event"""

    action: Literal["edited"]
    changes: NotRequired[WebhookProjectEditedPropChangesType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project: WebhookProjectEditedPropProjectType
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserWebhooksType]


class WebhookProjectEditedPropChangesType(TypedDict):
    """WebhookProjectEditedPropChanges

    The changes to the project if the action was `edited`.
    """

    body: NotRequired[WebhookProjectEditedPropChangesPropBodyType]
    name: NotRequired[WebhookProjectEditedPropChangesPropNameType]


class WebhookProjectEditedPropChangesPropBodyType(TypedDict):
    """WebhookProjectEditedPropChangesPropBody"""

    from_: str


class WebhookProjectEditedPropChangesPropNameType(TypedDict):
    """WebhookProjectEditedPropChangesPropName"""

    from_: str


class WebhookProjectEditedPropProjectType(TypedDict):
    """Project"""

    body: Union[str, None]
    columns_url: str
    created_at: datetime
    creator: Union[WebhookProjectEditedPropProjectPropCreatorType, None]
    html_url: str
    id: int
    name: str
    node_id: str
    number: int
    owner_url: str
    state: Literal["open", "closed"]
    updated_at: datetime
    url: str


class WebhookProjectEditedPropProjectPropCreatorType(TypedDict):
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
    "WebhookProjectEditedType",
    "WebhookProjectEditedPropChangesType",
    "WebhookProjectEditedPropChangesPropBodyType",
    "WebhookProjectEditedPropChangesPropNameType",
    "WebhookProjectEditedPropProjectType",
    "WebhookProjectEditedPropProjectPropCreatorType",
)
