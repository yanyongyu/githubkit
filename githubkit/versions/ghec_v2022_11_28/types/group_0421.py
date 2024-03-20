"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0390 import EnterpriseWebhooksType
from .group_0391 import SimpleInstallationType
from .group_0392 import OrganizationSimpleWebhooksType
from .group_0393 import RepositoryWebhooksType
from .group_0394 import SimpleUserWebhooksType


class WebhookCodeScanningAlertCreatedType(TypedDict):
    """code_scanning_alert created event"""

    action: Literal["created"]
    alert: WebhookCodeScanningAlertCreatedPropAlertType
    commit_oid: str
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    ref: str
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookCodeScanningAlertCreatedPropAlertType(TypedDict):
    """WebhookCodeScanningAlertCreatedPropAlert

    The code scanning alert involved in the event.
    """

    created_at: Union[datetime, None]
    dismissed_at: None
    dismissed_by: None
    dismissed_comment: NotRequired[Union[str, None]]
    dismissed_reason: None
    fixed_at: NotRequired[None]
    html_url: str
    instances_url: NotRequired[str]
    most_recent_instance: NotRequired[
        Union[WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstanceType, None]
    ]
    number: int
    rule: WebhookCodeScanningAlertCreatedPropAlertPropRuleType
    state: Literal["open", "dismissed"]
    tool: Union[WebhookCodeScanningAlertCreatedPropAlertPropToolType, None]
    updated_at: NotRequired[Union[str, None]]
    url: str


class WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstanceType(TypedDict):
    """Alert Instance"""

    analysis_key: str
    category: NotRequired[str]
    classifications: NotRequired[List[str]]
    commit_sha: NotRequired[str]
    environment: str
    location: NotRequired[
        WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropLocationType
    ]
    message: NotRequired[
        WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropMessageType
    ]
    ref: str
    state: Literal["open", "dismissed", "fixed"]


class WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropLocationType(
    TypedDict
):
    """WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropLocation"""

    end_column: NotRequired[int]
    end_line: NotRequired[int]
    path: NotRequired[str]
    start_column: NotRequired[int]
    start_line: NotRequired[int]


class WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropMessageType(
    TypedDict
):
    """WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropMessage"""

    text: NotRequired[str]


class WebhookCodeScanningAlertCreatedPropAlertPropRuleType(TypedDict):
    """WebhookCodeScanningAlertCreatedPropAlertPropRule"""

    description: str
    full_description: NotRequired[str]
    help_: NotRequired[Union[str, None]]
    help_uri: NotRequired[Union[str, None]]
    id: str
    name: NotRequired[str]
    severity: Union[None, Literal["none", "note", "warning", "error"]]
    tags: NotRequired[Union[List[str], None]]


class WebhookCodeScanningAlertCreatedPropAlertPropToolType(TypedDict):
    """WebhookCodeScanningAlertCreatedPropAlertPropTool"""

    guid: NotRequired[Union[str, None]]
    name: str
    version: Union[str, None]


__all__ = (
    "WebhookCodeScanningAlertCreatedType",
    "WebhookCodeScanningAlertCreatedPropAlertType",
    "WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstanceType",
    "WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropLocationType",
    "WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropMessageType",
    "WebhookCodeScanningAlertCreatedPropAlertPropRuleType",
    "WebhookCodeScanningAlertCreatedPropAlertPropToolType",
)
