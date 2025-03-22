"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0179 import Codespace


class ReposOwnerRepoCodespacesGetResponse200(GitHubModel):
    """ReposOwnerRepoCodespacesGetResponse200"""

    total_count: int = Field()
    codespaces: list[Codespace] = Field()


model_rebuild(ReposOwnerRepoCodespacesGetResponse200)

__all__ = ("ReposOwnerRepoCodespacesGetResponse200",)
