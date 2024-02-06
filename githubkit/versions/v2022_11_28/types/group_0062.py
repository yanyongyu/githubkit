"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired

from .group_0061 import RunnerLabelType


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
    labels: List[RunnerLabelType]


__all__ = ("RunnerType",)
