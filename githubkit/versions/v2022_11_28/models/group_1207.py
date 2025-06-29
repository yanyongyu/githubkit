"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import ExtraGitHubModel, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class UsersUsernameAttestationsBulkListPostResponse200(GitHubModel):
    """UsersUsernameAttestationsBulkListPostResponse200"""

    attestations_subject_digests: Missing[
        UsersUsernameAttestationsBulkListPostResponse200PropAttestationsSubjectDigests
    ] = Field(default=UNSET, description="Mapping of subject digest to bundles.")
    page_info: Missing[UsersUsernameAttestationsBulkListPostResponse200PropPageInfo] = (
        Field(default=UNSET, description="Information about the current page.")
    )


class UsersUsernameAttestationsBulkListPostResponse200PropAttestationsSubjectDigests(
    ExtraGitHubModel
):
    """UsersUsernameAttestationsBulkListPostResponse200PropAttestationsSubjectDigests

    Mapping of subject digest to bundles.
    """


class UsersUsernameAttestationsBulkListPostResponse200PropPageInfo(GitHubModel):
    """UsersUsernameAttestationsBulkListPostResponse200PropPageInfo

    Information about the current page.
    """

    has_next: Missing[bool] = Field(
        default=UNSET, description="Indicates whether there is a next page."
    )
    has_previous: Missing[bool] = Field(
        default=UNSET, description="Indicates whether there is a previous page."
    )
    next_: Missing[str] = Field(
        default=UNSET, alias="next", description="The cursor to the next page."
    )
    previous: Missing[str] = Field(
        default=UNSET, description="The cursor to the previous page."
    )


model_rebuild(UsersUsernameAttestationsBulkListPostResponse200)
model_rebuild(
    UsersUsernameAttestationsBulkListPostResponse200PropAttestationsSubjectDigests
)
model_rebuild(UsersUsernameAttestationsBulkListPostResponse200PropPageInfo)

__all__ = (
    "UsersUsernameAttestationsBulkListPostResponse200",
    "UsersUsernameAttestationsBulkListPostResponse200PropAttestationsSubjectDigests",
    "UsersUsernameAttestationsBulkListPostResponse200PropPageInfo",
)
