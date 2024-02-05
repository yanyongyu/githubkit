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


class DeploymentBranchPolicyNamePatternWithType(GitHubModel):
    """Deployment branch and tag policy name pattern"""

    name: str = Field(
        description="The name pattern that branches or tags must match in order to deploy to the environment.\n\nWildcard characters will not match `/`. For example, to match branches that begin with `release/` and contain an additional single slash, use `release/*/*`.\nFor more information about pattern matching syntax, see the [Ruby File.fnmatch documentation](https://ruby-doc.org/core-2.5.1/File.html#method-c-fnmatch)."
    )
    type: Missing[Literal["branch", "tag"]] = Field(
        default=UNSET, description="Whether this rule targets a branch or tag"
    )


model_rebuild(DeploymentBranchPolicyNamePatternWithType)

__all__ = ("DeploymentBranchPolicyNamePatternWithType",)
