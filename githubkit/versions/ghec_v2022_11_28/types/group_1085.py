"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0237 import JobType


class ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200Type(
    TypedDict
):
    """ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200"""

    total_count: int
    jobs: list[JobType]


__all__ = ("ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200Type",)
