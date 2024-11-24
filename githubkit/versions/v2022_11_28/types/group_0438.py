"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0385 import EnterpriseWebhooksType
from .group_0386 import SimpleInstallationType
from .group_0387 import OrganizationSimpleWebhooksType
from .group_0388 import RepositoryWebhooksType
from .group_0389 import WebhooksRuleType


class WebhookBranchProtectionRuleCreatedType(TypedDict):
    """branch protection rule created event"""

    action: Literal["created"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    rule: WebhooksRuleType
    sender: SimpleUserType


__all__ = ("WebhookBranchProtectionRuleCreatedType",)
