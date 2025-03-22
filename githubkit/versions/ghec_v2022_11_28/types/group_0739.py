"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0472 import EnterpriseWebhooksType
from .group_0473 import SimpleInstallationType
from .group_0474 import OrganizationSimpleWebhooksType
from .group_0475 import RepositoryWebhooksType
from .group_0506 import WebhooksProjectType


class WebhookProjectEditedType(TypedDict):
    """project edited event"""

    action: Literal["edited"]
    changes: NotRequired[WebhookProjectEditedPropChangesType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project: WebhooksProjectType
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserType]


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


__all__ = (
    "WebhookProjectEditedPropChangesPropBodyType",
    "WebhookProjectEditedPropChangesPropNameType",
    "WebhookProjectEditedPropChangesType",
    "WebhookProjectEditedType",
)
