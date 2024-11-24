"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict


class CodeScanningAlertRuleSummaryType(TypedDict):
    """CodeScanningAlertRuleSummary"""

    id: NotRequired[Union[str, None]]
    name: NotRequired[str]
    severity: NotRequired[Union[None, Literal["none", "note", "warning", "error"]]]
    security_severity_level: NotRequired[
        Union[None, Literal["low", "medium", "high", "critical"]]
    ]
    description: NotRequired[str]
    full_description: NotRequired[str]
    tags: NotRequired[Union[list[str], None]]
    help_: NotRequired[Union[str, None]]
    help_uri: NotRequired[Union[str, None]]


__all__ = ("CodeScanningAlertRuleSummaryType",)
