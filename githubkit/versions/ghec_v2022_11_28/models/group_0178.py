"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class CodespaceMachine(GitHubModel):
    """Codespace machine

    A description of the machine powering a codespace.
    """

    name: str = Field(description="The name of the machine.")
    display_name: str = Field(
        description="The display name of the machine includes cores, memory, and storage."
    )
    operating_system: str = Field(description="The operating system of the machine.")
    storage_in_bytes: int = Field(
        description="How much storage is available to the codespace."
    )
    memory_in_bytes: int = Field(
        description="How much memory is available to the codespace."
    )
    cpus: int = Field(description="How many cores are available to the codespace.")
    prebuild_availability: Union[None, Literal["none", "ready", "in_progress"]] = Field(
        description='Whether a prebuild is currently available when creating a codespace for this machine and repository. If a branch was not specified as a ref, the default branch will be assumed. Value will be "null" if prebuilds are not supported or prebuild availability could not be determined. Value will be "none" if no prebuild is available. Latest values "ready" and "in_progress" indicate the prebuild availability status.'
    )


model_rebuild(CodespaceMachine)

__all__ = ("CodespaceMachine",)
