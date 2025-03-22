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
from .group_0042 import IssueType
from .group_0419 import SimpleInstallationType
from .group_0420 import OrganizationSimpleWebhooksType
from .group_0421 import RepositoryWebhooksType


class WebhookSubIssuesSubIssueAddedType(TypedDict):
    """sub-issue added event"""

    action: Literal["sub_issue_added"]
    sub_issue_id: float
    sub_issue: IssueType
    sub_issue_repo: RepositoryType
    parent_issue_id: float
    parent_issue: IssueType
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookSubIssuesSubIssueAddedType",)
