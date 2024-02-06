"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0355 import EnterpriseWebhooksType
from .group_0356 import SimpleInstallationType
from .group_0358 import RepositoryWebhooksType
from .group_0359 import SimpleUserWebhooksType
from .group_0357 import OrganizationSimpleWebhooksType


class WebhookProjectColumnEditedType(TypedDict):
    """project_column edited event"""

    action: Literal["edited"]
    changes: WebhookProjectColumnEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project_column: WebhookProjectColumnEditedPropProjectColumnType
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserWebhooksType]


class WebhookProjectColumnEditedPropProjectColumnType(TypedDict):
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


class WebhookProjectColumnEditedPropChangesType(TypedDict):
    """WebhookProjectColumnEditedPropChanges"""

    name: NotRequired[WebhookProjectColumnEditedPropChangesPropNameType]


class WebhookProjectColumnEditedPropChangesPropNameType(TypedDict):
    """WebhookProjectColumnEditedPropChangesPropName"""

    from_: str


__all__ = (
    "WebhookProjectColumnEditedType",
    "WebhookProjectColumnEditedPropProjectColumnType",
    "WebhookProjectColumnEditedPropChangesType",
    "WebhookProjectColumnEditedPropChangesPropNameType",
)
