"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class Blob(GitHubModel):
    """Blob

    Blob
    """

    content: str = Field()
    encoding: str = Field()
    url: str = Field()
    sha: str = Field()
    size: Union[int, None] = Field()
    node_id: str = Field()
    highlighted_content: Missing[str] = Field(default=UNSET)


model_rebuild(Blob)

__all__ = ("Blob",)
