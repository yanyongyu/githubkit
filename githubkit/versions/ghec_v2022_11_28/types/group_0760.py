"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0153 import RepositoryRulesetType
from .group_0390 import EnterpriseWebhooksType
from .group_0391 import SimpleInstallationType
from .group_0392 import OrganizationSimpleWebhooksType
from .group_0393 import RepositoryWebhooksType
from .group_0394 import SimpleUserWebhooksType


class WebhookRepositoryRulesetCreatedType(TypedDict):
    """repository ruleset created event"""

    action: Literal["created"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    repository_ruleset: RepositoryRulesetType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookRepositoryRulesetCreatedType",)
