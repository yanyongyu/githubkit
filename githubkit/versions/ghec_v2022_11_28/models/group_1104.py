"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class ReposOwnerRepoAutolinksPostBody(GitHubModel):
    """ReposOwnerRepoAutolinksPostBody"""

    key_prefix: str = Field(
        description="This prefix appended by certain characters will generate a link any time it is found in an issue, pull request, or commit."
    )
    url_template: str = Field(
        description="The URL must contain `<num>` for the reference number. `<num>` matches different characters depending on the value of `is_alphanumeric`."
    )
    is_alphanumeric: Missing[bool] = Field(
        default=UNSET,
        description="Whether this autolink reference matches alphanumeric characters. If true, the `<num>` parameter of the `url_template` matches alphanumeric characters `A-Z` (case insensitive), `0-9`, and `-`. If false, this autolink reference only matches numeric characters.",
    )


model_rebuild(ReposOwnerRepoAutolinksPostBody)

__all__ = ("ReposOwnerRepoAutolinksPostBody",)
