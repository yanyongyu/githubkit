"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0399 import EnterpriseWebhooksType
from .group_0400 import SimpleInstallationType
from .group_0401 import OrganizationSimpleWebhooksType
from .group_0402 import RepositoryWebhooksType


class WebhookMetaDeletedType(TypedDict):
    """meta deleted event"""

    action: Literal["deleted"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    hook: WebhookMetaDeletedPropHookType
    hook_id: int
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[Union[None, RepositoryWebhooksType]]
    sender: NotRequired[SimpleUserType]


class WebhookMetaDeletedPropHookType(TypedDict):
    """WebhookMetaDeletedPropHook

    The modified webhook. This will contain different keys based on the type of
    webhook it is: repository, organization, business, app, or GitHub Marketplace.
    """

    active: bool
    config: WebhookMetaDeletedPropHookPropConfigType
    created_at: str
    events: list[str]
    id: int
    name: str
    type: str
    updated_at: str


class WebhookMetaDeletedPropHookPropConfigType(TypedDict):
    """WebhookMetaDeletedPropHookPropConfig"""

    content_type: Literal["json", "form"]
    insecure_ssl: str
    secret: NotRequired[str]
    url: str


__all__ = (
    "WebhookMetaDeletedPropHookPropConfigType",
    "WebhookMetaDeletedPropHookType",
    "WebhookMetaDeletedType",
)
