"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0378 import EnterpriseWebhooksType
from .group_0379 import SimpleInstallationType
from .group_0381 import RepositoryWebhooksType
from .group_0382 import SimpleUserWebhooksType
from .group_0380 import OrganizationSimpleWebhooksType


class WebhookCodeScanningAlertReopenedType(TypedDict):
    """code_scanning_alert reopened event"""

    action: Literal["reopened"]
    alert: Union[WebhookCodeScanningAlertReopenedPropAlertType, None]
    commit_oid: Union[str, None]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    ref: Union[str, None]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookCodeScanningAlertReopenedPropAlertType(TypedDict):
    """WebhookCodeScanningAlertReopenedPropAlert

    The code scanning alert involved in the event.
    """

    created_at: datetime
    dismissed_at: Union[str, None]
    dismissed_by: Union[
        WebhookCodeScanningAlertReopenedPropAlertPropDismissedByType, None
    ]
    dismissed_reason: Union[str, None]
    html_url: str
    most_recent_instance: NotRequired[
        Union[WebhookCodeScanningAlertReopenedPropAlertPropMostRecentInstanceType, None]
    ]
    number: int
    rule: WebhookCodeScanningAlertReopenedPropAlertPropRuleType
    state: Literal["open", "dismissed", "fixed"]
    tool: WebhookCodeScanningAlertReopenedPropAlertPropToolType
    url: str


class WebhookCodeScanningAlertReopenedPropAlertPropDismissedByType(TypedDict):
    """WebhookCodeScanningAlertReopenedPropAlertPropDismissedBy"""


class WebhookCodeScanningAlertReopenedPropAlertPropMostRecentInstanceType(TypedDict):
    """Alert Instance"""

    analysis_key: str
    category: NotRequired[str]
    classifications: NotRequired[List[str]]
    commit_sha: NotRequired[str]
    environment: str
    location: NotRequired[
        WebhookCodeScanningAlertReopenedPropAlertPropMostRecentInstancePropLocationType
    ]
    message: NotRequired[
        WebhookCodeScanningAlertReopenedPropAlertPropMostRecentInstancePropMessageType
    ]
    ref: str
    state: Literal["open", "dismissed", "fixed"]


class WebhookCodeScanningAlertReopenedPropAlertPropMostRecentInstancePropLocationType(
    TypedDict
):
    """WebhookCodeScanningAlertReopenedPropAlertPropMostRecentInstancePropLocation"""

    end_column: NotRequired[int]
    end_line: NotRequired[int]
    path: NotRequired[str]
    start_column: NotRequired[int]
    start_line: NotRequired[int]


class WebhookCodeScanningAlertReopenedPropAlertPropMostRecentInstancePropMessageType(
    TypedDict
):
    """WebhookCodeScanningAlertReopenedPropAlertPropMostRecentInstancePropMessage"""

    text: NotRequired[str]


class WebhookCodeScanningAlertReopenedPropAlertPropRuleType(TypedDict):
    """WebhookCodeScanningAlertReopenedPropAlertPropRule"""

    description: str
    full_description: NotRequired[str]
    help_: NotRequired[Union[str, None]]
    help_uri: NotRequired[Union[str, None]]
    id: str
    name: NotRequired[str]
    severity: Union[None, Literal["none", "note", "warning", "error"]]
    tags: NotRequired[Union[List[str], None]]


class WebhookCodeScanningAlertReopenedPropAlertPropToolType(TypedDict):
    """WebhookCodeScanningAlertReopenedPropAlertPropTool"""

    guid: NotRequired[Union[str, None]]
    name: str
    version: Union[str, None]


__all__ = (
    "WebhookCodeScanningAlertReopenedType",
    "WebhookCodeScanningAlertReopenedPropAlertType",
    "WebhookCodeScanningAlertReopenedPropAlertPropDismissedByType",
    "WebhookCodeScanningAlertReopenedPropAlertPropMostRecentInstanceType",
    "WebhookCodeScanningAlertReopenedPropAlertPropMostRecentInstancePropLocationType",
    "WebhookCodeScanningAlertReopenedPropAlertPropMostRecentInstancePropMessageType",
    "WebhookCodeScanningAlertReopenedPropAlertPropRuleType",
    "WebhookCodeScanningAlertReopenedPropAlertPropToolType",
)
