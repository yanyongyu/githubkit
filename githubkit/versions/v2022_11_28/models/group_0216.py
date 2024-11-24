"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser


class CodeScanningCodeqlDatabase(GitHubModel):
    """CodeQL Database

    A CodeQL database.
    """

    id: int = Field(description="The ID of the CodeQL database.")
    name: str = Field(description="The name of the CodeQL database.")
    language: str = Field(description="The language of the CodeQL database.")
    uploader: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    content_type: str = Field(description="The MIME type of the CodeQL database file.")
    size: int = Field(description="The size of the CodeQL database file in bytes.")
    created_at: datetime = Field(
        description="The date and time at which the CodeQL database was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ."
    )
    updated_at: datetime = Field(
        description="The date and time at which the CodeQL database was last updated, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ."
    )
    url: str = Field(
        description="The URL at which to download the CodeQL database. The `Accept` header must be set to the value of the `content_type` property."
    )
    commit_oid: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The commit SHA of the repository at the time the CodeQL database was created.",
    )


model_rebuild(CodeScanningCodeqlDatabase)

__all__ = ("CodeScanningCodeqlDatabase",)
