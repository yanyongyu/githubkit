"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ActionsHostedRunnerMachineSpec(GitHubModel):
    """Github-owned VM details.

    Provides details of a particular machine spec.
    """

    id: str = Field(
        description="The ID used for the `size` parameter when creating a new runner."
    )
    cpu_cores: int = Field(description="The number of cores.")
    memory_gb: int = Field(description="The available RAM for the machine spec.")
    storage_gb: int = Field(
        description="The available SSD storage for the machine spec."
    )


model_rebuild(ActionsHostedRunnerMachineSpec)

__all__ = ("ActionsHostedRunnerMachineSpec",)
