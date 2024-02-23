"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class RepositoryRuleParamsRestrictedCommits(GitHubModel):
    """RestrictedCommits

    Restricted commit
    """

    oid: str = Field(description="Full or abbreviated commit hash to reject")
    reason: Missing[str] = Field(default=UNSET, description="Reason for restriction")


model_rebuild(RepositoryRuleParamsRestrictedCommits)

__all__ = ("RepositoryRuleParamsRestrictedCommits",)
