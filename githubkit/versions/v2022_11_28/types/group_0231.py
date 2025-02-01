"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0031 import SimpleRepositoryType
from .group_0232 import CodeScanningVariantAnalysisPropScannedRepositoriesItemsType
from .group_0233 import CodeScanningVariantAnalysisPropSkippedRepositoriesType


class CodeScanningVariantAnalysisType(TypedDict):
    """Variant Analysis

    A run of a CodeQL query against one or more repositories.
    """

    id: int
    controller_repo: SimpleRepositoryType
    actor: SimpleUserType
    query_language: Literal[
        "cpp", "csharp", "go", "java", "javascript", "python", "ruby", "swift"
    ]
    query_pack_url: str
    created_at: NotRequired[datetime]
    updated_at: NotRequired[datetime]
    completed_at: NotRequired[Union[datetime, None]]
    status: Literal["in_progress", "succeeded", "failed", "cancelled"]
    actions_workflow_run_id: NotRequired[int]
    failure_reason: NotRequired[
        Literal["no_repos_queried", "actions_workflow_run_failed", "internal_error"]
    ]
    scanned_repositories: NotRequired[
        list[CodeScanningVariantAnalysisPropScannedRepositoriesItemsType]
    ]
    skipped_repositories: NotRequired[
        CodeScanningVariantAnalysisPropSkippedRepositoriesType
    ]


__all__ = ("CodeScanningVariantAnalysisType",)
