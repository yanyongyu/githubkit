"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing_extensions import Annotated

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoCodespacesSecretsSecretNamePutBody(GitHubModel):
    """ReposOwnerRepoCodespacesSecretsSecretNamePutBody"""

    encrypted_value: Missing[
        Annotated[
            str,
            Field(
                pattern="^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})$"
            ),
        ]
    ] = Field(
        default=UNSET,
        description="Value for your secret, encrypted with [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from the [Get a repository public key](https://docs.github.com/rest/codespaces/repository-secrets#get-a-repository-public-key) endpoint.",
    )
    key_id: Missing[str] = Field(
        default=UNSET, description="ID of the key you used to encrypt the secret."
    )


model_rebuild(ReposOwnerRepoCodespacesSecretsSecretNamePutBody)

__all__ = ("ReposOwnerRepoCodespacesSecretsSecretNamePutBody",)
