"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0456 import EnterpriseWebhooksType
from .group_0457 import SimpleInstallationType
from .group_0458 import OrganizationSimpleWebhooksType
from .group_0459 import RepositoryWebhooksType


class WebhookRepositoryVulnerabilityAlertDismissType(TypedDict):
    """repository_vulnerability_alert dismiss event"""

    action: Literal["dismiss"]
    alert: WebhookRepositoryVulnerabilityAlertDismissPropAlertType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookRepositoryVulnerabilityAlertDismissPropAlertType(TypedDict):
    """Repository Vulnerability Alert Alert

    The security alert of the vulnerable dependency.
    """

    affected_package_name: str
    affected_range: str
    created_at: str
    dismiss_comment: NotRequired[Union[str, None]]
    dismiss_reason: str
    dismissed_at: str
    dismisser: Union[
        WebhookRepositoryVulnerabilityAlertDismissPropAlertPropDismisserType, None
    ]
    external_identifier: str
    external_reference: Union[str, None]
    fix_reason: NotRequired[str]
    fixed_at: NotRequired[datetime]
    fixed_in: NotRequired[str]
    ghsa_id: str
    id: int
    node_id: str
    number: int
    severity: str
    state: Literal["dismissed"]


class WebhookRepositoryVulnerabilityAlertDismissPropAlertPropDismisserType(TypedDict):
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


__all__ = (
    "WebhookRepositoryVulnerabilityAlertDismissPropAlertPropDismisserType",
    "WebhookRepositoryVulnerabilityAlertDismissPropAlertType",
    "WebhookRepositoryVulnerabilityAlertDismissType",
)
