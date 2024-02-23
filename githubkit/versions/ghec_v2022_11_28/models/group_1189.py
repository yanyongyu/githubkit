"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class UserCodespacesCodespaceNamePatchBody(GitHubModel):
    """UserCodespacesCodespaceNamePatchBody"""

    machine: Missing[str] = Field(
        default=UNSET, description="A valid machine to transition this codespace to."
    )
    display_name: Missing[str] = Field(
        default=UNSET, description="Display name for this codespace"
    )
    recent_folders: Missing[List[str]] = Field(
        default=UNSET,
        description="Recently opened folders inside the codespace. It is currently used by the clients to determine the folder path to load the codespace in.",
    )


model_rebuild(UserCodespacesCodespaceNamePatchBody)

__all__ = ("UserCodespacesCodespaceNamePatchBody",)
