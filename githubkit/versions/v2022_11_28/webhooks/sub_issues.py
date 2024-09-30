"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import Dict, Type, Union
from typing_extensions import Annotated, TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import (
    WebhookSubIssuesSubIssueAdded,
    WebhookSubIssuesSubIssueRemoved,
    WebhookSubIssuesParentIssueAdded,
    WebhookSubIssuesParentIssueRemoved,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookSubIssuesParentIssueAdded,
        WebhookSubIssuesParentIssueRemoved,
        WebhookSubIssuesSubIssueAdded,
        WebhookSubIssuesSubIssueRemoved,
    ],
    Field(discriminator="action"),
]

SubIssuesEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "parent_issue_added": WebhookSubIssuesParentIssueAdded,
    "parent_issue_removed": WebhookSubIssuesParentIssueRemoved,
    "sub_issue_added": WebhookSubIssuesSubIssueAdded,
    "sub_issue_removed": WebhookSubIssuesSubIssueRemoved,
}

sub_issues_action_types = action_types

__all__ = ("Event", "SubIssuesEvent", "action_types", "sub_issues_action_types")