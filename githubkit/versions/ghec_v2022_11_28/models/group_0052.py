"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class GetLicenseSyncStatus(GitHubModel):
    """License Sync Status

    Information about the status of a license sync job for an enterprise.
    """

    server_instances: Missing[
        List[GetLicenseSyncStatusPropServerInstancesItems]
    ] = Field(default=UNSET)


class GetLicenseSyncStatusPropServerInstancesItems(GitHubModel):
    """GetLicenseSyncStatusPropServerInstancesItems"""

    server_id: Missing[str] = Field(default=UNSET)
    hostname: Missing[str] = Field(default=UNSET)
    last_sync: Missing[
        GetLicenseSyncStatusPropServerInstancesItemsPropLastSync
    ] = Field(default=UNSET)


class GetLicenseSyncStatusPropServerInstancesItemsPropLastSync(GitHubModel):
    """GetLicenseSyncStatusPropServerInstancesItemsPropLastSync"""

    date: Missing[str] = Field(default=UNSET)
    status: Missing[str] = Field(default=UNSET)
    error: Missing[str] = Field(default=UNSET)


model_rebuild(GetLicenseSyncStatus)
model_rebuild(GetLicenseSyncStatusPropServerInstancesItems)
model_rebuild(GetLicenseSyncStatusPropServerInstancesItemsPropLastSync)

__all__ = (
    "GetLicenseSyncStatus",
    "GetLicenseSyncStatusPropServerInstancesItems",
    "GetLicenseSyncStatusPropServerInstancesItemsPropLastSync",
)
