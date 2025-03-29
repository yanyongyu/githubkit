"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing_extensions import NotRequired, TypedDict

from .group_0080 import CodeScanningAnalysisToolType


class CodeScanningAnalysisType(TypedDict):
    """CodeScanningAnalysis"""

    ref: str
    commit_sha: str
    analysis_key: str
    environment: str
    category: NotRequired[str]
    error: str
    created_at: datetime
    results_count: int
    rules_count: int
    id: int
    url: str
    sarif_id: str
    tool: CodeScanningAnalysisToolType
    deletable: bool
    warning: str


__all__ = ("CodeScanningAnalysisType",)
