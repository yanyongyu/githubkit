"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_1121 import ReposOwnerRepoPagesPutBodyPropSourceAnyof1


class ReposOwnerRepoPagesPutBodyAnyof3(GitHubModel):
    """ReposOwnerRepoPagesPutBodyAnyof3"""

    cname: Missing[Union[str, None]] = Field(
        default=UNSET,
        description='Specify a custom domain for the repository. Sending a `null` value will remove the custom domain. For more about custom domains, see "[Using a custom domain with GitHub Pages](https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site)."',
    )
    https_enforced: Missing[bool] = Field(
        default=UNSET,
        description="Specify whether HTTPS should be enforced for the repository.",
    )
    build_type: Missing[Literal["legacy", "workflow"]] = Field(
        default=UNSET,
        description="The process by which the GitHub Pages site will be built. `workflow` means that the site is built by a custom GitHub Actions workflow. `legacy` means that the site is built by GitHub when changes are pushed to a specific branch.",
    )
    source: Missing[
        Union[
            Literal["gh-pages", "master", "master /docs"],
            ReposOwnerRepoPagesPutBodyPropSourceAnyof1,
        ]
    ] = Field(default=UNSET)


model_rebuild(ReposOwnerRepoPagesPutBodyAnyof3)

__all__ = ("ReposOwnerRepoPagesPutBodyAnyof3",)
