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


class ProjectsColumnsColumnIdCardsPostResponse503(GitHubModel):
    """ProjectsColumnsColumnIdCardsPostResponse503"""

    code: Missing[str] = Field(default=UNSET)
    message: Missing[str] = Field(default=UNSET)
    documentation_url: Missing[str] = Field(default=UNSET)
    errors: Missing[
        list[ProjectsColumnsColumnIdCardsPostResponse503PropErrorsItems]
    ] = Field(default=UNSET)


class ProjectsColumnsColumnIdCardsPostResponse503PropErrorsItems(GitHubModel):
    """ProjectsColumnsColumnIdCardsPostResponse503PropErrorsItems"""

    code: Missing[str] = Field(default=UNSET)
    message: Missing[str] = Field(default=UNSET)


model_rebuild(ProjectsColumnsColumnIdCardsPostResponse503)
model_rebuild(ProjectsColumnsColumnIdCardsPostResponse503PropErrorsItems)

__all__ = (
    "ProjectsColumnsColumnIdCardsPostResponse503",
    "ProjectsColumnsColumnIdCardsPostResponse503PropErrorsItems",
)
