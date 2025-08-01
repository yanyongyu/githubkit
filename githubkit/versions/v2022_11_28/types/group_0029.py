"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import NotRequired, TypedDict


class CodeScanningOptionsType(TypedDict):
    """CodeScanningOptions

    Security Configuration feature options for code scanning
    """

    allow_advanced: NotRequired[Union[bool, None]]


__all__ = ("CodeScanningOptionsType",)
