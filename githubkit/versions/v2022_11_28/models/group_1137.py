"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class UserProjectsPostBody(GitHubModel):
    """UserProjectsPostBody"""

    name: str = Field(description="Name of the project")
    body: Missing[Union[str, None]] = Field(
        default=UNSET, description="Body of the project"
    )


model_rebuild(UserProjectsPostBody)

__all__ = ("UserProjectsPostBody",)
