"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict


class LicenseType(TypedDict):
    """License

    License
    """

    key: str
    name: str
    spdx_id: Union[str, None]
    url: Union[str, None]
    node_id: str
    html_url: str
    description: str
    implementation: str
    permissions: list[str]
    conditions: list[str]
    limitations: list[str]
    body: str
    featured: bool


__all__ = ("LicenseType",)
