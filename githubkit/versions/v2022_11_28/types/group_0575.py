"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0384 import EnterpriseWebhooksType
from .group_0385 import SimpleInstallationType
from .group_0386 import OrganizationSimpleWebhooksType
from .group_0387 import RepositoryWebhooksType
from .group_0399 import WebhooksLabelType


class WebhookLabelEditedType(TypedDict):
    """label edited event"""

    action: Literal["edited"]
    changes: NotRequired[WebhookLabelEditedPropChangesType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    label: WebhooksLabelType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookLabelEditedPropChangesType(TypedDict):
    """WebhookLabelEditedPropChanges

    The changes to the label if the action was `edited`.
    """

    color: NotRequired[WebhookLabelEditedPropChangesPropColorType]
    description: NotRequired[WebhookLabelEditedPropChangesPropDescriptionType]
    name: NotRequired[WebhookLabelEditedPropChangesPropNameType]


class WebhookLabelEditedPropChangesPropColorType(TypedDict):
    """WebhookLabelEditedPropChangesPropColor"""

    from_: str


class WebhookLabelEditedPropChangesPropDescriptionType(TypedDict):
    """WebhookLabelEditedPropChangesPropDescription"""

    from_: str


class WebhookLabelEditedPropChangesPropNameType(TypedDict):
    """WebhookLabelEditedPropChangesPropName"""

    from_: str


__all__ = (
    "WebhookLabelEditedPropChangesPropColorType",
    "WebhookLabelEditedPropChangesPropDescriptionType",
    "WebhookLabelEditedPropChangesPropNameType",
    "WebhookLabelEditedPropChangesType",
    "WebhookLabelEditedType",
)
