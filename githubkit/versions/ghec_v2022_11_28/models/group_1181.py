"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoImportLfsPatchBody(GitHubModel):
    """ReposOwnerRepoImportLfsPatchBody"""

    use_lfs: Literal["opt_in", "opt_out"] = Field(
        description="Whether to store large files during the import. `opt_in` means large files will be stored using Git LFS. `opt_out` means large files will be removed during the import."
    )


model_rebuild(ReposOwnerRepoImportLfsPatchBody)

__all__ = ("ReposOwnerRepoImportLfsPatchBody",)
