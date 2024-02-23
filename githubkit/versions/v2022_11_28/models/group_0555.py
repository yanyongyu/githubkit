"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0356 import EnterpriseWebhooks
from .group_0357 import SimpleInstallation
from .group_0358 import OrganizationSimpleWebhooks
from .group_0359 import RepositoryWebhooks
from .group_0360 import SimpleUserWebhooks


class WebhookLabelEdited(GitHubModel):
    """label edited event"""

    action: Literal["edited"] = Field()
    changes: Missing[WebhookLabelEditedPropChanges] = Field(
        default=UNSET,
        description="The changes to the label if the action was `edited`.",
    )
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
    label: WebhookLabelEditedPropLabel = Field(title="Label")
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


class WebhookLabelEditedPropLabel(GitHubModel):
    """Label"""

    color: str = Field(
        description="6-character hex code, without the leading #, identifying the color"
    )
    default: bool = Field()
    description: Union[str, None] = Field()
    id: int = Field()
    name: str = Field(description="The name of the label.")
    node_id: str = Field()
    url: str = Field(description="URL for the label")


class WebhookLabelEditedPropChanges(GitHubModel):
    """WebhookLabelEditedPropChanges

    The changes to the label if the action was `edited`.
    """

    color: Missing[WebhookLabelEditedPropChangesPropColor] = Field(default=UNSET)
    description: Missing[WebhookLabelEditedPropChangesPropDescription] = Field(
        default=UNSET
    )
    name: Missing[WebhookLabelEditedPropChangesPropName] = Field(default=UNSET)


class WebhookLabelEditedPropChangesPropColor(GitHubModel):
    """WebhookLabelEditedPropChangesPropColor"""

    from_: str = Field(
        alias="from",
        description="The previous version of the color if the action was `edited`.",
    )


class WebhookLabelEditedPropChangesPropDescription(GitHubModel):
    """WebhookLabelEditedPropChangesPropDescription"""

    from_: str = Field(
        alias="from",
        description="The previous version of the description if the action was `edited`.",
    )


class WebhookLabelEditedPropChangesPropName(GitHubModel):
    """WebhookLabelEditedPropChangesPropName"""

    from_: str = Field(
        alias="from",
        description="The previous version of the name if the action was `edited`.",
    )


model_rebuild(WebhookLabelEdited)
model_rebuild(WebhookLabelEditedPropLabel)
model_rebuild(WebhookLabelEditedPropChanges)
model_rebuild(WebhookLabelEditedPropChangesPropColor)
model_rebuild(WebhookLabelEditedPropChangesPropDescription)
model_rebuild(WebhookLabelEditedPropChangesPropName)

__all__ = (
    "WebhookLabelEdited",
    "WebhookLabelEditedPropLabel",
    "WebhookLabelEditedPropChanges",
    "WebhookLabelEditedPropChangesPropColor",
    "WebhookLabelEditedPropChangesPropDescription",
    "WebhookLabelEditedPropChangesPropName",
)
