"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0174 import Job


class ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200(
    GitHubModel
):
    """ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200"""

    total_count: int = Field()
    jobs: list[Job] = Field()


model_rebuild(ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200)

__all__ = ("ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200",)
