"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0155 import MinimalRepository


class OrgsOrgCodespacesSecretsSecretNameRepositoriesGetResponse200(GitHubModel):
    """OrgsOrgCodespacesSecretsSecretNameRepositoriesGetResponse200"""

    total_count: int = Field()
    repositories: list[MinimalRepository] = Field()


model_rebuild(OrgsOrgCodespacesSecretsSecretNameRepositoriesGetResponse200)

__all__ = ("OrgsOrgCodespacesSecretsSecretNameRepositoriesGetResponse200",)
