"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0069 import Runner


class OrgsOrgActionsRunnerGroupsRunnerGroupIdRunnersGetResponse200(GitHubModel):
    """OrgsOrgActionsRunnerGroupsRunnerGroupIdRunnersGetResponse200"""

    total_count: float = Field()
    runners: list[Runner] = Field()


model_rebuild(OrgsOrgActionsRunnerGroupsRunnerGroupIdRunnersGetResponse200)

__all__ = ("OrgsOrgActionsRunnerGroupsRunnerGroupIdRunnersGetResponse200",)
