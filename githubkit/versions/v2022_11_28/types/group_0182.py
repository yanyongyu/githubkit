"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0058 import MinimalRepositoryType
from .group_0180 import PullRequestMinimalType
from .group_0181 import SimpleCommitType


class WorkflowRunType(TypedDict):
    """Workflow Run

    An invocation of a workflow
    """

    id: int
    name: NotRequired[Union[str, None]]
    node_id: str
    check_suite_id: NotRequired[int]
    check_suite_node_id: NotRequired[str]
    head_branch: Union[str, None]
    head_sha: str
    path: str
    run_number: int
    run_attempt: NotRequired[int]
    referenced_workflows: NotRequired[Union[list[ReferencedWorkflowType], None]]
    event: str
    status: Union[str, None]
    conclusion: Union[str, None]
    workflow_id: int
    url: str
    html_url: str
    pull_requests: Union[list[PullRequestMinimalType], None]
    created_at: datetime
    updated_at: datetime
    actor: NotRequired[SimpleUserType]
    triggering_actor: NotRequired[SimpleUserType]
    run_started_at: NotRequired[datetime]
    jobs_url: str
    logs_url: str
    check_suite_url: str
    artifacts_url: str
    cancel_url: str
    rerun_url: str
    previous_attempt_url: NotRequired[Union[str, None]]
    workflow_url: str
    head_commit: Union[None, SimpleCommitType]
    repository: MinimalRepositoryType
    head_repository: MinimalRepositoryType
    head_repository_id: NotRequired[int]
    display_title: str


class ReferencedWorkflowType(TypedDict):
    """Referenced workflow

    A workflow referenced/reused by the initial caller workflow
    """

    path: str
    sha: str
    ref: NotRequired[str]


__all__ = (
    "ReferencedWorkflowType",
    "WorkflowRunType",
)
