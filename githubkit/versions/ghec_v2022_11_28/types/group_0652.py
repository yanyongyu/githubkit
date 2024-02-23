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


class WebhookProjectColumnMovedType(TypedDict):
    """project_column moved event"""

    action: Literal["moved"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project_column: WebhookProjectColumnMovedPropProjectColumnType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType


class WebhookProjectColumnMovedPropProjectColumnType(TypedDict):
    """Project Column"""

    after_id: NotRequired[Union[int, None]]
    cards_url: str
    created_at: datetime
    id: int
    name: str
    node_id: str
    project_url: str
    updated_at: datetime
    url: str


__all__ = (
    "WebhookProjectColumnMovedType",
    "WebhookProjectColumnMovedPropProjectColumnType",
)
