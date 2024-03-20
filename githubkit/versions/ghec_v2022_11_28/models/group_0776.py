"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0778 import (
    WebhookRepositoryVulnerabilityAlertDismissPropAlertAllof0PropDismisser,
)


class WebhookRepositoryVulnerabilityAlertDismissPropAlert(GitHubModel):
    """WebhookRepositoryVulnerabilityAlertDismissPropAlert"""

    affected_package_name: str = Field()
    affected_range: str = Field()
    created_at: str = Field()
    dismiss_comment: Missing[Union[Union[str, None], None]] = Field(default=UNSET)
    dismiss_reason: str = Field()
    dismissed_at: str = Field()
    dismisser: Union[
        Union[
            WebhookRepositoryVulnerabilityAlertDismissPropAlertAllof0PropDismisser, None
        ],
        None,
    ] = Field(title="User")
    external_identifier: str = Field()
    external_reference: Union[Union[str, None], None] = Field()
    fix_reason: Missing[str] = Field(default=UNSET)
    fixed_at: Missing[datetime] = Field(default=UNSET)
    fixed_in: Missing[str] = Field(default=UNSET)
    ghsa_id: str = Field()
    id: int = Field()
    node_id: str = Field()
    number: int = Field()
    severity: str = Field()
    state: Literal["dismissed"] = Field()


model_rebuild(WebhookRepositoryVulnerabilityAlertDismissPropAlert)

__all__ = ("WebhookRepositoryVulnerabilityAlertDismissPropAlert",)
