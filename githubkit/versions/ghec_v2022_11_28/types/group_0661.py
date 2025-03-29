"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0471 import EnterpriseWebhooksType
from .group_0472 import SimpleInstallationType
from .group_0473 import OrganizationSimpleWebhooksType
from .group_0474 import RepositoryWebhooksType
from .group_0488 import WebhooksLabelType
from .group_0662 import WebhookIssuesEditedPropIssueType


class WebhookIssuesEditedType(TypedDict):
    """issues edited event"""

    action: Literal["edited"]
    changes: WebhookIssuesEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    issue: WebhookIssuesEditedPropIssueType
    label: NotRequired[WebhooksLabelType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookIssuesEditedPropChangesType(TypedDict):
    """WebhookIssuesEditedPropChanges

    The changes to the issue.
    """

    body: NotRequired[WebhookIssuesEditedPropChangesPropBodyType]
    title: NotRequired[WebhookIssuesEditedPropChangesPropTitleType]


class WebhookIssuesEditedPropChangesPropBodyType(TypedDict):
    """WebhookIssuesEditedPropChangesPropBody"""

    from_: str


class WebhookIssuesEditedPropChangesPropTitleType(TypedDict):
    """WebhookIssuesEditedPropChangesPropTitle"""

    from_: str


__all__ = (
    "WebhookIssuesEditedPropChangesPropBodyType",
    "WebhookIssuesEditedPropChangesPropTitleType",
    "WebhookIssuesEditedPropChangesType",
    "WebhookIssuesEditedType",
)
