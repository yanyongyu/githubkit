"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import ExtraGitHubModel, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class GistsPostBody(GitHubModel):
    """GistsPostBody"""

    description: Missing[str] = Field(
        default=UNSET, description="Description of the gist"
    )
    files: GistsPostBodyPropFiles = Field(
        description="Names and content for the files that make up the gist"
    )
    public: Missing[Union[bool, Literal["true", "false"]]] = Field(default=UNSET)


class GistsPostBodyPropFiles(ExtraGitHubModel):
    """GistsPostBodyPropFiles

    Names and content for the files that make up the gist

    Examples:
        {'hello.rb': {'content': 'puts "Hello, World!"'}}
    """


model_rebuild(GistsPostBody)
model_rebuild(GistsPostBodyPropFiles)

__all__ = (
    "GistsPostBody",
    "GistsPostBodyPropFiles",
)
