"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0189 import CodespaceMachine


class UserCodespacesCodespaceNameMachinesGetResponse200(GitHubModel):
    """UserCodespacesCodespaceNameMachinesGetResponse200"""

    total_count: int = Field()
    machines: list[CodespaceMachine] = Field()


model_rebuild(UserCodespacesCodespaceNameMachinesGetResponse200)

__all__ = ("UserCodespacesCodespaceNameMachinesGetResponse200",)
