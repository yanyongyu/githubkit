"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0040 import MilestoneType
from .group_0385 import EnterpriseWebhooksType
from .group_0387 import OrganizationSimpleWebhooksType
from .group_0388 import RepositoryWebhooksType
from .group_0425 import WebhooksPullRequest5Type


class WebhookPullRequestMilestonedType(TypedDict):
    """pull_request milestoned event"""

    action: Literal["milestoned"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    milestone: NotRequired[MilestoneType]
    number: int
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: WebhooksPullRequest5Type
    repository: RepositoryWebhooksType
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookPullRequestMilestonedType",)
