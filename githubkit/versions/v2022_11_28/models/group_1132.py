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


class UserGpgKeysPostBody(GitHubModel):
    """UserGpgKeysPostBody"""

    name: Missing[str] = Field(
        default=UNSET, description="A descriptive name for the new key."
    )
    armored_public_key: str = Field(description="A GPG key in ASCII-armored format.")


model_rebuild(UserGpgKeysPostBody)

__all__ = ("UserGpgKeysPostBody",)
