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


class ReposOwnerRepoImportAuthorsAuthorIdPatchBody(GitHubModel):
    """ReposOwnerRepoImportAuthorsAuthorIdPatchBody"""

    email: Missing[str] = Field(default=UNSET, description="The new Git author email.")
    name: Missing[str] = Field(default=UNSET, description="The new Git author name.")


model_rebuild(ReposOwnerRepoImportAuthorsAuthorIdPatchBody)

__all__ = ("ReposOwnerRepoImportAuthorsAuthorIdPatchBody",)
