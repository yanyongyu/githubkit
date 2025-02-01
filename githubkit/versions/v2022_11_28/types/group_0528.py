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
from .group_0529 import WebhookIssueCommentCreatedPropCommentType
from .group_0530 import WebhookIssueCommentCreatedPropIssueType


class WebhookIssueCommentCreatedType(TypedDict):
    """issue_comment created event"""

    action: Literal["created"]
    comment: WebhookIssueCommentCreatedPropCommentType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    issue: WebhookIssueCommentCreatedPropIssueType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookIssueCommentCreatedType",)
