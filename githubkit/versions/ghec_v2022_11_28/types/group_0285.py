"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0284 import CodeScanningVariantAnalysisRepositoryType


class CodeScanningVariantAnalysisSkippedRepoGroupType(TypedDict):
    """CodeScanningVariantAnalysisSkippedRepoGroup"""

    repository_count: int
    repositories: list[CodeScanningVariantAnalysisRepositoryType]


__all__ = ("CodeScanningVariantAnalysisSkippedRepoGroupType",)
