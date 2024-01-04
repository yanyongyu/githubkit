"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from typing_extensions import Annotated

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoActionsRunnersRunnerIdLabelsPostBody(GitHubModel):
    """ReposOwnerRepoActionsRunnersRunnerIdLabelsPostBody"""

    labels: Annotated[List[str], Field(max_length=100, min_length=1)] = Field(
        description="The names of the custom labels to add to the runner."
    )


model_rebuild(ReposOwnerRepoActionsRunnersRunnerIdLabelsPostBody)

__all__ = ("ReposOwnerRepoActionsRunnersRunnerIdLabelsPostBody",)
