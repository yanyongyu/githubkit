"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0034 import Runner


class EnterprisesEnterpriseActionsRunnerGroupsRunnerGroupIdRunnersGetResponse200(
    GitHubModel
):
    """EnterprisesEnterpriseActionsRunnerGroupsRunnerGroupIdRunnersGetResponse200"""

    total_count: float = Field()
    runners: List[Runner] = Field()


model_rebuild(
    EnterprisesEnterpriseActionsRunnerGroupsRunnerGroupIdRunnersGetResponse200
)

__all__ = (
    "EnterprisesEnterpriseActionsRunnerGroupsRunnerGroupIdRunnersGetResponse200",
)