"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0178 import MinimalRepository


class OrgsOrgActionsRunnerGroupsRunnerGroupIdRepositoriesGetResponse200(GitHubModel):
    """OrgsOrgActionsRunnerGroupsRunnerGroupIdRepositoriesGetResponse200"""

    total_count: float = Field()
    repositories: list[MinimalRepository] = Field()


model_rebuild(OrgsOrgActionsRunnerGroupsRunnerGroupIdRepositoriesGetResponse200)

__all__ = ("OrgsOrgActionsRunnerGroupsRunnerGroupIdRepositoriesGetResponse200",)
