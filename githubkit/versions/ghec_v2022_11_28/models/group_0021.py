"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0017 import AppPermissions
from .group_0020 import Repository


class InstallationToken(GitHubModel):
    """Installation Token

    Authentication token for a GitHub App installed on a user, org, or enterprise.
    """

    token: str = Field()
    expires_at: str = Field()
    permissions: Missing[AppPermissions] = Field(
        default=UNSET,
        title="App Permissions",
        description="The permissions granted to the user access token.",
    )
    repository_selection: Missing[Literal["all", "selected"]] = Field(default=UNSET)
    repositories: Missing[list[Repository]] = Field(default=UNSET)
    single_file: Missing[str] = Field(default=UNSET)
    has_multiple_single_files: Missing[bool] = Field(default=UNSET)
    single_file_paths: Missing[list[str]] = Field(default=UNSET)


model_rebuild(InstallationToken)

__all__ = ("InstallationToken",)
