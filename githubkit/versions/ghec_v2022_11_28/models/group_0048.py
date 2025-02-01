"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class GetAuditLogStreamConfigsItems(GitHubModel):
    """GetAuditLogStreamConfigsItems"""

    id: Missing[int] = Field(default=UNSET)
    stream_type: Missing[str] = Field(default=UNSET)
    stream_details: Missing[str] = Field(default=UNSET)
    enabled: Missing[bool] = Field(default=UNSET)
    created_at: Missing[datetime] = Field(default=UNSET)
    updated_at: Missing[datetime] = Field(default=UNSET)
    paused_at: Missing[Union[datetime, None]] = Field(default=UNSET)


model_rebuild(GetAuditLogStreamConfigsItems)

__all__ = ("GetAuditLogStreamConfigsItems",)
