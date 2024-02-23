"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class OrgHook(GitHubModel):
    """Org Hook

    Org Hook
    """

    id: int = Field()
    url: str = Field()
    ping_url: str = Field()
    deliveries_url: Missing[str] = Field(default=UNSET)
    name: str = Field()
    events: List[str] = Field()
    active: bool = Field()
    config: OrgHookPropConfig = Field()
    updated_at: datetime = Field()
    created_at: datetime = Field()
    type: str = Field()


class OrgHookPropConfig(GitHubModel):
    """OrgHookPropConfig"""

    url: Missing[str] = Field(default=UNSET)
    insecure_ssl: Missing[str] = Field(default=UNSET)
    content_type: Missing[str] = Field(default=UNSET)
    secret: Missing[str] = Field(default=UNSET)


model_rebuild(OrgHook)
model_rebuild(OrgHookPropConfig)

__all__ = (
    "OrgHook",
    "OrgHookPropConfig",
)
