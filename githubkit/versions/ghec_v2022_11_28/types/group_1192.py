"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import NotRequired, TypedDict


class UserProjectsPostBodyType(TypedDict):
    """UserProjectsPostBody"""

    name: str
    body: NotRequired[Union[str, None]]


__all__ = ("UserProjectsPostBodyType",)