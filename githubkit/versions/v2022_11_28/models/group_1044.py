"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoIssuesIssueNumberLockPutBody(GitHubModel):
    """ReposOwnerRepoIssuesIssueNumberLockPutBody"""

    lock_reason: Missing[Literal["off-topic", "too heated", "resolved", "spam"]] = (
        Field(
            default=UNSET,
            description="The reason for locking the issue or pull request conversation. Lock will fail if you don't use one of these reasons:  \n * `off-topic`  \n * `too heated`  \n * `resolved`  \n * `spam`",
        )
    )


model_rebuild(ReposOwnerRepoIssuesIssueNumberLockPutBody)

__all__ = ("ReposOwnerRepoIssuesIssueNumberLockPutBody",)
