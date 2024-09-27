"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0066 import MilestoneType
from .group_0415 import EnterpriseWebhooksType
from .group_0418 import RepositoryWebhooksType
from .group_0419 import SimpleUserWebhooksType
from .group_0458 import WebhooksPullRequest5Type
from .group_0417 import OrganizationSimpleWebhooksType


class WebhookPullRequestMilestonedType(TypedDict):
    """pull_request milestoned event"""

    action: Literal["milestoned"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    milestone: NotRequired[MilestoneType]
    number: int
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: WebhooksPullRequest5Type
    repository: RepositoryWebhooksType
    sender: NotRequired[SimpleUserWebhooksType]


__all__ = ("WebhookPullRequestMilestonedType",)
