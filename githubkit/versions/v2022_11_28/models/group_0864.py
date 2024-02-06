"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0050 import MinimalRepository


class OrgsOrgCodespacesSecretsSecretNameRepositoriesGetResponse200(GitHubModel):
    """OrgsOrgCodespacesSecretsSecretNameRepositoriesGetResponse200"""

    total_count: int = Field()
    repositories: List[MinimalRepository] = Field()


model_rebuild(OrgsOrgCodespacesSecretsSecretNameRepositoriesGetResponse200)

__all__ = ("OrgsOrgCodespacesSecretsSecretNameRepositoriesGetResponse200",)
