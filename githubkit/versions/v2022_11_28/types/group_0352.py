"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing_extensions import TypedDict

from .group_0017 import RepositoryType


class StarredRepositoryType(TypedDict):
    """Starred Repository

    Starred Repository
    """

    starred_at: datetime
    repo: RepositoryType


__all__ = ("StarredRepositoryType",)
