"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict


class MarkdownPostBodyType(TypedDict):
    """MarkdownPostBody"""

    text: str
    mode: NotRequired[Literal["markdown", "gfm"]]
    context: NotRequired[str]


__all__ = ("MarkdownPostBodyType",)
