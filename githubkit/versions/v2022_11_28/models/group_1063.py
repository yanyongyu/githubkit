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


class ReposOwnerRepoPullsPullNumberPatchBody(GitHubModel):
    """ReposOwnerRepoPullsPullNumberPatchBody"""

    title: Missing[str] = Field(
        default=UNSET, description="The title of the pull request."
    )
    body: Missing[str] = Field(
        default=UNSET, description="The contents of the pull request."
    )
    state: Missing[Literal["open", "closed"]] = Field(
        default=UNSET,
        description="State of this Pull Request. Either `open` or `closed`.",
    )
    base: Missing[str] = Field(
        default=UNSET,
        description="The name of the branch you want your changes pulled into. This should be an existing branch on the current repository. You cannot update the base branch on a pull request to point to another repository.",
    )
    maintainer_can_modify: Missing[bool] = Field(
        default=UNSET,
        description="Indicates whether [maintainers can modify](https://docs.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) the pull request.",
    )


model_rebuild(ReposOwnerRepoPullsPullNumberPatchBody)

__all__ = ("ReposOwnerRepoPullsPullNumberPatchBody",)