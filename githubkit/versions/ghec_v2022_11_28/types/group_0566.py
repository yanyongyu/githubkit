"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0456 import EnterpriseWebhooksType
from .group_0457 import SimpleInstallationType
from .group_0458 import OrganizationSimpleWebhooksType
from .group_0459 import RepositoryWebhooksType
from .group_0471 import DiscussionType


class WebhookDiscussionEditedType(TypedDict):
    """discussion edited event"""

    action: Literal["edited"]
    changes: NotRequired[WebhookDiscussionEditedPropChangesType]
    discussion: DiscussionType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookDiscussionEditedPropChangesType(TypedDict):
    """WebhookDiscussionEditedPropChanges"""

    body: NotRequired[WebhookDiscussionEditedPropChangesPropBodyType]
    title: NotRequired[WebhookDiscussionEditedPropChangesPropTitleType]


class WebhookDiscussionEditedPropChangesPropBodyType(TypedDict):
    """WebhookDiscussionEditedPropChangesPropBody"""

    from_: str


class WebhookDiscussionEditedPropChangesPropTitleType(TypedDict):
    """WebhookDiscussionEditedPropChangesPropTitle"""

    from_: str


__all__ = (
    "WebhookDiscussionEditedPropChangesPropBodyType",
    "WebhookDiscussionEditedPropChangesPropTitleType",
    "WebhookDiscussionEditedPropChangesType",
    "WebhookDiscussionEditedType",
)
