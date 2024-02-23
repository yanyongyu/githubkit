"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0207 import CheckRun


class ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200(GitHubModel):
    """ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200"""

    total_count: int = Field()
    check_runs: List[CheckRun] = Field()


model_rebuild(ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200)

__all__ = ("ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200",)
