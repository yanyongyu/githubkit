"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0005 import IntegrationType
from .group_0161 import PullRequestMinimalType
from .group_0188 import DeploymentSimpleType


class CheckRunType(TypedDict):
    """CheckRun

    A check performed on the code of a given code change
    """

    id: int
    head_sha: str
    node_id: str
    external_id: Union[str, None]
    url: str
    html_url: Union[str, None]
    details_url: Union[str, None]
    status: Literal[
        "queued", "in_progress", "completed", "waiting", "requested", "pending"
    ]
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
        ],
    ]
    started_at: Union[datetime, None]
    completed_at: Union[datetime, None]
    output: CheckRunPropOutputType
    name: str
    check_suite: Union[CheckRunPropCheckSuiteType, None]
    app: Union[None, IntegrationType]
    pull_requests: List[PullRequestMinimalType]
    deployment: NotRequired[DeploymentSimpleType]


class CheckRunPropOutputType(TypedDict):
    """CheckRunPropOutput"""

    title: Union[str, None]
    summary: Union[str, None]
    text: Union[str, None]
    annotations_count: int
    annotations_url: str


class CheckRunPropCheckSuiteType(TypedDict):
    """CheckRunPropCheckSuite"""

    id: int


__all__ = (
    "CheckRunType",
    "CheckRunPropOutputType",
    "CheckRunPropCheckSuiteType",
)
