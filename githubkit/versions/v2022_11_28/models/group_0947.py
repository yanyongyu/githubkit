"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0153 import Job


class ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200(
    GitHubModel
):
    """ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200"""

    total_count: int = Field()
    jobs: List[Job] = Field()


model_rebuild(ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200)

__all__ = ("ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200",)
