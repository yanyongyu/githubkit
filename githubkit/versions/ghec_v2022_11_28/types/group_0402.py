"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import TypedDict

from .group_0003 import SimpleUserType


class StargazerType(TypedDict):
    """Stargazer

    Stargazer
    """

    starred_at: datetime
    user: Union[None, SimpleUserType]


__all__ = ("StargazerType",)
