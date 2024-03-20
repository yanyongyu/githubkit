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


class WebhookRepositoryVulnerabilityAlertResolvePropAlertAllof1(GitHubModel):
    """WebhookRepositoryVulnerabilityAlertResolvePropAlertAllof1"""

    affected_package_name: Missing[str] = Field(default=UNSET)
    affected_range: Missing[str] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    external_identifier: Missing[str] = Field(default=UNSET)
    external_reference: Missing[Union[str, None]] = Field(default=UNSET)
    fix_reason: Missing[str] = Field(default=UNSET)
    fixed_at: Missing[datetime] = Field(default=UNSET)
    fixed_in: Missing[str] = Field(default=UNSET)
    ghsa_id: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    number: Missing[int] = Field(default=UNSET)
    severity: Missing[str] = Field(default=UNSET)
    state: Literal["fixed", "open"] = Field()


model_rebuild(WebhookRepositoryVulnerabilityAlertResolvePropAlertAllof1)

__all__ = ("WebhookRepositoryVulnerabilityAlertResolvePropAlertAllof1",)
