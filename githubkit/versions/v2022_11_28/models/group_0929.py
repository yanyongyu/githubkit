"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoAttestationsPostResponse201(GitHubModel):
    """ReposOwnerRepoAttestationsPostResponse201"""

    id: Missing[int] = Field(default=UNSET, description="The ID of the attestation.")


model_rebuild(ReposOwnerRepoAttestationsPostResponse201)

__all__ = ("ReposOwnerRepoAttestationsPostResponse201",)
