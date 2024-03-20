"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations


from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class UserKeysPostBody(GitHubModel):
    """UserKeysPostBody"""

    title: Missing[str] = Field(
        default=UNSET, description="A descriptive name for the new key."
    )
    key: str = Field(
        pattern="^ssh-(rsa|dss|ed25519) |^ecdsa-sha2-nistp(256|384|521) ",
        description="The public SSH key to add to your GitHub account.",
    )


model_rebuild(UserKeysPostBody)

__all__ = ("UserKeysPostBody",)
