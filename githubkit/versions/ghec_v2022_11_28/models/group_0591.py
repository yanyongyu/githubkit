"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0487 import EnterpriseWebhooks
from .group_0488 import SimpleInstallation
from .group_0489 import OrganizationSimpleWebhooks
from .group_0490 import RepositoryWebhooks
from .group_0502 import Discussion


class WebhookDiscussionCategoryChanged(GitHubModel):
    """discussion category changed event"""

    action: Literal["category_changed"] = Field()
    changes: WebhookDiscussionCategoryChangedPropChanges = Field()
    discussion: Discussion = Field(
        title="Discussion", description="A Discussion in a repository."
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


class WebhookDiscussionCategoryChangedPropChanges(GitHubModel):
    """WebhookDiscussionCategoryChangedPropChanges"""

    category: WebhookDiscussionCategoryChangedPropChangesPropCategory = Field()


class WebhookDiscussionCategoryChangedPropChangesPropCategory(GitHubModel):
    """WebhookDiscussionCategoryChangedPropChangesPropCategory"""

    from_: WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFrom = Field(
        alias="from"
    )


class WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFrom(GitHubModel):
    """WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFrom"""

    created_at: datetime = Field()
    description: str = Field()
    emoji: str = Field()
    id: int = Field()
    is_answerable: bool = Field()
    name: str = Field()
    node_id: Missing[str] = Field(default=UNSET)
    repository_id: int = Field()
    slug: str = Field()
    updated_at: str = Field()


model_rebuild(WebhookDiscussionCategoryChanged)
model_rebuild(WebhookDiscussionCategoryChangedPropChanges)
model_rebuild(WebhookDiscussionCategoryChangedPropChangesPropCategory)
model_rebuild(WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFrom)

__all__ = (
    "WebhookDiscussionCategoryChanged",
    "WebhookDiscussionCategoryChangedPropChanges",
    "WebhookDiscussionCategoryChangedPropChangesPropCategory",
    "WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFrom",
)
