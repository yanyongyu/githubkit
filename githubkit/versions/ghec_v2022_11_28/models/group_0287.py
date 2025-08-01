"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0010 import Integration
from .group_0178 import MinimalRepository
from .group_0257 import PullRequestMinimal
from .group_0258 import SimpleCommit


class CheckSuite(GitHubModel):
    """CheckSuite

    A suite of checks performed on the code of a given code change
    """

    id: int = Field()
    node_id: str = Field()
    head_branch: Union[str, None] = Field()
    head_sha: str = Field(
        description="The SHA of the head commit that is being checked."
    )
    status: Union[
        None,
        Literal[
            "queued", "in_progress", "completed", "waiting", "requested", "pending"
        ],
    ] = Field(
        description="The phase of the lifecycle that the check suite is currently in. Statuses of waiting, requested, and pending are reserved for GitHub Actions check suites."
    )
    conclusion: Union[
        None,
        Literal[
            "success",
            "failure",
            "neutral",
            "cancelled",
            "skipped",
            "timed_out",
            "action_required",
            "startup_failure",
            "stale",
        ],
    ] = Field()
    url: Union[str, None] = Field()
    before: Union[str, None] = Field()
    after: Union[str, None] = Field()
    pull_requests: Union[list[PullRequestMinimal], None] = Field()
    app: Union[None, Integration, None] = Field()
    repository: MinimalRepository = Field(
        title="Minimal Repository", description="Minimal Repository"
    )
    created_at: Union[datetime, None] = Field()
    updated_at: Union[datetime, None] = Field()
    head_commit: SimpleCommit = Field(title="Simple Commit", description="A commit.")
    latest_check_runs_count: int = Field()
    check_runs_url: str = Field()
    rerequestable: Missing[bool] = Field(default=UNSET)
    runs_rerequestable: Missing[bool] = Field(default=UNSET)


class ReposOwnerRepoCommitsRefCheckSuitesGetResponse200(GitHubModel):
    """ReposOwnerRepoCommitsRefCheckSuitesGetResponse200"""

    total_count: int = Field()
    check_suites: list[CheckSuite] = Field()


model_rebuild(CheckSuite)
model_rebuild(ReposOwnerRepoCommitsRefCheckSuitesGetResponse200)

__all__ = (
    "CheckSuite",
    "ReposOwnerRepoCommitsRefCheckSuitesGetResponse200",
)
