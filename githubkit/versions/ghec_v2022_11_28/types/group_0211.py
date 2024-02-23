"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0040 import CodeScanningAlertRuleSummaryType
from .group_0041 import CodeScanningAnalysisToolType
from .group_0042 import CodeScanningAlertInstanceType


class CodeScanningAlertItemsType(TypedDict):
    """CodeScanningAlertItems"""

    number: int
    created_at: datetime
    updated_at: NotRequired[datetime]
    url: str
    html_url: str
    instances_url: str
    state: Literal["open", "dismissed", "fixed"]
    fixed_at: NotRequired[Union[datetime, None]]
    dismissed_by: Union[None, SimpleUserType]
    dismissed_at: Union[datetime, None]
    dismissed_reason: Union[
        None, Literal["false positive", "won't fix", "used in tests"]
    ]
    dismissed_comment: NotRequired[Union[str, None]]
    rule: CodeScanningAlertRuleSummaryType
    tool: CodeScanningAnalysisToolType
    most_recent_instance: CodeScanningAlertInstanceType


__all__ = ("CodeScanningAlertItemsType",)
