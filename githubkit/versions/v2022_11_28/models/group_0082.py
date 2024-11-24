"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser
from .group_0058 import MinimalRepository
from .group_0081 import CodespaceMachine


class Codespace(GitHubModel):
    """Codespace

    A codespace.
    """

    id: int = Field()
    name: str = Field(description="Automatically generated name of this codespace.")
    display_name: Missing[Union[str, None]] = Field(
        default=UNSET, description="Display name for this codespace."
    )
    environment_id: Union[str, None] = Field(
        description="UUID identifying this codespace's environment."
    )
    owner: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    billable_owner: SimpleUser = Field(
        title="Simple User", description="A GitHub user."
    )
    repository: MinimalRepository = Field(
        title="Minimal Repository", description="Minimal Repository"
    )
    machine: Union[None, CodespaceMachine] = Field()
    devcontainer_path: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="Path to devcontainer.json from repo root used to create Codespace.",
    )
    prebuild: Union[bool, None] = Field(
        description="Whether the codespace was created from a prebuild."
    )
    created_at: datetime = Field()
    updated_at: datetime = Field()
    last_used_at: datetime = Field(
        description="Last known time this codespace was started."
    )
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
    ] = Field(description="State of this codespace.")
    url: str = Field(description="API URL for this codespace.")
    git_status: CodespacePropGitStatus = Field(
        description="Details about the codespace's git repository."
    )
    location: Literal["EastUs", "SouthEastAsia", "WestEurope", "WestUs2"] = Field(
        description="The initally assigned location of a new codespace."
    )
    idle_timeout_minutes: Union[int, None] = Field(
        description="The number of minutes of inactivity after which this codespace will be automatically stopped."
    )
    web_url: str = Field(description="URL to access this codespace on the web.")
    machines_url: str = Field(
        description="API URL to access available alternate machine types for this codespace."
    )
    start_url: str = Field(description="API URL to start this codespace.")
    stop_url: str = Field(description="API URL to stop this codespace.")
    publish_url: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="API URL to publish this codespace to a new repository.",
    )
    pulls_url: Union[str, None] = Field(
        description="API URL for the Pull Request associated with this codespace, if any."
    )
    recent_folders: list[str] = Field()
    runtime_constraints: Missing[CodespacePropRuntimeConstraints] = Field(default=UNSET)
    pending_operation: Missing[Union[bool, None]] = Field(
        default=UNSET,
        description="Whether or not a codespace has a pending async operation. This would mean that the codespace is temporarily unavailable. The only thing that you can do with a codespace in this state is delete it.",
    )
    pending_operation_disabled_reason: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="Text to show user when codespace is disabled by a pending operation",
    )
    idle_timeout_notice: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="Text to show user when codespace idle timeout minutes has been overriden by an organization policy",
    )
    retention_period_minutes: Missing[Union[int, None]] = Field(
        default=UNSET,
        description="Duration in minutes after codespace has gone idle in which it will be deleted. Must be integer minutes between 0 and 43200 (30 days).",
    )
    retention_expires_at: Missing[Union[datetime, None]] = Field(
        default=UNSET,
        description='When a codespace will be auto-deleted based on the "retention_period_minutes" and "last_used_at"',
    )
    last_known_stop_notice: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The text to display to a user when a codespace has been stopped for a potentially actionable reason.",
    )


class CodespacePropGitStatus(GitHubModel):
    """CodespacePropGitStatus

    Details about the codespace's git repository.
    """

    ahead: Missing[int] = Field(
        default=UNSET,
        description="The number of commits the local repository is ahead of the remote.",
    )
    behind: Missing[int] = Field(
        default=UNSET,
        description="The number of commits the local repository is behind the remote.",
    )
    has_unpushed_changes: Missing[bool] = Field(
        default=UNSET, description="Whether the local repository has unpushed changes."
    )
    has_uncommitted_changes: Missing[bool] = Field(
        default=UNSET,
        description="Whether the local repository has uncommitted changes.",
    )
    ref: Missing[str] = Field(
        default=UNSET,
        description="The current branch (or SHA if in detached HEAD state) of the local repository.",
    )


class CodespacePropRuntimeConstraints(GitHubModel):
    """CodespacePropRuntimeConstraints"""

    allowed_port_privacy_settings: Missing[Union[list[str], None]] = Field(
        default=UNSET,
        description="The privacy settings a user can select from when forwarding a port.",
    )


model_rebuild(Codespace)
model_rebuild(CodespacePropGitStatus)
model_rebuild(CodespacePropRuntimeConstraints)

__all__ = (
    "Codespace",
    "CodespacePropGitStatus",
    "CodespacePropRuntimeConstraints",
)
