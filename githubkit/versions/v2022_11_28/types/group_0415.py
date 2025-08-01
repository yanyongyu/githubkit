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
from .group_0092 import CodespaceMachineType
from .group_0126 import FullRepositoryType


class CodespaceWithFullRepositoryType(TypedDict):
    """Codespace

    A codespace.
    """

    id: int
    name: str
    display_name: NotRequired[Union[str, None]]
    environment_id: Union[str, None]
    owner: SimpleUserType
    billable_owner: SimpleUserType
    repository: FullRepositoryType
    machine: Union[None, CodespaceMachineType]
    devcontainer_path: NotRequired[Union[str, None]]
    prebuild: Union[bool, None]
    created_at: datetime
    updated_at: datetime
    last_used_at: datetime
    state: Literal[
        "Unknown",
        "Created",
        "Queued",
        "Provisioning",
        "Available",
        "Awaiting",
        "Unavailable",
        "Deleted",
        "Moved",
        "Shutdown",
        "Archived",
        "Starting",
        "ShuttingDown",
        "Failed",
        "Exporting",
        "Updating",
        "Rebuilding",
    ]
    url: str
    git_status: CodespaceWithFullRepositoryPropGitStatusType
    location: Literal["EastUs", "SouthEastAsia", "WestEurope", "WestUs2"]
    idle_timeout_minutes: Union[int, None]
    web_url: str
    machines_url: str
    start_url: str
    stop_url: str
    publish_url: NotRequired[Union[str, None]]
    pulls_url: Union[str, None]
    recent_folders: list[str]
    runtime_constraints: NotRequired[
        CodespaceWithFullRepositoryPropRuntimeConstraintsType
    ]
    pending_operation: NotRequired[Union[bool, None]]
    pending_operation_disabled_reason: NotRequired[Union[str, None]]
    idle_timeout_notice: NotRequired[Union[str, None]]
    retention_period_minutes: NotRequired[Union[int, None]]
    retention_expires_at: NotRequired[Union[datetime, None]]


class CodespaceWithFullRepositoryPropGitStatusType(TypedDict):
    """CodespaceWithFullRepositoryPropGitStatus

    Details about the codespace's git repository.
    """

    ahead: NotRequired[int]
    behind: NotRequired[int]
    has_unpushed_changes: NotRequired[bool]
    has_uncommitted_changes: NotRequired[bool]
    ref: NotRequired[str]


class CodespaceWithFullRepositoryPropRuntimeConstraintsType(TypedDict):
    """CodespaceWithFullRepositoryPropRuntimeConstraints"""

    allowed_port_privacy_settings: NotRequired[Union[list[str], None]]


__all__ = (
    "CodespaceWithFullRepositoryPropGitStatusType",
    "CodespaceWithFullRepositoryPropRuntimeConstraintsType",
    "CodespaceWithFullRepositoryType",
)
