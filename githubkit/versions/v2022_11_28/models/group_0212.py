"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0003 import SimpleUser
from .group_0063 import MinimalRepository
from .group_0210 import PullRequestMinimal
from .group_0211 import SimpleCommit


class WorkflowRun(GitHubModel):
    """Workflow Run

    An invocation of a workflow
    """

    id: int = Field(description="The ID of the workflow run.")
    name: Missing[Union[str, None]] = Field(
        default=UNSET, description="The name of the workflow run."
    )
    node_id: str = Field()
    check_suite_id: Missing[int] = Field(
        default=UNSET, description="The ID of the associated check suite."
    )
    check_suite_node_id: Missing[str] = Field(
        default=UNSET, description="The node ID of the associated check suite."
    )
    head_branch: Union[str, None] = Field()
    head_sha: str = Field(
        description="The SHA of the head commit that points to the version of the workflow being run."
    )
    path: str = Field(description="The full path of the workflow")
    run_number: int = Field(
        description="The auto incrementing run number for the workflow run."
    )
    run_attempt: Missing[int] = Field(
        default=UNSET,
        description="Attempt number of the run, 1 for first attempt and higher if the workflow was re-run.",
    )
    referenced_workflows: Missing[Union[list[ReferencedWorkflow], None]] = Field(
        default=UNSET
    )
    event: str = Field()
    status: Union[str, None] = Field()
    conclusion: Union[str, None] = Field()
    workflow_id: int = Field(description="The ID of the parent workflow.")
    url: str = Field(description="The URL to the workflow run.")
    html_url: str = Field()
    pull_requests: Union[list[PullRequestMinimal], None] = Field(
        description="Pull requests that are open with a `head_sha` or `head_branch` that matches the workflow run. The returned pull requests do not necessarily indicate pull requests that triggered the run."
    )
    created_at: datetime = Field()
    updated_at: datetime = Field()
    actor: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )
    triggering_actor: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )
    run_started_at: Missing[datetime] = Field(
        default=UNSET, description="The start time of the latest run. Resets on re-run."
    )
    jobs_url: str = Field(description="The URL to the jobs for the workflow run.")
    logs_url: str = Field(
        description="The URL to download the logs for the workflow run."
    )
    check_suite_url: str = Field(description="The URL to the associated check suite.")
    artifacts_url: str = Field(
        description="The URL to the artifacts for the workflow run."
    )
    cancel_url: str = Field(description="The URL to cancel the workflow run.")
    rerun_url: str = Field(description="The URL to rerun the workflow run.")
    previous_attempt_url: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The URL to the previous attempted run of this workflow, if one exists.",
    )
    workflow_url: str = Field(description="The URL to the workflow.")
    head_commit: Union[None, SimpleCommit] = Field()
    repository: MinimalRepository = Field(
        title="Minimal Repository", description="Minimal Repository"
    )
    head_repository: MinimalRepository = Field(
        title="Minimal Repository", description="Minimal Repository"
    )
    head_repository_id: Missing[int] = Field(default=UNSET)
    display_title: str = Field(
        description="The event-specific title associated with the run or the run-name if set, or the value of `run-name` if it is set in the workflow."
    )


class ReferencedWorkflow(GitHubModel):
    """Referenced workflow

    A workflow referenced/reused by the initial caller workflow
    """

    path: str = Field()
    sha: str = Field()
    ref: Missing[str] = Field(default=UNSET)


model_rebuild(WorkflowRun)
model_rebuild(ReferencedWorkflow)

__all__ = (
    "ReferencedWorkflow",
    "WorkflowRun",
)
