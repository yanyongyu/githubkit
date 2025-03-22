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

from .group_0003 import SimpleUser
from .group_0472 import EnterpriseWebhooks
from .group_0473 import SimpleInstallation
from .group_0474 import OrganizationSimpleWebhooks
from .group_0475 import RepositoryWebhooks
from .group_0492 import WebhooksIssueComment
from .group_0493 import WebhooksChanges
from .group_0634 import WebhookIssueCommentEditedPropIssue


class WebhookIssueCommentEdited(GitHubModel):
    """issue_comment edited event"""

    action: Literal["edited"] = Field()
    changes: WebhooksChanges = Field(description="The changes to the comment.")
    comment: WebhooksIssueComment = Field(
        title="issue comment",
        description="The [comment](https://docs.github.com/enterprise-cloud@latest//rest/issues/comments#get-an-issue-comment) itself.",
    )
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    issue: WebhookIssueCommentEditedPropIssue = Field(
        description="The [issue](https://docs.github.com/enterprise-cloud@latest//rest/issues/issues#get-an-issue) the comment belongs to."
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


model_rebuild(WebhookIssueCommentEdited)

__all__ = ("WebhookIssueCommentEdited",)
