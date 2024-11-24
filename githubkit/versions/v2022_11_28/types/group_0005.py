"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict


class BasicErrorType(TypedDict):
    """Basic Error

    Basic Error
    """

    message: NotRequired[str]
    documentation_url: NotRequired[str]
    url: NotRequired[str]
    status: NotRequired[str]


__all__ = ("BasicErrorType",)
