"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0451 import EnterpriseWebhooksType
from .group_0452 import SimpleInstallationType
from .group_0453 import OrganizationSimpleWebhooksType
from .group_0454 import RepositoryWebhooksType
from .group_0491 import PullRequestWebhookType


class WebhookPullRequestConvertedToDraftType(TypedDict):
    """pull_request converted_to_draft event"""

    action: Literal["converted_to_draft"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    number: int
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: PullRequestWebhookType
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookPullRequestConvertedToDraftType",)
