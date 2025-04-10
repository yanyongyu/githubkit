"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class ProjectsProjectIdPatchBody(GitHubModel):
    """ProjectsProjectIdPatchBody"""

    name: Missing[str] = Field(default=UNSET, description="Name of the project")
    body: Missing[Union[str, None]] = Field(
        default=UNSET, description="Body of the project"
    )
    state: Missing[str] = Field(
        default=UNSET, description="State of the project; either 'open' or 'closed'"
    )
    organization_permission: Missing[Literal["read", "write", "admin", "none"]] = Field(
        default=UNSET,
        description="The baseline permission that all organization members have on this project",
    )
    private: Missing[bool] = Field(
        default=UNSET,
        description="Whether or not this project can be seen by everyone.",
    )


model_rebuild(ProjectsProjectIdPatchBody)

__all__ = ("ProjectsProjectIdPatchBody",)
