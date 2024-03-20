"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict


class RepositoryRuleParamsCodeScanningThresholdType(TypedDict):
    """CodeScanningThreshold

    A tool and its thresholds.
    """

    alerts: Literal["none", "errors", "errors_and_warnings", "all"]
    security_alerts: Literal[
        "none", "critical", "high_or_higher", "medium_or_higher", "all"
    ]
    tool: str


__all__ = ("RepositoryRuleParamsCodeScanningThresholdType",)