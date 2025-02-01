"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0017 import AppPermissions


class ApplicationsClientIdTokenScopedPostBody(GitHubModel):
    """ApplicationsClientIdTokenScopedPostBody"""

    access_token: str = Field(
        description="The access token used to authenticate to the GitHub API."
    )
    target: Missing[str] = Field(
        default=UNSET,
        description="The name of the user or organization to scope the user access token to. **Required** unless `target_id` is specified.",
    )
    target_id: Missing[int] = Field(
        default=UNSET,
        description="The ID of the user or organization to scope the user access token to. **Required** unless `target` is specified.",
    )
    repositories: Missing[list[str]] = Field(
        default=UNSET,
        description="The list of repository names to scope the user access token to. `repositories` may not be specified if `repository_ids` is specified.",
    )
    repository_ids: Missing[list[int]] = Field(
        default=UNSET,
        description="The list of repository IDs to scope the user access token to. `repository_ids` may not be specified if `repositories` is specified.",
    )
    permissions: Missing[AppPermissions] = Field(
        default=UNSET,
        title="App Permissions",
        description="The permissions granted to the user access token.",
    )


model_rebuild(ApplicationsClientIdTokenScopedPostBody)

__all__ = ("ApplicationsClientIdTokenScopedPostBody",)
