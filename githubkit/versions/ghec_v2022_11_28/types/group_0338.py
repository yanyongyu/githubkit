"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import TypedDict

from .group_0002 import SimpleUserType


class PageBuildType(TypedDict):
    """Page Build

    Page Build
    """

    url: str
    status: str
    error: PageBuildPropErrorType
    pusher: Union[None, SimpleUserType]
    commit: str
    duration: int
    created_at: datetime
    updated_at: datetime


class PageBuildPropErrorType(TypedDict):
    """PageBuildPropError"""

    message: Union[str, None]


__all__ = (
    "PageBuildPropErrorType",
    "PageBuildType",
)
