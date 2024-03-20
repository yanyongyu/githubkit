"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class ReposOwnerRepoReleasesPostBody(GitHubModel):
    """ReposOwnerRepoReleasesPostBody"""

    tag_name: str = Field(description="The name of the tag.")
    target_commitish: Missing[str] = Field(
        default=UNSET,
        description="Specifies the commitish value that determines where the Git tag is created from. Can be any branch or commit SHA. Unused if the Git tag already exists. Default: the repository's default branch.",
    )
    name: Missing[str] = Field(default=UNSET, description="The name of the release.")
    body: Missing[str] = Field(
        default=UNSET, description="Text describing the contents of the tag."
    )
    draft: Missing[bool] = Field(
        default=UNSET,
        description="`true` to create a draft (unpublished) release, `false` to create a published one.",
    )
    prerelease: Missing[bool] = Field(
        default=UNSET,
        description="`true` to identify the release as a prerelease. `false` to identify the release as a full release.",
    )
    discussion_category_name: Missing[str] = Field(
        default=UNSET,
        description='If specified, a discussion of the specified category is created and linked to the release. The value must be a category that already exists in the repository. For more information, see "[Managing categories for discussions in your repository](https://docs.github.com/discussions/managing-discussions-for-your-community/managing-categories-for-discussions-in-your-repository)."',
    )
    generate_release_notes: Missing[bool] = Field(
        default=UNSET,
        description="Whether to automatically generate the name and body for this release. If `name` is specified, the specified name will be used; otherwise, a name will be automatically generated. If `body` is specified, the body will be pre-pended to the automatically generated notes.",
    )
    make_latest: Missing[Literal["true", "false", "legacy"]] = Field(
        default=UNSET,
        description="Specifies whether this release should be set as the latest release for the repository. Drafts and prereleases cannot be set as latest. Defaults to `true` for newly published releases. `legacy` specifies that the latest release should be determined based on the release creation date and higher semantic version.",
    )


model_rebuild(ReposOwnerRepoReleasesPostBody)

__all__ = ("ReposOwnerRepoReleasesPostBody",)
