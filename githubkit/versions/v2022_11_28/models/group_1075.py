"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0207 import ActionsVariable


class ReposOwnerRepoEnvironmentsEnvironmentNameVariablesGetResponse200(GitHubModel):
    """ReposOwnerRepoEnvironmentsEnvironmentNameVariablesGetResponse200"""

    total_count: int = Field()
    variables: list[ActionsVariable] = Field()


model_rebuild(ReposOwnerRepoEnvironmentsEnvironmentNameVariablesGetResponse200)

__all__ = ("ReposOwnerRepoEnvironmentsEnvironmentNameVariablesGetResponse200",)
