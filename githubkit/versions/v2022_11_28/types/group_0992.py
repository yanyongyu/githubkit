"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0217 import CheckRunType


class ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200Type(TypedDict):
    """ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200"""

    total_count: int
    check_runs: list[CheckRunType]


__all__ = ("ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200Type",)
