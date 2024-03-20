"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class GistsGistIdGetResponse403(GitHubModel):
    """GistsGistIdGetResponse403"""

    block: Missing[GistsGistIdGetResponse403PropBlock] = Field(default=UNSET)
    message: Missing[str] = Field(default=UNSET)
    documentation_url: Missing[str] = Field(default=UNSET)


class GistsGistIdGetResponse403PropBlock(GitHubModel):
    """GistsGistIdGetResponse403PropBlock"""

    reason: Missing[str] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    html_url: Missing[Union[str, None]] = Field(default=UNSET)


model_rebuild(GistsGistIdGetResponse403)
model_rebuild(GistsGistIdGetResponse403PropBlock)

__all__ = (
    "GistsGistIdGetResponse403",
    "GistsGistIdGetResponse403PropBlock",
)
