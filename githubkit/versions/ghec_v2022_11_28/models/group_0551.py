"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0472 import EnterpriseWebhooks
from .group_0473 import SimpleInstallation
from .group_0474 import OrganizationSimpleWebhooks
from .group_0475 import RepositoryWebhooks


class WebhookCodeScanningAlertReopenedByUser(GitHubModel):
    """code_scanning_alert reopened_by_user event"""

    action: Literal["reopened_by_user"] = Field()
    alert: WebhookCodeScanningAlertReopenedByUserPropAlert = Field(
        description="The code scanning alert involved in the event."
    )
    commit_oid: str = Field(
        description="The commit SHA of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty."
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
    ref: str = Field(
        description="The Git reference of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty."
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class WebhookCodeScanningAlertReopenedByUserPropAlert(GitHubModel):
    """WebhookCodeScanningAlertReopenedByUserPropAlert

    The code scanning alert involved in the event.
    """

    created_at: datetime = Field(
        description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ.`"
    )
    dismissed_at: None = Field(
        description="The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    dismissed_by: None = Field()
    dismissed_comment: Missing[Union[Annotated[str, Field(max_length=280)], None]] = (
        Field(
            default=UNSET,
            description="The dismissal comment associated with the dismissal of the alert.",
        )
    )
    dismissed_reason: None = Field(
        description="The reason for dismissing or closing the alert. Can be one of: `false positive`, `won't fix`, and `used in tests`."
    )
    fixed_at: Missing[None] = Field(
        default=UNSET,
        description="The time that the alert was fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    html_url: str = Field(description="The GitHub URL of the alert resource.")
    most_recent_instance: Missing[
        Union[
            WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstance, None
        ]
    ] = Field(default=UNSET, title="Alert Instance")
    number: int = Field(description="The code scanning alert number.")
    rule: WebhookCodeScanningAlertReopenedByUserPropAlertPropRule = Field()
    state: Union[None, Literal["open", "fixed"]] = Field(
        description="State of a code scanning alert. Events for alerts found outside the default branch will return a `null` value until they are dismissed or fixed."
    )
    tool: WebhookCodeScanningAlertReopenedByUserPropAlertPropTool = Field()
    url: str = Field()


class WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstance(
    GitHubModel
):
    """Alert Instance"""

    analysis_key: str = Field(
        description="Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name."
    )
    category: Missing[str] = Field(
        default=UNSET,
        description="Identifies the configuration under which the analysis was executed.",
    )
    classifications: Missing[list[str]] = Field(default=UNSET)
    commit_sha: Missing[str] = Field(default=UNSET)
    environment: str = Field(
        description="Identifies the variable values associated with the environment in which the analysis that generated this alert instance was performed, such as the language that was analyzed."
    )
    location: Missing[
        WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropLocation
    ] = Field(default=UNSET)
    message: Missing[
        WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropMessage
    ] = Field(default=UNSET)
    ref: str = Field(
        description="The full Git reference, formatted as `refs/heads/<branch name>`."
    )
    state: Literal["open", "dismissed", "fixed"] = Field(
        description="State of a code scanning alert."
    )


class WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropLocation(
    GitHubModel
):
    """WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropLocatio
    n
    """

    end_column: Missing[int] = Field(default=UNSET)
    end_line: Missing[int] = Field(default=UNSET)
    path: Missing[str] = Field(default=UNSET)
    start_column: Missing[int] = Field(default=UNSET)
    start_line: Missing[int] = Field(default=UNSET)


class WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropMessage(
    GitHubModel
):
    """WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropMessage"""

    text: Missing[str] = Field(default=UNSET)


class WebhookCodeScanningAlertReopenedByUserPropAlertPropRule(GitHubModel):
    """WebhookCodeScanningAlertReopenedByUserPropAlertPropRule"""

    description: str = Field(
        description="A short description of the rule used to detect the alert."
    )
    id: str = Field(
        description="A unique identifier for the rule used to detect the alert."
    )
    severity: Union[None, Literal["none", "note", "warning", "error"]] = Field(
        description="The severity of the alert."
    )


class WebhookCodeScanningAlertReopenedByUserPropAlertPropTool(GitHubModel):
    """WebhookCodeScanningAlertReopenedByUserPropAlertPropTool"""

    name: str = Field(
        description="The name of the tool used to generate the code scanning analysis alert."
    )
    version: Union[str, None] = Field(
        description="The version of the tool used to detect the alert."
    )


model_rebuild(WebhookCodeScanningAlertReopenedByUser)
model_rebuild(WebhookCodeScanningAlertReopenedByUserPropAlert)
model_rebuild(WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstance)
model_rebuild(
    WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropLocation
)
model_rebuild(
    WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropMessage
)
model_rebuild(WebhookCodeScanningAlertReopenedByUserPropAlertPropRule)
model_rebuild(WebhookCodeScanningAlertReopenedByUserPropAlertPropTool)

__all__ = (
    "WebhookCodeScanningAlertReopenedByUser",
    "WebhookCodeScanningAlertReopenedByUserPropAlert",
    "WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstance",
    "WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropLocation",
    "WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropMessage",
    "WebhookCodeScanningAlertReopenedByUserPropAlertPropRule",
    "WebhookCodeScanningAlertReopenedByUserPropAlertPropTool",
)
