"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0154 import MinimalRepository


class OrgsOrgDependabotSecretsSecretNameRepositoriesGetResponse200(GitHubModel):
    """OrgsOrgDependabotSecretsSecretNameRepositoriesGetResponse200"""

    total_count: int = Field()
    repositories: list[MinimalRepository] = Field()


model_rebuild(OrgsOrgDependabotSecretsSecretNameRepositoriesGetResponse200)

__all__ = ("OrgsOrgDependabotSecretsSecretNameRepositoriesGetResponse200",)
