"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class DependabotPublicKey(GitHubModel):
    """DependabotPublicKey

    The public key used for setting Dependabot Secrets.
    """

    key_id: str = Field(description="The identifier for the key.")
    key: str = Field(description="The Base64 encoded public key.")


model_rebuild(DependabotPublicKey)

__all__ = ("DependabotPublicKey",)
