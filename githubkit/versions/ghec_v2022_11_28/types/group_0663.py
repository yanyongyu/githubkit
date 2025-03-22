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
from .group_0489 import WebhooksLabelType
from .group_0664 import WebhookIssuesLabeledPropIssueType


class WebhookIssuesLabeledType(TypedDict):
    """issues labeled event"""

    action: Literal["labeled"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    issue: WebhookIssuesLabeledPropIssueType
    label: NotRequired[WebhooksLabelType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookIssuesLabeledType",)
