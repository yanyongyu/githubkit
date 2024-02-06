"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0155 import ActionsSecret


class ReposOwnerRepoActionsOrganizationSecretsGetResponse200(GitHubModel):
    """ReposOwnerRepoActionsOrganizationSecretsGetResponse200"""

    total_count: int = Field()
    secrets: List[ActionsSecret] = Field()


model_rebuild(ReposOwnerRepoActionsOrganizationSecretsGetResponse200)

__all__ = ("ReposOwnerRepoActionsOrganizationSecretsGetResponse200",)
