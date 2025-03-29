"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0058 import SimpleRepositoryType


class CodeScanningVariantAnalysisRepoTaskType(TypedDict):
    """CodeScanningVariantAnalysisRepoTask"""

    repository: SimpleRepositoryType
    analysis_status: Literal[
        "pending", "in_progress", "succeeded", "failed", "canceled", "timed_out"
    ]
    artifact_size_in_bytes: NotRequired[int]
    result_count: NotRequired[int]
    failure_message: NotRequired[str]
    database_commit_sha: NotRequired[str]
    source_location_prefix: NotRequired[str]
    artifact_url: NotRequired[str]


__all__ = ("CodeScanningVariantAnalysisRepoTaskType",)
