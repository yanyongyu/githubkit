"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0020 import RepositoryType
from .group_0153 import IssueType
from .group_0473 import SimpleInstallationType
from .group_0474 import OrganizationSimpleWebhooksType
from .group_0475 import RepositoryWebhooksType


class WebhookSubIssuesParentIssueAddedType(TypedDict):
    """parent issue added event"""

    action: Literal["parent_issue_added"]
    parent_issue_id: float
    parent_issue: IssueType
    parent_issue_repo: RepositoryType
    sub_issue_id: float
    sub_issue: IssueType
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookSubIssuesParentIssueAddedType",)
