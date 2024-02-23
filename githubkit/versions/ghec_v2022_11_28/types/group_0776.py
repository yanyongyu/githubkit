"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0777 import (
    WebhookRepositoryVulnerabilityAlertDismissPropAlertAllof0PropDismisserType,
)


class WebhookRepositoryVulnerabilityAlertDismissPropAlertAllof0Type(TypedDict):
    """Repository Vulnerability Alert Alert

    The security alert of the vulnerable dependency.
    """

    affected_package_name: str
    affected_range: str
    created_at: str
    dismiss_comment: NotRequired[Union[str, None]]
    dismiss_reason: NotRequired[str]
    dismissed_at: NotRequired[str]
    dismisser: NotRequired[
        Union[
            WebhookRepositoryVulnerabilityAlertDismissPropAlertAllof0PropDismisserType,
            None,
        ]
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
    state: Literal["open", "dismissed", "fixed"]


__all__ = ("WebhookRepositoryVulnerabilityAlertDismissPropAlertAllof0Type",)
