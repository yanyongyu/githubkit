"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0008 import IntegrationType
from .group_0058 import MinimalRepositoryType
from .group_0179 import PullRequestMinimalType


class SimpleCheckSuiteType(TypedDict):
    """SimpleCheckSuite

    A suite of checks performed on the code of a given code change
    """

    after: NotRequired[Union[str, None]]
    app: NotRequired[Union[IntegrationType, None]]
    before: NotRequired[Union[str, None]]
    conclusion: NotRequired[
        Union[
            None,
            Literal[
                "success",
                "failure",
                "neutral",
                "cancelled",
                "skipped",
                "timed_out",
                "action_required",
                "stale",
                "startup_failure",
            ],
        ]
    ]
    created_at: NotRequired[datetime]
    head_branch: NotRequired[Union[str, None]]
    head_sha: NotRequired[str]
    id: NotRequired[int]
    node_id: NotRequired[str]
    pull_requests: NotRequired[list[PullRequestMinimalType]]
    repository: NotRequired[MinimalRepositoryType]
    status: NotRequired[
        Literal["queued", "in_progress", "completed", "pending", "waiting"]
    ]
    updated_at: NotRequired[datetime]
    url: NotRequired[str]


__all__ = ("SimpleCheckSuiteType",)
