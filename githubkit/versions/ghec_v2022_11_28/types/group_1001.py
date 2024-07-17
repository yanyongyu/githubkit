"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Literal
from typing_extensions import TypedDict, NotRequired

from .group_1000 import (
    ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputType,
    ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItemsType,
)


class ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0Type(TypedDict):
    """ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0"""

    name: NotRequired[str]
    details_url: NotRequired[str]
    external_id: NotRequired[str]
    started_at: NotRequired[datetime]
    status: NotRequired[Literal["completed"]]
    conclusion: Literal[
        "action_required",
        "cancelled",
        "failure",
        "neutral",
        "success",
        "skipped",
        "stale",
        "timed_out",
    ]
    completed_at: NotRequired[datetime]
    output: NotRequired[ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputType]
    actions: NotRequired[
        List[ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItemsType]
    ]


__all__ = ("ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0Type",)
