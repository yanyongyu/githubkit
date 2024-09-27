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


class ReposOwnerRepoCollaboratorsUsernamePutBody(GitHubModel):
    """ReposOwnerRepoCollaboratorsUsernamePutBody"""

    permission: Missing[str] = Field(
        default=UNSET,
        description="The permission to grant the collaborator. **Only valid on organization-owned repositories.** We accept the following permissions to be set: `pull`, `triage`, `push`, `maintain`, `admin` and you can also specify a custom repository role name, if the owning organization has defined any.",
    )


model_rebuild(ReposOwnerRepoCollaboratorsUsernamePutBody)

__all__ = ("ReposOwnerRepoCollaboratorsUsernamePutBody",)
