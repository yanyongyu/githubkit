"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0356 import EnterpriseWebhooks
from .group_0357 import SimpleInstallation
from .group_0358 import OrganizationSimpleWebhooks
from .group_0359 import RepositoryWebhooks
from .group_0360 import SimpleUserWebhooks
from .group_0520 import WebhookIssuesMilestonedPropIssue


class WebhookIssuesMilestoned(GitHubModel):
    """issues milestoned event"""

    action: Literal["milestoned"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    issue: WebhookIssuesMilestonedPropIssue = Field()
    milestone: WebhookIssuesMilestonedPropMilestone = Field(
        title="Milestone",
        description="A collection of related issues and pull requests.",
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
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookIssuesMilestonedPropMilestone(GitHubModel):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None] = Field()
    closed_issues: int = Field()
    created_at: datetime = Field()
    creator: Union[WebhookIssuesMilestonedPropMilestonePropCreator, None] = Field(
        title="User"
    )
    description: Union[str, None] = Field()
    due_on: Union[datetime, None] = Field()
    html_url: str = Field()
    id: int = Field()
    labels_url: str = Field()
    node_id: str = Field()
    number: int = Field(description="The number of the milestone.")
    open_issues: int = Field()
    state: Literal["open", "closed"] = Field(description="The state of the milestone.")
    title: str = Field(description="The title of the milestone.")
    updated_at: datetime = Field()
    url: str = Field()


class WebhookIssuesMilestonedPropMilestonePropCreator(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization", "Mannequin"]] = Field(
        default=UNSET
    )
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookIssuesMilestoned)
model_rebuild(WebhookIssuesMilestonedPropMilestone)
model_rebuild(WebhookIssuesMilestonedPropMilestonePropCreator)

__all__ = (
    "WebhookIssuesMilestoned",
    "WebhookIssuesMilestonedPropMilestone",
    "WebhookIssuesMilestonedPropMilestonePropCreator",
)
