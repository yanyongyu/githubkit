"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired


class CodeScanningAlertInstanceType(TypedDict):
    """CodeScanningAlertInstance"""

    ref: NotRequired[str]
    analysis_key: NotRequired[str]
    environment: NotRequired[str]
    category: NotRequired[str]
    state: NotRequired[Union[None, Literal["open", "dismissed", "fixed"]]]
    commit_sha: NotRequired[str]
    message: NotRequired[CodeScanningAlertInstancePropMessageType]
    location: NotRequired[CodeScanningAlertLocationType]
    html_url: NotRequired[str]
    classifications: NotRequired[
        list[Union[None, Literal["source", "generated", "test", "library"]]]
    ]


class CodeScanningAlertLocationType(TypedDict):
    """CodeScanningAlertLocation

    Describe a region within a file for the alert.
    """

    path: NotRequired[str]
    start_line: NotRequired[int]
    end_line: NotRequired[int]
    start_column: NotRequired[int]
    end_column: NotRequired[int]


class CodeScanningAlertInstancePropMessageType(TypedDict):
    """CodeScanningAlertInstancePropMessage"""

    text: NotRequired[str]


__all__ = (
    "CodeScanningAlertInstanceType",
    "CodeScanningAlertLocationType",
    "CodeScanningAlertInstancePropMessageType",
)
