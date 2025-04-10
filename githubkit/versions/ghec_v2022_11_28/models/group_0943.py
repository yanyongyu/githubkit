"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class MarkdownPostBody(GitHubModel):
    """MarkdownPostBody"""

    text: str = Field(description="The Markdown text to render in HTML.")
    mode: Missing[Literal["markdown", "gfm"]] = Field(
        default=UNSET, description="The rendering mode."
    )
    context: Missing[str] = Field(
        default=UNSET,
        description="The repository context to use when creating references in `gfm` mode.  For example, setting `context` to `octo-org/octo-repo` will change the text `#42` into an HTML link to issue 42 in the `octo-org/octo-repo` repository.",
    )


model_rebuild(MarkdownPostBody)

__all__ = ("MarkdownPostBody",)
