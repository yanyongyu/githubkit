"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0149 import RepositoryRuleCommitAuthorEmailPatternPropParameters


class RepositoryRuleCommitAuthorEmailPattern(GitHubModel):
    """commit_author_email_pattern

    Parameters to be used for the commit_author_email_pattern rule
    """

    type: Literal["commit_author_email_pattern"] = Field()
    parameters: Missing[RepositoryRuleCommitAuthorEmailPatternPropParameters] = Field(
        default=UNSET
    )


model_rebuild(RepositoryRuleCommitAuthorEmailPattern)

__all__ = ("RepositoryRuleCommitAuthorEmailPattern",)
