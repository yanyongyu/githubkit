"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser
from .group_0019 import Repository
from .group_0042 import Issue
from .group_0386 import SimpleInstallation
from .group_0387 import OrganizationSimpleWebhooks
from .group_0388 import RepositoryWebhooks


class WebhookSubIssuesSubIssueRemoved(GitHubModel):
    """sub-issue removed event"""

    action: Literal["sub_issue_removed"] = Field()
    sub_issue_id: float = Field(description="The ID of the sub-issue.")
    sub_issue: Issue = Field(
        title="Issue",
        description="Issues are a great way to keep track of tasks, enhancements, and bugs for your projects.",
    )
    sub_issue_repo: Repository = Field(
        title="Repository", description="A repository on GitHub."
    )
    parent_issue_id: float = Field(description="The ID of the parent issue.")
    parent_issue: Issue = Field(
        title="Issue",
        description="Issues are a great way to keep track of tasks, enhancements, and bugs for your projects.",
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )


model_rebuild(WebhookSubIssuesSubIssueRemoved)

__all__ = ("WebhookSubIssuesSubIssueRemoved",)
