"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0402 import EnterpriseWebhooksType
from .group_0403 import SimpleInstallationType
from .group_0405 import RepositoryWebhooksType
from .group_0406 import SimpleUserWebhooksType
from .group_0442 import PullRequestWebhookType
from .group_0404 import OrganizationSimpleWebhooksType


class WebhookPullRequestReopenedType(TypedDict):
    """pull_request reopened event"""

    action: Literal["reopened"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    number: int
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: PullRequestWebhookType
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookPullRequestReopenedType",)
