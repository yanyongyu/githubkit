"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0444 import EnterpriseWebhooksType
from .group_0445 import SimpleInstallationType
from .group_0446 import OrganizationSimpleWebhooksType
from .group_0447 import RepositoryWebhooksType


class WebhookCodeScanningAlertClosedByUserType(TypedDict):
    """code_scanning_alert closed_by_user event"""

    action: Literal["closed_by_user"]
    alert: WebhookCodeScanningAlertClosedByUserPropAlertType
    commit_oid: str
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    ref: str
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookCodeScanningAlertClosedByUserPropAlertType(TypedDict):
    """WebhookCodeScanningAlertClosedByUserPropAlert

    The code scanning alert involved in the event.
    """

    created_at: datetime
    dismissed_at: datetime
    dismissed_by: Union[
        WebhookCodeScanningAlertClosedByUserPropAlertPropDismissedByType, None
    ]
    dismissed_comment: NotRequired[Union[str, None]]
    dismissed_reason: Union[
        None, Literal["false positive", "won't fix", "used in tests"]
    ]
    fixed_at: NotRequired[None]
    html_url: str
    most_recent_instance: NotRequired[
        Union[
            WebhookCodeScanningAlertClosedByUserPropAlertPropMostRecentInstanceType,
            None,
        ]
    ]
    number: int
    rule: WebhookCodeScanningAlertClosedByUserPropAlertPropRuleType
    state: Literal["dismissed", "fixed"]
    tool: WebhookCodeScanningAlertClosedByUserPropAlertPropToolType
    url: str


class WebhookCodeScanningAlertClosedByUserPropAlertPropDismissedByType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhookCodeScanningAlertClosedByUserPropAlertPropMostRecentInstanceType(
    TypedDict
):
    """Alert Instance"""

    analysis_key: str
    category: NotRequired[str]
    classifications: NotRequired[list[str]]
    commit_sha: NotRequired[str]
    environment: str
    location: NotRequired[
        WebhookCodeScanningAlertClosedByUserPropAlertPropMostRecentInstancePropLocationType
    ]
    message: NotRequired[
        WebhookCodeScanningAlertClosedByUserPropAlertPropMostRecentInstancePropMessageType
    ]
    ref: str
    state: Literal["open", "dismissed", "fixed"]


class WebhookCodeScanningAlertClosedByUserPropAlertPropMostRecentInstancePropLocationType(
    TypedDict
):
    """WebhookCodeScanningAlertClosedByUserPropAlertPropMostRecentInstancePropLocation"""

    end_column: NotRequired[int]
    end_line: NotRequired[int]
    path: NotRequired[str]
    start_column: NotRequired[int]
    start_line: NotRequired[int]


class WebhookCodeScanningAlertClosedByUserPropAlertPropMostRecentInstancePropMessageType(
    TypedDict
):
    """WebhookCodeScanningAlertClosedByUserPropAlertPropMostRecentInstancePropMessage"""

    text: NotRequired[str]


class WebhookCodeScanningAlertClosedByUserPropAlertPropRuleType(TypedDict):
    """WebhookCodeScanningAlertClosedByUserPropAlertPropRule"""

    description: str
    full_description: NotRequired[str]
    help_: NotRequired[Union[str, None]]
    help_uri: NotRequired[Union[str, None]]
    id: str
    name: NotRequired[str]
    severity: Union[None, Literal["none", "note", "warning", "error"]]
    tags: NotRequired[Union[list[str], None]]


class WebhookCodeScanningAlertClosedByUserPropAlertPropToolType(TypedDict):
    """WebhookCodeScanningAlertClosedByUserPropAlertPropTool"""

    guid: NotRequired[Union[str, None]]
    name: str
    version: Union[str, None]


__all__ = (
    "WebhookCodeScanningAlertClosedByUserPropAlertPropDismissedByType",
    "WebhookCodeScanningAlertClosedByUserPropAlertPropMostRecentInstancePropLocationType",
    "WebhookCodeScanningAlertClosedByUserPropAlertPropMostRecentInstancePropMessageType",
    "WebhookCodeScanningAlertClosedByUserPropAlertPropMostRecentInstanceType",
    "WebhookCodeScanningAlertClosedByUserPropAlertPropRuleType",
    "WebhookCodeScanningAlertClosedByUserPropAlertPropToolType",
    "WebhookCodeScanningAlertClosedByUserPropAlertType",
    "WebhookCodeScanningAlertClosedByUserType",
)
