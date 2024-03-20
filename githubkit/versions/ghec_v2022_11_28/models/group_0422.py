"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0390 import EnterpriseWebhooks
from .group_0391 import SimpleInstallation
from .group_0392 import OrganizationSimpleWebhooks
from .group_0393 import RepositoryWebhooks
from .group_0394 import SimpleUserWebhooks


class WebhookCodeScanningAlertFixed(GitHubModel):
    """code_scanning_alert fixed event"""

    action: Literal["fixed"] = Field()
    alert: WebhookCodeScanningAlertFixedPropAlert = Field(
        description="The code scanning alert involved in the event."
    )
    commit_oid: str = Field(
        description="The commit SHA of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty."
    )
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
    ref: str = Field(
        description="The Git reference of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty."
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookCodeScanningAlertFixedPropAlert(GitHubModel):
    """WebhookCodeScanningAlertFixedPropAlert

    The code scanning alert involved in the event.
    """

    created_at: datetime = Field(
        description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ.`"
    )
    dismissed_at: Union[datetime, None] = Field(
        description="The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    dismissed_by: Union[
        WebhookCodeScanningAlertFixedPropAlertPropDismissedBy, None
    ] = Field(title="User")
    dismissed_reason: Union[
        None, Literal["false positive", "won't fix", "used in tests"]
    ] = Field(description="The reason for dismissing or closing the alert.")
    html_url: str = Field(description="The GitHub URL of the alert resource.")
    instances_url: Missing[str] = Field(default=UNSET)
    most_recent_instance: Missing[
        Union[WebhookCodeScanningAlertFixedPropAlertPropMostRecentInstance, None]
    ] = Field(default=UNSET, title="Alert Instance")
    number: int = Field(description="The code scanning alert number.")
    rule: WebhookCodeScanningAlertFixedPropAlertPropRule = Field()
    state: Literal["fixed"] = Field(description="State of a code scanning alert.")
    tool: WebhookCodeScanningAlertFixedPropAlertPropTool = Field()
    url: str = Field()


class WebhookCodeScanningAlertFixedPropAlertPropDismissedBy(GitHubModel):
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


class WebhookCodeScanningAlertFixedPropAlertPropMostRecentInstance(GitHubModel):
    """Alert Instance"""

    analysis_key: str = Field(
        description="Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name."
    )
    category: Missing[str] = Field(
        default=UNSET,
        description="Identifies the configuration under which the analysis was executed.",
    )
    classifications: Missing[List[str]] = Field(default=UNSET)
    commit_sha: Missing[str] = Field(default=UNSET)
    environment: str = Field(
        description="Identifies the variable values associated with the environment in which the analysis that generated this alert instance was performed, such as the language that was analyzed."
    )
    location: Missing[
        WebhookCodeScanningAlertFixedPropAlertPropMostRecentInstancePropLocation
    ] = Field(default=UNSET)
    message: Missing[
        WebhookCodeScanningAlertFixedPropAlertPropMostRecentInstancePropMessage
    ] = Field(default=UNSET)
    ref: str = Field(
        description="The full Git reference, formatted as `refs/heads/<branch name>`."
    )
    state: Literal["open", "dismissed", "fixed"] = Field(
        description="State of a code scanning alert."
    )


class WebhookCodeScanningAlertFixedPropAlertPropMostRecentInstancePropLocation(
    GitHubModel
):
    """WebhookCodeScanningAlertFixedPropAlertPropMostRecentInstancePropLocation"""

    end_column: Missing[int] = Field(default=UNSET)
    end_line: Missing[int] = Field(default=UNSET)
    path: Missing[str] = Field(default=UNSET)
    start_column: Missing[int] = Field(default=UNSET)
    start_line: Missing[int] = Field(default=UNSET)


class WebhookCodeScanningAlertFixedPropAlertPropMostRecentInstancePropMessage(
    GitHubModel
):
    """WebhookCodeScanningAlertFixedPropAlertPropMostRecentInstancePropMessage"""

    text: Missing[str] = Field(default=UNSET)


class WebhookCodeScanningAlertFixedPropAlertPropRule(GitHubModel):
    """WebhookCodeScanningAlertFixedPropAlertPropRule"""

    description: str = Field(
        description="A short description of the rule used to detect the alert."
    )
    full_description: Missing[str] = Field(default=UNSET)
    help_: Missing[Union[str, None]] = Field(default=UNSET, alias="help")
    help_uri: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="A link to the documentation for the rule used to detect the alert.",
    )
    id: str = Field(
        description="A unique identifier for the rule used to detect the alert."
    )
    name: Missing[str] = Field(default=UNSET)
    severity: Union[None, Literal["none", "note", "warning", "error"]] = Field(
        description="The severity of the alert."
    )
    tags: Missing[Union[List[str], None]] = Field(default=UNSET)


class WebhookCodeScanningAlertFixedPropAlertPropTool(GitHubModel):
    """WebhookCodeScanningAlertFixedPropAlertPropTool"""

    guid: Missing[Union[str, None]] = Field(default=UNSET)
    name: str = Field(
        description="The name of the tool used to generate the code scanning analysis alert."
    )
    version: Union[str, None] = Field(
        description="The version of the tool used to detect the alert."
    )


model_rebuild(WebhookCodeScanningAlertFixed)
model_rebuild(WebhookCodeScanningAlertFixedPropAlert)
model_rebuild(WebhookCodeScanningAlertFixedPropAlertPropDismissedBy)
model_rebuild(WebhookCodeScanningAlertFixedPropAlertPropMostRecentInstance)
model_rebuild(WebhookCodeScanningAlertFixedPropAlertPropMostRecentInstancePropLocation)
model_rebuild(WebhookCodeScanningAlertFixedPropAlertPropMostRecentInstancePropMessage)
model_rebuild(WebhookCodeScanningAlertFixedPropAlertPropRule)
model_rebuild(WebhookCodeScanningAlertFixedPropAlertPropTool)

__all__ = (
    "WebhookCodeScanningAlertFixed",
    "WebhookCodeScanningAlertFixedPropAlert",
    "WebhookCodeScanningAlertFixedPropAlertPropDismissedBy",
    "WebhookCodeScanningAlertFixedPropAlertPropMostRecentInstance",
    "WebhookCodeScanningAlertFixedPropAlertPropMostRecentInstancePropLocation",
    "WebhookCodeScanningAlertFixedPropAlertPropMostRecentInstancePropMessage",
    "WebhookCodeScanningAlertFixedPropAlertPropRule",
    "WebhookCodeScanningAlertFixedPropAlertPropTool",
)
