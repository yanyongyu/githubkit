"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0390 import EnterpriseWebhooks
from .group_0391 import SimpleInstallation
from .group_0393 import RepositoryWebhooks
from .group_0394 import SimpleUserWebhooks
from .group_0392 import OrganizationSimpleWebhooks


class WebhookProjectCardMoved(GitHubModel):
    """project_card moved event"""

    action: Literal["moved"] = Field()
    changes: Missing[WebhookProjectCardMovedPropChanges] = Field(default=UNSET)
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    project_card: WebhookProjectCardMovedPropProjectCard = Field()
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookProjectCardMovedPropChanges(GitHubModel):
    """WebhookProjectCardMovedPropChanges"""

    column_id: WebhookProjectCardMovedPropChangesPropColumnId = Field()


class WebhookProjectCardMovedPropChangesPropColumnId(GitHubModel):
    """WebhookProjectCardMovedPropChangesPropColumnId"""

    from_: int = Field(alias="from")


class WebhookProjectCardMovedPropProjectCard(GitHubModel):
    """WebhookProjectCardMovedPropProjectCard"""

    after_id: Union[Union[int, None], None] = Field()
    archived: bool = Field(description="Whether or not the card is archived")
    column_id: int = Field()
    column_url: str = Field()
    content_url: Missing[str] = Field(default=UNSET)
    created_at: datetime = Field()
    creator: Union[WebhookProjectCardMovedPropProjectCardMergedCreator, None] = Field()
    id: int = Field(description="The project card's ID")
    node_id: str = Field()
    note: Union[Union[str, None], None] = Field()
    project_url: str = Field()
    updated_at: datetime = Field()
    url: str = Field()


class WebhookProjectCardMovedPropProjectCardMergedCreator(GitHubModel):
    """WebhookProjectCardMovedPropProjectCardMergedCreator"""

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


model_rebuild(WebhookProjectCardMoved)
model_rebuild(WebhookProjectCardMovedPropChanges)
model_rebuild(WebhookProjectCardMovedPropChangesPropColumnId)
model_rebuild(WebhookProjectCardMovedPropProjectCard)
model_rebuild(WebhookProjectCardMovedPropProjectCardMergedCreator)

__all__ = (
    "WebhookProjectCardMoved",
    "WebhookProjectCardMovedPropChanges",
    "WebhookProjectCardMovedPropChangesPropColumnId",
    "WebhookProjectCardMovedPropProjectCard",
    "WebhookProjectCardMovedPropProjectCardMergedCreator",
)
