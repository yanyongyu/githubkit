"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .group_0015 import InstallationType


class OrgsOrgInstallationsGetResponse200Type(TypedDict):
    """OrgsOrgInstallationsGetResponse200"""

    total_count: int
    installations: List[InstallationType]


__all__ = ("OrgsOrgInstallationsGetResponse200Type",)
