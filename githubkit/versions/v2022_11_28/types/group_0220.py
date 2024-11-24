"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0217 import CodeScanningVariantAnalysisRepositoryType


class CodeScanningVariantAnalysisPropScannedRepositoriesItemsType(TypedDict):
    """CodeScanningVariantAnalysisPropScannedRepositoriesItems"""

    repository: CodeScanningVariantAnalysisRepositoryType
    analysis_status: Literal[
        "pending", "in_progress", "succeeded", "failed", "canceled", "timed_out"
    ]
    result_count: NotRequired[int]
    artifact_size_in_bytes: NotRequired[int]
    failure_message: NotRequired[str]


__all__ = ("CodeScanningVariantAnalysisPropScannedRepositoriesItemsType",)
