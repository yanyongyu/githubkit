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
from .group_0073 import Milestone
from .group_0427 import EnterpriseWebhooks
from .group_0429 import OrganizationSimpleWebhooks
from .group_0430 import RepositoryWebhooks
from .group_0469 import WebhooksPullRequest5


class WebhookPullRequestMilestoned(GitHubModel):
    """pull_request milestoned event"""

    action: Literal["milestoned"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."',
    )
    milestone: Missing[Milestone] = Field(
        default=UNSET,
        title="Milestone",
        description="A collection of related issues and pull requests.",
    )
    number: int = Field(description="The pull request number.")
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    pull_request: WebhooksPullRequest5 = Field(title="Pull Request")
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )


model_rebuild(WebhookPullRequestMilestoned)

__all__ = ("WebhookPullRequestMilestoned",)
