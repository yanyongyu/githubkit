"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0351 import EnterpriseWebhooks
from .group_0352 import SimpleInstallation
from .group_0354 import RepositoryWebhooks
from .group_0355 import SimpleUserWebhooks
from .group_0353 import OrganizationSimpleWebhooks


class WebhookProjectCardConverted(GitHubModel):
    """project_card converted event"""

    action: Literal["converted"] = Field()
    changes: WebhookProjectCardConvertedPropChanges = Field()
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
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    project_card: WebhookProjectCardConvertedPropProjectCard = Field(
        title="Project Card"
    )
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookProjectCardConvertedPropChanges(GitHubModel):
    """WebhookProjectCardConvertedPropChanges"""

    note: WebhookProjectCardConvertedPropChangesPropNote = Field()


class WebhookProjectCardConvertedPropChangesPropNote(GitHubModel):
    """WebhookProjectCardConvertedPropChangesPropNote"""

    from_: str = Field(alias="from")


class WebhookProjectCardConvertedPropProjectCard(GitHubModel):
    """Project Card"""

    after_id: Missing[Union[int, None]] = Field(default=UNSET)
    archived: bool = Field(description="Whether or not the card is archived")
    column_id: int = Field()
    column_url: str = Field()
    content_url: Missing[str] = Field(default=UNSET)
    created_at: datetime = Field()
    creator: Union[WebhookProjectCardConvertedPropProjectCardPropCreator, None] = Field(
        title="User"
    )
    id: int = Field(description="The project card's ID")
    node_id: str = Field()
    note: Union[str, None] = Field()
    project_url: str = Field()
    updated_at: datetime = Field()
    url: str = Field()


class WebhookProjectCardConvertedPropProjectCardPropCreator(GitHubModel):
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
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookProjectCardConverted)
model_rebuild(WebhookProjectCardConvertedPropChanges)
model_rebuild(WebhookProjectCardConvertedPropChangesPropNote)
model_rebuild(WebhookProjectCardConvertedPropProjectCard)
model_rebuild(WebhookProjectCardConvertedPropProjectCardPropCreator)

__all__ = (
    "WebhookProjectCardConverted",
    "WebhookProjectCardConvertedPropChanges",
    "WebhookProjectCardConvertedPropChangesPropNote",
    "WebhookProjectCardConvertedPropProjectCard",
    "WebhookProjectCardConvertedPropProjectCardPropCreator",
)
