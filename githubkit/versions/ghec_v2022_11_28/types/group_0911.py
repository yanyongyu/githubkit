"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Any
from typing_extensions import NotRequired, TypeAlias, TypedDict


class GistsGistIdPatchBodyType(TypedDict):
    """GistsGistIdPatchBody"""

    description: NotRequired[str]
    files: NotRequired[GistsGistIdPatchBodyPropFilesType]


GistsGistIdPatchBodyPropFilesType: TypeAlias = dict[str, Any]
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


__all__ = (
    "GistsGistIdPatchBodyPropFilesType",
    "GistsGistIdPatchBodyType",
)
