"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0356 import EnterpriseWebhooksType
from .group_0357 import SimpleInstallationType
from .group_0358 import OrganizationSimpleWebhooksType
from .group_0359 import RepositoryWebhooksType
from .group_0360 import SimpleUserWebhooksType
from .group_0531 import WebhookIssuesReopenedPropIssueType


class WebhookIssuesReopenedType(TypedDict):
    """issues reopened event"""

    action: Literal["reopened"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    issue: WebhookIssuesReopenedPropIssueType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookIssuesReopenedType",)
