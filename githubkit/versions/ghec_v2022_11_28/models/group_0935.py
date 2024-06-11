"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0177 import Artifact


class ReposOwnerRepoActionsArtifactsGetResponse200(GitHubModel):
    """ReposOwnerRepoActionsArtifactsGetResponse200"""

    total_count: int = Field()
    artifacts: List[Artifact] = Field()


model_rebuild(ReposOwnerRepoActionsArtifactsGetResponse200)

__all__ = ("ReposOwnerRepoActionsArtifactsGetResponse200",)
