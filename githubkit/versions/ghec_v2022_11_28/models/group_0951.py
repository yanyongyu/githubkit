"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class OrgsOrgOutsideCollaboratorsUsernameDeleteResponse422(GitHubModel):
    """OrgsOrgOutsideCollaboratorsUsernameDeleteResponse422"""

    message: Missing[str] = Field(default=UNSET)
    documentation_url: Missing[str] = Field(default=UNSET)


model_rebuild(OrgsOrgOutsideCollaboratorsUsernameDeleteResponse422)

__all__ = ("OrgsOrgOutsideCollaboratorsUsernameDeleteResponse422",)
