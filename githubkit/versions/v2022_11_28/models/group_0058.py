"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class SelectedActions(GitHubModel):
    """SelectedActions"""

    github_owned_allowed: Missing[bool] = Field(
        default=UNSET,
        description="Whether GitHub-owned actions are allowed. For example, this includes the actions in the `actions` organization.",
    )
    verified_allowed: Missing[bool] = Field(
        default=UNSET,
        description="Whether actions from GitHub Marketplace verified creators are allowed. Set to `true` to allow all actions by GitHub Marketplace verified creators.",
    )
    patterns_allowed: Missing[List[str]] = Field(
        default=UNSET,
        description="Specifies a list of string-matching patterns to allow specific action(s) and reusable workflow(s). Wildcards, tags, and SHAs are allowed. For example, `monalisa/octocat@*`, `monalisa/octocat@v2`, `monalisa/*`.\n\n**Note**: The `patterns_allowed` setting only applies to public repositories.",
    )


model_rebuild(SelectedActions)

__all__ = ("SelectedActions",)
