"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_1083 import ReposOwnerRepoPagesPostBodyPropSourceType


class ReposOwnerRepoPagesPostBodyAnyof1Type(TypedDict):
    """ReposOwnerRepoPagesPostBodyAnyof1"""

    build_type: Literal["legacy", "workflow"]
    source: NotRequired[ReposOwnerRepoPagesPostBodyPropSourceType]


__all__ = ("ReposOwnerRepoPagesPostBodyAnyof1Type",)
