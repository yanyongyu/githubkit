"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild


class GistsGistIdPatchBody(GitHubModel):
    """GistsGistIdPatchBody"""

    description: Missing[str] = Field(
        default=UNSET, description="The description of the gist."
    )
    files: Missing[GistsGistIdPatchBodyPropFiles] = Field(
        default=UNSET,
        description="The gist files to be updated, renamed, or deleted. Each `key` must match the current filename\n(including extension) of the targeted gist file. For example: `hello.py`.\n\nTo delete a file, set the whole file to null. For example: `hello.py : null`. The file will also be\ndeleted if the specified object does not contain at least one of `content` or `filename`.",
    )


class GistsGistIdPatchBodyPropFiles(ExtraGitHubModel):
    """GistsGistIdPatchBodyPropFiles

    The gist files to be updated, renamed, or deleted. Each `key` must match the
    current filename
    (including extension) of the targeted gist file. For example: `hello.py`.

    To delete a file, set the whole file to null. For example: `hello.py : null`.
    The file will also be
    deleted if the specified object does not contain at least one of `content` or
    `filename`.

    Examples:
        {'hello.rb': {'content': 'blah', 'filename': 'goodbye.rb'}}
    """


model_rebuild(GistsGistIdPatchBody)
model_rebuild(GistsGistIdPatchBodyPropFiles)

__all__ = (
    "GistsGistIdPatchBody",
    "GistsGistIdPatchBodyPropFiles",
)
