"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_1088 import ReposOwnerRepoPagesPostBodyPropSource


class ReposOwnerRepoPagesPostBodyAnyof1(GitHubModel):
    """ReposOwnerRepoPagesPostBodyAnyof1"""

    build_type: Literal["legacy", "workflow"] = Field(
        description='The process in which the Page will be built. Possible values are `"legacy"` and `"workflow"`.'
    )
    source: Missing[ReposOwnerRepoPagesPostBodyPropSource] = Field(
        default=UNSET,
        description="The source branch and directory used to publish your Pages site.",
    )


model_rebuild(ReposOwnerRepoPagesPostBodyAnyof1)

__all__ = ("ReposOwnerRepoPagesPostBodyAnyof1",)
