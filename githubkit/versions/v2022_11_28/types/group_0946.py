"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .group_0151 import ArtifactType


class ReposOwnerRepoActionsRunsRunIdArtifactsGetResponse200Type(TypedDict):
    """ReposOwnerRepoActionsRunsRunIdArtifactsGetResponse200"""

    total_count: int
    artifacts: List[ArtifactType]


__all__ = ("ReposOwnerRepoActionsRunsRunIdArtifactsGetResponse200Type",)
