"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0178 import MinimalRepositoryType


class UserCodespacesSecretsSecretNameRepositoriesGetResponse200Type(TypedDict):
    """UserCodespacesSecretsSecretNameRepositoriesGetResponse200"""

    total_count: int
    repositories: list[MinimalRepositoryType]


__all__ = ("UserCodespacesSecretsSecretNameRepositoriesGetResponse200Type",)
