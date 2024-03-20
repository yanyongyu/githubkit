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

from .group_0136 import RepositoryRulePullRequestPropParameters


class RepositoryRulePullRequest(GitHubModel):
    """pull_request

    Require all commits be made to a non-target branch and submitted via a pull
    request before they can be merged.
    """

    type: Literal["pull_request"] = Field()
    parameters: Missing[RepositoryRulePullRequestPropParameters] = Field(default=UNSET)


model_rebuild(RepositoryRulePullRequest)

__all__ = ("RepositoryRulePullRequest",)
