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
from .group_0397 import WebhooksAnswerType
from .group_0398 import DiscussionType


class WebhookDiscussionAnsweredType(TypedDict):
    """discussion answered event"""

    action: Literal["answered"]
    answer: WebhooksAnswerType
    discussion: DiscussionType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookDiscussionAnsweredType",)
