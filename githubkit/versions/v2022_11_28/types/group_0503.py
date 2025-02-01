"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0399 import EnterpriseWebhooksType
from .group_0400 import SimpleInstallationType
from .group_0401 import OrganizationSimpleWebhooksType
from .group_0402 import RepositoryWebhooksType
from .group_0412 import DiscussionType
from .group_0414 import WebhooksLabelType


class WebhookDiscussionLabeledType(TypedDict):
    """discussion labeled event"""

    action: Literal["labeled"]
    discussion: DiscussionType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    label: WebhooksLabelType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookDiscussionLabeledType",)
