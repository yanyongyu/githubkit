"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0074 import RunnerLabelType


class RunnerType(TypedDict):
    """Self hosted runners

    A self hosted runner
    """

    id: int
    runner_group_id: NotRequired[int]
    name: str
    os: str
    status: str
    busy: bool
    labels: list[RunnerLabelType]
    ephemeral: NotRequired[bool]


__all__ = ("RunnerType",)
